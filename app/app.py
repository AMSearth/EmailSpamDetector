from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
from app.routes import router
from fastapi.templating import Jinja2Templates
from slowapi import  _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.rate_limiting import limiter

app = FastAPI(
    title="Email Spam Detection API",
    description="Random Forest based spam detection service.",
    version="1.0.0",
    )

# add rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# add api router
app.include_router(router)

# mount files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/health")
async def health():
    return {
        "status": "API Running...",
        "timestamp": datetime.now(tz=timezone.utc)
    }


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )