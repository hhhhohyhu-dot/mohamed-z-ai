from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.dashboard import router as dashboard_router
from app.api.market import router as market_router
from app.api.news import router as news_router


app = FastAPI(
    title="Mohamed Z AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(market_router)
app.include_router(news_router)
app.include_router(dashboard_router)


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