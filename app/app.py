from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
from app.routes import router
from fastapi.templating import Jinja2Templates


app = FastAPI(
    title="Email Spam Detection API",
    description="Random Forest based spam detection service.",
    version="1.0.0",
    )

app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/health")
async def root():
    return {
        "status": "API Running...",
        "timestamp": datetime.now(tz=timezone.utc)
    }


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )