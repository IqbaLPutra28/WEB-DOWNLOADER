# ⚡ Quick Start Guide (5 menit setup)

## 🏃‍♂️ Run Locally (Windows)

### Step 1: Install Python
Buka PowerShell dan jalankan:
```powershell
python --version  # Check if installed
# Jika belum, download dari python.org
```

### Step 2: Install Dependencies
```powershell
cd D:\WEB-DOWNLOADER
pip install -r requirements.txt
```

### Step 3: Jalankan Backend
```powershell
./start.bat
# Atau manual:
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

✅ Backend ready di `http://localhost:8000`

### Step 4: Buka Frontend
```
Buka file: D:\WEB-DOWNLOADER\frontend\index.html di browser
atau
http://localhost:8000/docs (API docs)
```

✅ Selesai! Aplikasi ready untuk digunakan.

---

## 🌐 Deploy ke Render (5 menit)

### Step 1: Push ke GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/web-downloader
git push -u origin main
```

### Step 2: Daftar Render
- Buka https://render.com
- Sign up dengan GitHub account

### Step 3: Create Web Service
1. Click "New +"
2. Select "Web Service"
3. Connect GitHub repo
4. Biarkan setting default (sudah di render.yaml)
5. Click "Deploy"

### Step 4: Tunggu Deployment
- Status akan berubah dari "Building" → "Live"
- URL akan muncul: `https://video-downloader-XXXXX.onrender.com`

✅ Website sudah live!

---

## 🚄 Deploy ke Railway (5 menit)

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
railway login
```

### Step 2: Deploy
```bash
cd D:\WEB-DOWNLOADER
railway init
railway up
```

### Step 3: Cek Domain
```bash
railway status
# Akan muncul URL publik
```

✅ Website live di Railway!

---

## 🐛 Troubleshooting

### Download tidak work?
```
❌ Localhost error?
✅ Cek ulang di browser: http://localhost:8000/api/health

❌ CORS error?
✅ Pastikan backend running dan frontend buka dari file:// atau localhost

❌ URL tidak support?
✅ Hanya YouTube, TikTok, Instagram, Twitter yang support
```

### Deploy error?
```
❌ Build failed?
✅ Cek requirements.txt ada
✅ Lihat logs di Render/Railway dashboard

❌ Module not found?
✅ pip install -r requirements.txt
✅ Cek Python version >= 3.8
```

---

## 📱 Deploy Frontend ke Netlify (Optional)

Untuk separate frontend dari backend:

### Step 1: Create Netlify Account
https://netlify.com

### Step 2: Deploy Frontend
```bash
# Buat folder netlify
mkdir netlify-build
cp frontend/* netlify-build/

# Update API URL di index.html:
# const API_URL = 'https://your-render-backend.onrender.com'
```

### Step 3: Deploy
- Drag and drop folder ke Netlify
- atau connect GitHub

---

## 🔐 Environment Configuration

Saat deploy, set environment variables:

**Render Dashboard:**
1. Settings → Environment
2. Add variable:
   - Key: `PYTHONUNBUFFERED`
   - Value: `1`

**Railway Dashboard:**
- Variables sudah auto-set dari railway.json

---

## ✅ Testing Website

### Local Testing
1. Buka http://localhost:8000
2. Paste YouTube URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
3. Click "Cek Resolusi"
4. Select kualitas
5. Click "Download"

### Production Testing
1. Buka deployed URL
2. Repeat steps 2-5 above
3. File akan download automatically

---

## 📊 Check Health

### Local
```bash
curl http://localhost:8000/api/health
# Response: {"status":"ok","service":"video-downloader"}
```

### Production
```bash
curl https://your-domain.onrender.com/api/health
```

---

## 🚀 Optimization Checklist

- [ ] Update CORS domain di main.py untuk production
- [ ] Setup Cloudflare CDN (optional)
- [ ] Enable rate limiting (lihat RATE_LIMITING.md)
- [ ] Setup error monitoring dengan Sentry
- [ ] Configure email notifications untuk errors

---

## 📚 Full Documentation

- **README.md** - Complete guide
- **DEPLOYMENT.md** - Detailed deployment
- **SECURITY.md** - Security features
- **OPTIMIZATION.md** - Performance tuning
- **PROJECT_SUMMARY.md** - All changes

---

## 🎯 Success Checklist

- [ ] ✅ Backend running locally
- [ ] ✅ Frontend loading
- [ ] ✅ Download working
- [ ] ✅ GitHub pushed
- [ ] ✅ Website deployed
- [ ] ✅ Domain accessible
- [ ] ✅ Download working on production

---

**Semua selesai! Website sudah siap production! 🎉**

Punya pertanyaan? Lihat dokumentasi lengkap di folder project.
