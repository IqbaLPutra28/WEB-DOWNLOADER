from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel, HttpUrl, validator
import yt_dlp
import os
import shutil
import re
from urllib.parse import urlparse
from pathlib import Path
import time

# Konfigurasi
DOWNLOAD_DIR = "downloads"
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
ALLOWED_DOMAINS = ["youtube.com", "youtu.be", "tiktok.com", "instagram.com", "twitter.com", "x.com"]
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

app = FastAPI(title="Video Downloader API", version="1.0")

# Middleware keamanan
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])  # Ubah ke domain spesifik saat deploy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ubah ke ["https://yourdomain.com"] saat deploy
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    max_age=3600,
)

# Buat direktori jika belum ada
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR, mode=0o755)

def validate_url(url: str) -> bool:
    """Validasi URL agar aman"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        # Hapus www. untuk normalisasi
        domain = domain.replace("www.", "")
        return any(allowed in domain for allowed in ALLOWED_DOMAINS)
    except:
        return False

class VideoRequest(BaseModel):
    url: HttpUrl
    format_id: str = None
    
    @validator('url')
    def validate_video_url(cls, v):
        url_str = str(v)
        if not validate_url(url_str):
            raise ValueError("Domain tidak didukung. Gunakan YouTube, TikTok, Instagram, atau Twitter.")
        if len(url_str) > 2048:
            raise ValueError("URL terlalu panjang")
        return v
    
    @validator('format_id')
    def validate_format(cls, v):
        if v and not re.match(r'^[a-zA-Z0-9]+$', v):
            raise ValueError("Format ID tidak valid")
        return v

def cleanup_old_files():
    """Hapus file yang berusia lebih dari 24 jam"""
    try:
        now = time.time()
        for filename in os.listdir(DOWNLOAD_DIR):
            filepath = os.path.join(DOWNLOAD_DIR, filename)
            if os.path.isfile(filepath):
                if os.stat(filepath).st_mtime < now - 86400:  # 24 jam
                    os.remove(filepath)
    except Exception as e:
        print(f"Error cleanup files: {e}")

@app.get("/api/health")
def health_check():
    """Endpoint untuk monitoring"""
    return {"status": "ok", "service": "video-downloader"}

@app.post("/api/formats")
def get_formats(request: VideoRequest):
    """Ambil format video yang tersedia"""
    try:
        cleanup_old_files()
        
        ydl_opts = {
            'quiet': True,
            'user_agent': USER_AGENT,
            'socket_timeout': 30,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(str(request.url), download=False)
            
            # Validasi info
            if not info or 'formats' not in info:
                raise HTTPException(status_code=400, detail="Format video tidak ditemukan")
            
            formats = [{"format_id": "bestaudio", "res": "MP3 (Audio Only)"}]
            seen_resolutions = {"MP3 (Audio Only)"}
            
            # Filter hanya format video dengan kualitas
            for f in info.get('formats', []):
                if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                    height = f.get('height')
                    if height and f.get('ext') in ['mp4', 'webm']:
                        res = f"{height}p"
                        if res not in seen_resolutions:
                            formats.append({
                                "format_id": f.get('format_id'),
                                "res": res,
                                "size": f.get('filesize', 'Unknown')
                            })
                            seen_resolutions.add(res)
            
            # Batasi jumlah format (max 10)
            formats = formats[:10]
            
            return {
                "formats": formats,
                "title": info.get('title', 'Video')[:200],  # Batasi panjang
                "thumb": info.get('thumbnail', '')[:2048],
                "duration": info.get('duration', 0)
            }
    except yt_dlp.utils.DownloadError:
        raise HTTPException(status_code=400, detail="URL video tidak valid atau tidak dapat diakses")
    except Exception as e:
        # Jangan expose error detail kepada user
        raise HTTPException(status_code=400, detail="Gagal mengambil informasi video")

@app.post("/api/download")
def download_video(request: VideoRequest, background_tasks: BackgroundTasks):
    """Download video dengan format yang dipilih"""
    try:
        # Cleanup files lama
        cleanup_old_files()
        
        # Validasi format_id
        if request.format_id and len(request.format_id) > 50:
            raise HTTPException(status_code=400, detail="Format ID tidak valid")
        
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s'),
            'format': request.format_id or 'best[ext=mp4]/best',
            'user_agent': USER_AGENT,
            'socket_timeout': 30,
            'no_warnings': True,
            'quiet': True,
            'max_filesize': MAX_FILE_SIZE,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(str(request.url), download=True)
            filename = os.path.basename(ydl.prepare_filename(info))
            
            # Validasi file yang diunduh
            filepath = os.path.join(DOWNLOAD_DIR, filename)
            if not os.path.exists(filepath):
                raise HTTPException(status_code=500, detail="File download gagal")
            
            # Schedule untuk menghapus file setelah diunduh (1 jam)
            background_tasks.add_task(cleanup_old_files)
            
            return {"filename": filename, "title": info.get('title', 'Video')}
    except yt_dlp.utils.DownloadError:
        raise HTTPException(status_code=400, detail="Download gagal - URL tidak valid atau terlalu besar")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Terjadi kesalahan saat download")

@app.get("/api/get-file/{filename}")
def get_file(filename: str):
    """Download file yang telah diunduh"""
    try:
        # Validasi filename untuk mencegah path traversal
        if '..' in filename or '/' in filename or '\\' in filename:
            raise HTTPException(status_code=400, detail="Nama file tidak valid")
        
        # Whitelist hanya alphanumeric, dash, underscore, dan dot
        if not re.match(r'^[a-zA-Z0-9._-]+$', filename):
            raise HTTPException(status_code=400, detail="Nama file tidak valid")
        
        file_path = os.path.join(DOWNLOAD_DIR, filename)
        
        # Verifikasi path ada dalam download directory
        real_path = os.path.realpath(file_path)
        real_download_dir = os.path.realpath(DOWNLOAD_DIR)
        
        if not real_path.startswith(real_download_dir):
            raise HTTPException(status_code=403, detail="Akses ditolak")
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File tidak ditemukan")
        
        return FileResponse(
            file_path,
            media_type='application/octet-stream',
            filename=filename,
            headers={"Content-Disposition": f"attachment; filename=\"{filename}\""}
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Terjadi kesalahan")