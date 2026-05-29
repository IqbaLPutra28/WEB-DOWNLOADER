# 🚀 Optimization & Performance Guide

## Frontend Optimization

### 1. Lazy Loading Images
```javascript
// Sudah implemented dengan loading="lazy"
<img src="thumbnail.jpg" alt="Video" loading="lazy">
```

### 2. CSS/JS Minification
Untuk production, minify files:
```bash
npm install -g cssnano terser
terser styles.css -c > styles.min.css
terser index.html -c > index.min.html
```

### 3. Enable Caching
Tambah Cache Headers di `backend/main.py`:
```python
@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html", headers={
        "Cache-Control": "public, max-age=3600"
    })
```

### 4. Compress Assets
```python
from fastapi.middleware.gzip import GZIPMiddleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)
```

---

## Backend Optimization

### 1. Connection Pooling
```python
# yt-dlp sudah optimal, tapi bisa tambah caching
from functools import lru_cache

@lru_cache(maxsize=100)
def get_format_cache(url):
    # Implement caching untuk format requests
    pass
```

### 2. Async Processing
```python
# Background task untuk cleanup
from background_tasks import BackgroundTask

# Sudah digunakan di download_video
background_tasks.add_task(cleanup_old_files)
```

### 3. Memory Management
```python
# Set memory limits untuk yt-dlp
ydl_opts = {
    'socket_timeout': 30,
    'max_filesize': 500 * 1024 * 1024,  # Batasi ukuran file
    'quiet': True,  # Kurangi memory output
}
```

---

## Database Optimization (Future)

Jika menambahkan database:
```python
# Install
pip install sqlalchemy psycopg2-binary

# Use connection pooling
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@db:5432/app"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
)
```

---

## CDN Integration (Render/Railway)

### Cloudflare (Free Tier)
1. Signup di https://cloudflare.com
2. Add domain
3. Update DNS records
4. Enable Auto Minify, Caching, etc.

Benefits:
- ✅ Global CDN
- ✅ DDoS protection
- ✅ Auto compression
- ✅ Free SSL

---

## Performance Metrics

Target:
- First Contentful Paint (FCP): < 1.5s
- Largest Contentful Paint (LCP): < 2.5s
- Cumulative Layout Shift (CLS): < 0.1
- Time to Interactive (TTI): < 3.8s

Test dengan:
- https://pagespeed.web.dev
- https://www.webpagetest.org

---

## Database Query Optimization

Jika menambahkan database log:
```python
# Create indexes
CREATE INDEX idx_video_id ON downloads(video_id);
CREATE INDEX idx_created_at ON downloads(created_at);

# Use pagination
@app.get("/api/downloads")
def list_downloads(skip: int = 0, limit: int = 10):
    return db.query(Download).offset(skip).limit(limit).all()
```

---

## Load Testing

Test kapasitas backend:
```bash
pip install locust

# locustfile.py
from locust import HttpUser, task

class VideoDownloadUser(HttpUser):
    @task
    def check_formats(self):
        self.client.post("/api/formats", json={"url": "https://youtube.com/watch?v=test"})
```

Run:
```bash
locust -f locustfile.py --host http://localhost:8000
```

---

## Monitoring

Setup monitoring untuk production:

### Option 1: Sentry (Error tracking)
```bash
pip install sentry-sdk

import sentry_sdk
sentry_sdk.init("your-sentry-dsn")
```

### Option 2: New Relic (APM)
```bash
pip install newrelic
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program ...
```

### Option 3: Simple Logging
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

---

## Checklist Sebelum Deploy Production

- [ ] Enable HTTPS (auto di Render/Railway)
- [ ] Setup security headers (SECURITY.md)
- [ ] Rate limiting active (RATE_LIMITING.md)
- [ ] Error logging enabled
- [ ] CORS properly configured
- [ ] Input validation strict
- [ ] File cleanup working
- [ ] Backups scheduled
- [ ] Monitoring active
- [ ] CDN configured

---

## Quick Performance Wins

1. **Minify frontend**
   - Reduce CSS/JS size 40-60%

2. **Enable compression**
   - Already configured with GZIP

3. **Optimize images**
   - WebP format (browser support check)
   - Progressive JPEG

4. **Service Workers**
   - For offline support

5. **Lazy load resources**
   - Already implemented

---

**Target deployment time: < 2 menit
Target startup time: < 5 detik**

Optimize berdasarkan monitoring metrics! 📊
