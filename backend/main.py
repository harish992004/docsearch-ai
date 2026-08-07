from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="DocSearch AI",
    description="AI-powered document intelligence platform",
    version="0.1.0"
)

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to DocSearch AI 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }