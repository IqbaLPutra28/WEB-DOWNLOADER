# Rate Limiting Guide

## Add Rate Limiting untuk Production

Rate limiting mencegah abuse dan DDoS attacks.

### Install slowapi

```bash
pip install slowapi
```

Update `backend/main.py`:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

# Initialize limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def _rate_limit_exceeded_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Terlalu banyak request. Coba lagi nanti."}
    )

# Apply rate limits to endpoints
@app.post("/api/formats")
@limiter.limit("10/minute")  # 10 requests per minute
def get_formats(request: VideoRequest, request_req = Depends()):
    # ... existing code

@app.post("/api/download")
@limiter.limit("5/minute")  # 5 downloads per minute per IP
def download_video(request: VideoRequest, background_tasks: BackgroundTasks, request_req = Depends()):
    # ... existing code
```

### Rate Limits yang Direkomendasikan

| Endpoint | Limit | Alasan |
|----------|-------|--------|
| `/api/formats` | 10/min | Scan video info |
| `/api/download` | 5/min | Bandwidth intensive |
| `/api/get-file` | 20/min | File download |
| `/api/health` | 100/min | Health checks |

### Alternative: Redis-based Rate Limiting

Untuk production dengan multiple instances:

```python
from slowapi.backends import RedisBackend
from slowapi import Limiter

limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)
```

Render.com redis: Cek di Add-ons
Railway redis: `railway add redis`

---

Implementasi rate limiting wajib untuk production!
