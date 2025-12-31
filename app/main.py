from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.routers import web, api

app = FastAPI(title="SFERA AI Carousel")

BASE_DIR = Path(__file__).resolve().parent.parent

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.mount("/media", StaticFiles(directory=str(BASE_DIR / "media")), name="media")

app.include_router(web.router)
app.include_router(api.router)
