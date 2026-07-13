from fastapi import APIRouter

from app.services.market_service import (
    get_market_data,
    get_chart_data,
)

from app.services.yfinance_service import (
    get_market_history,
)

router = APIRouter(
    prefix="/api",
    tags=["Market"],
)


@router.post("/analyze")
async def analyze(data: dict):

    symbol = data.get("symbol", "XAU/USD")
    timeframe = data.get("timeframe", "1h")

    return await get_market_data(
        symbol=symbol,
        timeframe=timeframe,
    )


@router.get("/chart/{symbol}")
async def chart(
    symbol: str,
    timeframe: str = "1h",
):

    return await get_chart_data(
        symbol=symbol,
        timeframe=timeframe,
    )


@router.get("/test/{symbol}")
async def test(
    symbol: str,
    timeframe: str = "1h",
):

    df = await get_market_history(
        symbol=symbol,
        timeframe=timeframe,
    )

    close = df["Close"]
    volume = df["Volume"]

    # yfinance الجديد يرجع MultiIndex
    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    if hasattr(volume, "columns"):
        volume = volume.iloc[:, 0]

    return {
        "success": True,
        "symbol": symbol,
        "timeframe": timeframe,
        "rows": len(df),
        "last_close": round(float(close.iloc[-1]), 2),
        "last_volume": round(float(volume.iloc[-1]), 2),
    }