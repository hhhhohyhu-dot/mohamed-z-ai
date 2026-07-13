from fastapi import APIRouter

from app.news.news_service import get_market_news

router = APIRouter(
    prefix="/api/news",
    tags=["News"],
)


@router.get("/{symbol}")
async def news(symbol: str):
    return await get_market_news(symbol)