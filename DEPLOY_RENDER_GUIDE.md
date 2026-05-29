# 🚀 DEPLOY KE RENDER - STEP BY STEP

Panduan lengkap deploy web downloader ke Render.com (FREE)

## ✅ Prerequisites

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Git installed (`git --version`)
- [ ] GitHub account
- [ ] Render account (daftar gratis di render.com)
- [ ] Project files ready di `d:\WEB-DOWNLOADER`

---

## STEP 1: Install Tools (Jika belum ada)

### Install Git untuk Windows
1. Buka: https://git-scm.com/download/win
2. Download & install (default settings OK)
3. Restart PowerShell

### Verify instalasi
```powershell
git --version      # Harus show version
python --version   # Harus 3.8+
```

---

## STEP 2: Push Kode ke GitHub (10 menit)

Buka **PowerShell** dan jalankan commands ini:

```powershell
# 1. Navigate ke project folder
cd d:\WEB-DOWNLOADER

# 2. Initialize Git (jika belum)
git init
git config user.name "IqbaLPutra28"
git config user.email "your-email@example.com"

# 3. Add semua files
git add .

# 4. First commit
git commit -m "Initial commit - Video Downloader with security"

# 5. Set branch ke main
git branch -M main

# 6. Add remote repository
git remote add origin https://github.com/IqbaLPutra28/web-downloader.git

# 7. Push ke GitHub
git push -u origin main
```

### ⚠️ Perhatian:
- Jika `git push` minta login, ikuti prompt di browser
- Atau generate Personal Access Token di GitHub Settings

**Verify:** Buka https://github.com/IqbaLPutra28/web-downloader
- Harus muncul semua files (README.md, requirements.txt, backend/, dll)

---

## STEP 3: Daftar Render.com (Gratis) (5 menit)

1. Buka: https://render.com
2. Click **Sign Up**
3. Sign up dengan GitHub account
4. Authorize Render ke GitHub
5. Done! Dashboard ready.

---

## STEP 4: Deploy ke Render (5 menit)

### Di Render Dashboard:

1. **Click "New +"** (top-right)
2. **Select "Web Service"**
3. **Connect Repository:**
   - Search: `web-downloader`
   - Click pada repository
   - Click "Connect"

4. **Configure Settings:**
   - **Name:** `video-downloader` (atau nama lain)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** `Free` ✅

5. **Environment Variables** (opsional):
   - Add: `PYTHONUNBUFFERED = 1`

6. **Click "Create Web Service"**

### Status Monitor:
- Akan muncul "Building..." (tunggu 2-5 menit)
- Berubah menjadi "Live" ✅

### Domain Render:
- URL akan muncul: `https://video-downloader-xxxxx.onrender.com`
- **Ini URL website Anda!**

---

## STEP 5: Test Website (2 menit)

### Test di browser:

1. Buka: `https://video-downloader-xxxxx.onrender.com`
   - Ganti `xxxxx` dengan random string di dashboard

2. Paste YouTube URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

3. Click "Cek Resolusi"

4. Select quality dan "Download Sekarang"

✅ **Jika berhasil download, website sudah live!**

---

## Troubleshooting

### ❌ "Build failed"
```
Solusi:
1. Check logs di Render (click service → Logs)
2. Verify requirements.txt ada
3. Verify Python version
4. Re-deploy: Settings → Redeploy
```

### ❌ "Cannot GET /"
```
Solusi:
1. Buka: https://your-domain.onrender.com/api/health
2. Harus return: {"status":"ok"}
3. Frontend di: https://your-domain.onrender.com/docs
```

### ❌ "CORS Error"
```
Jika download error di browser console:
1. Buka backend/main.py
2. Ubah CORS settings:
   allow_origins=["https://your-domain.onrender.com"]
3. Commit & push
4. Render auto-redeploy
```

### ❌ "503 Service Unavailable"
```
1. Service masih loading (tunggu 1-2 menit)
2. Atau out of memory (free tier punya limit)
3. Check dashboard status
```

---

## 🔧 Advanced Setup (Opsional)

### Custom Domain
1. Render Dashboard → Settings
2. Custom Domain
3. Point DNS ke Render
4. Setup SSL (auto)

### Environment Variables
Untuk production safety:
```
FRONTEND_URL=https://your-domain.onrender.com
BACKEND_URL=https://your-domain.onrender.com
PYTHONUNBUFFERED=1
```

### Auto-Deploy
- Already setup! Setiap push ke GitHub, Render auto-deploy.

### Logs & Monitoring
- Render Dashboard → Logs (real-time)
- Check untuk errors atau issues

---

## 📊 Performance Tips

- Free tier: Cukup untuk 100-500 users/hari
- Jika traffic tinggi: Upgrade ke Paid ($7/month)
- Response time: 1-2 detik (normal)
- Deploy time: 2-5 menit

---

## Konfirmasi Deployment

### Checklist:
- [ ] Git installed & configured
- [ ] Code pushed ke GitHub
- [ ] Render account created
- [ ] Web Service deployed
- [ ] Status "Live" di Render
- [ ] Website accessible via URL
- [ ] Download test successful

---

## 🎉 DONE!

Website Anda sekarang **LIVE** di Render!

**URL:** https://video-downloader-xxxxx.onrender.com

Share URL ini ke teman untuk mencoba! 🚀

---

## Next Steps (Opsional):

1. **Setup Custom Domain** (beli domain + point ke Render)
2. **Add Rate Limiting** (lihat RATE_LIMITING.md)
3. **Monitor dengan Sentry** (error tracking)
4. **Add Database** (untuk history)

---

**Need Help?**
- Check Render logs: Dashboard → Logs
- GitHub issues: Create issue jika ada error
- Re-read DEPLOYMENT.md untuk detail

**Semua selesai! Website sudah live! 🎉**
