from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mohamed Z AI API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {
        "success": True,
        "message": "Mohamed Z AI Backend is Running 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }