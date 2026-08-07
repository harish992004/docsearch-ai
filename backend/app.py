from fastapi import FastAPI

app = FastAPI(
    title="DocSearch AI",
    description="AI-powered OCR search platform",
    version="0.1.0"
)


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