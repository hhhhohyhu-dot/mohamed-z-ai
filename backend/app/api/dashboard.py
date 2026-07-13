from fastapi import APIRouter

from app.services.market_service import (
    get_market_data,
    get_chart_data,
)

from app.news.news_service import (
    get_market_news,
)

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/{symbol}")
async def dashboard(
    symbol: str,
    timeframe: str = "1h",
):

    result = {}

    try:
        result["market"] = await get_market_data(
            symbol,
            timeframe,
        )
    except Exception as e:
        result["market_error"] = str(e)

    try:
        result["chart"] = await get_chart_data(
            symbol,
            timeframe,
        )
    except Exception as e:
        result["chart_error"] = str(e)

    try:
        result["news"] = await get_market_news(symbol)
    except Exception as e:
        result["news_error"] = str(e)

    return result