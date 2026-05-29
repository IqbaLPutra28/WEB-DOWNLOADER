# 🚀 Step-by-Step Deployment Guide

Panduan lengkap deploy ke free hosting.

## Render.com (Rekomendasi Terbaik)

### Step 1: Prepare GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/web-downloader
git push -u origin main
```

### Step 2: Create Render Account
- Buka https://render.com
- Sign up dengan GitHub account

### Step 3: Create Web Service
1. Click "New +"
2. Select "Web Service"
3. Connect GitHub repository
4. Configure:
   - **Name:** video-downloader
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** Free

### Step 4: Environment Variables
Di Render dashboard:
```
PYTHONUNBUFFERED = 1
FRONTEND_URL = https://video-downloader.render.com
```

### Step 5: Deploy
Render akan auto-deploy setiap push ke GitHub.

**Estimated Time:** 2-5 menit first deployment

---

## Railway.app (Alternatif)

### Step 1: Create Railway Account
https://railway.app

### Step 2: Create New Project
```bash
npm install -g @railway/cli
railway login
cd WEB-DOWNLOADER
railway init
```

### Step 3: Add Services
```bash
railway service add
# Pilih Python
```

### Step 4: Deploy
```bash
railway up
```

Dashboard: https://railway.app/dashboard

---

## PythonAnywhere (Untuk Testing)

### Step 1: Sign Up
https://www.pythonanywhere.com (free tier tersedia)

### Step 2: Upload Files
- Upload via Web Interface atau Git
- Setup Virtual Environment

### Step 3: Create Web App
1. Web Tab → Add a new web app
2. Choose Python framework: Flask/FastAPI
3. Point ke `backend/main.py`

### Step 4: Configure
Buat `.env` di home directory dengan settings.

---

## Replit (Development)

### Step 1: Import Project
https://replit.com/github/username/web-downloader

### Step 2: Setup
Replit akan auto-detect Python project.

### Step 3: Run
Click "Run" button.

⚠️ **Catatan:** Free tier Replit punya limitation, tapi OK untuk development/demo.

---

## Using Custom Domain

### Dengan Render:
1. Settings → Custom Domain
2. Add domain (ex: video.yourdomain.com)
3. Update DNS records sesuai instruksi

### Dengan Railway:
1. Projects → Environment → Railway Domain
2. Setup custom domain di DNS provider

---

## Monitoring & Logs

### Render Logs:
Dashboard → Logs tab (realtime)

### Railway Logs:
`railway logs`

### Setup Uptime Monitoring:
- UptimeRobot (free): https://uptimerobot.com
- Create HTTP check untuk `/api/health`

---

## Common Issues & Solutions

### 1. "Module not found: fastapi"
**Solusi:**
```bash
pip install -r requirements.txt --force-reinstall
```

### 2. "Port already in use"
Render/Railway auto-handle port. Pastikan start command menggunakan `$PORT`.

### 3. CORS errors di frontend
**Buka backend/main.py dan update:**
```python
allow_origins=["https://your-domain.netlify.app"]
```

### 4. 502 Bad Gateway
- Check backend logs
- Pastikan start command benar
- Cek memory usage (free tier punya limitation)

### 5. Deployment stuck
- Cek file size (pastikan < 1GB)
- Hapus unnecessary files
- Create `.railwayignore` atau `.deployignore`

---

## Performance Tips

1. **Optimize yt-dlp:**
```python
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    'socket_timeout': 30,
    # ... other options
}
```

2. **Enable caching di frontend:**
```javascript
// Add cache headers
headers: {
    'Cache-Control': 'max-age=3600'
}
```

3. **Use CDN untuk static files:**
   - Cloudflare (free)
   - Netlify (untuk frontend)

---

## Scaling (Jika Traffic Tinggi)

Jika free tier tidak cukup:

### Upgrade Options:
1. **Render:** Upgrade ke paid plan ($7/bulan)
2. **Railway:** Add more credits ($5/bulan or more)
3. **DigitalOcean App Platform:** $5/bulan
4. **Heroku alternatives:** Fly.io, Replit Pro

---

## Maintenance Checklist

- [ ] Setup GitHub Actions untuk testing
- [ ] Monitor logs daily
- [ ] Keep dependencies updated: `pip list --outdated`
- [ ] Test error cases regularly
- [ ] Backup download directory
- [ ] Monitor disk space

---

**🎉 Selesai! Website sudah live!**

Akses melalui:
- Render: `https://video-downloader.render.com`
- Railway: URL dari dashboard

---

## 📞 Quick Support

**Error saat deployment?**
1. Check logs (Render/Railway dashboard)
2. Verify `requirements.txt` ada
3. Cek Python version kompatibilitas
4. Lihat GitHub Issues

**Perlu help?**
- Buat Discussion di GitHub
- Buka Issue dengan screenshot

---

Semoga deployment sukses! 🚀
