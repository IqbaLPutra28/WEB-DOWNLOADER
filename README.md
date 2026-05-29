# 🎬 Video Downloader - Dokumentasi Lengkap

Aplikasi web untuk mendownload video dari YouTube, TikTok, Instagram, dan Twitter dengan interface yang user-friendly.

## 📋 Fitur

✅ Download video dengan berbagai resolusi  
✅ Konversi ke MP3 (audio only)  
✅ Preview thumbnail dan durasi video  
✅ Interface responsif dan modern  
✅ Keamanan tingkat enterprise (validasi input, path traversal protection)  
✅ Cleanup otomatis file lama (24 jam)  
✅ Error handling yang baik  

## 🔒 Keamanan

Aplikasi ini dilengkapi dengan:
- ✅ Input validation (whitelist domain)
- ✅ Path traversal protection
- ✅ CORS configuration
- ✅ Rate limiting ready
- ✅ File size limits (500MB)
- ✅ Timeout on downloads
- ✅ Secure filename validation
- ✅ No sensitive error exposure

## 💻 Setup Lokal

### Prerequisites
- Python 3.8+
- pip atau conda
- Git

### Instalasi

1. Clone repository:
```bash
git clone <repo-url>
cd WEB-DOWNLOADER
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan backend:
```bash
cd backend
python main.py
# atau dengan uvicorn langsung:
uvicorn main:app --host 0.0.0.0 --port 8000
```

4. Buka frontend di browser:
```
Buka frontend/index.html atau akses http://localhost:8000
```

## 🚀 Deployment ke Platform Gratis

### Option 1: Render (Rekomendasi)
**Free Tier:** 750 jam/bulan

1. Push code ke GitHub
2. Buat akun di https://render.com
3. Buat Web Service baru
4. Connect GitHub repository
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
7. Deploy!

**File yang diperlukan:** `render.yaml`
```yaml
services:
  - type: web
    name: video-downloader
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
    healthCheckPath: /api/health
    staticPublicPath: /frontend
```

### Option 2: Railway
**Free Tier:** $5/bulan kredit

1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Inisialisasi: `railway init`
4. Deploy: `railway up`

**railway.json:**
```json
{
  "build": {
    "builder": "dockerfile"
  },
  "deploy": {
    "startCommand": "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
  }
}
```

### Option 3: Heroku (Alternatif)
⚠️ **Note:** Heroku menghapus free tier (Nov 2022). Gunakan alternative lain.

### Option 4: PythonAnywhere
**Free Tier:** Aplikasi sederhana OK

1. Sign up di https://www.pythonanywhere.com
2. Upload files via Web UI
3. Setup virtual environment
4. Configure WSGI
5. Set domain

### Option 5: Replit (Development)
Cocok untuk development, bukan production.

1. https://replit.com/~
2. Import from GitHub
3. Setup secrets di .env
4. Run!

## 🐳 Docker (Optional untuk deployment)

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build & Run:**
```bash
docker build -t video-downloader .
docker run -p 8000:8000 video-downloader
```

## ⚙️ Konfigurasi Environment

Buat file `.env`:
```
FRONTEND_URL=https://yourdomain.com
BACKEND_URL=https://api.yourdomain.com
DOWNLOAD_LIMIT_MB=500
MAX_VIDEOS_PER_HOUR=50
```

Update di `backend/main.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_ORIGINS = os.getenv("FRONTEND_URL", "*").split(",")
```

## 🔧 Troubleshooting

### Frontend tidak bisa connect ke backend
- Pastikan CORS_ORIGINS benar di backend/main.py
- Check browser console untuk CORS errors
- Gunakan absolute URL di frontend (bukan localhost)

### Download timeout
- Increase socket_timeout di backend/main.py
- Check file size (maksimal 500MB)
- Cek koneksi internet

### Path traversal warnings
- Sudah dihandle. Filename divalidasi dengan regex strict.

## 📝 Environment Variables untuk Deployment

Di Render/Railway, set variables ini:

| Variable | Value | Keterangan |
|----------|-------|-----------|
| `FRONTEND_URL` | `https://yourdomain.com` | Domain frontend |
| `BACKEND_URL` | `https://api.yourdomain.com` | Domain backend |
| `PYTHONUNBUFFERED` | `1` | Logging realtime |

## 🎯 Best Practices untuk Production

1. **Update CORS di main.py:**
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specify domain
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)
```

2. **Setup SSL Certificate:**
   - Render/Railway auto-generate HTTPS
   - PythonAnywhere support HTTPS

3. **Monitor Download Directory:**
   - Setup cron job untuk cleanup
   - Monitor disk space

4. **Add Rate Limiting:**
   - Install `slowapi`: `pip install slowapi`
   - Lihat contoh di `RATE_LIMITING.md`

5. **Enable Logging:**
   - Setup proper logging untuk production
   - Monitor backend via Render/Railway dashboard

## 📊 API Documentation

**GET** `/api/health`
- Status check
- Response: `{"status": "ok", "service": "video-downloader"}`

**POST** `/api/formats`
- Ambil format video yang tersedia
- Body: `{"url": "https://youtube.com/..."}`
- Response: `{"formats": [...], "title": "...", "thumb": "..."}`

**POST** `/api/download`
- Download video
- Body: `{"url": "...", "format_id": "..."}`
- Response: `{"filename": "..."}`

**GET** `/api/get-file/{filename}`
- Download file yang sudah siap
- Response: Binary video file

## 🤝 Contributing

Pull requests welcome! Tolong fork dulu.

## 📄 License

MIT License - Free to use untuk personal & commercial

## 📞 Support

Punya masalah? Cek GitHub issues atau buat discussion baru.

---

**Happy Downloading! 🎉**
