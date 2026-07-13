import yfinance as yf


SYMBOLS = {
    "AAPL": "AAPL",
    "MSFT": "MSFT",
    "NVDA": "NVDA",
    "TSLA": "TSLA",
    "AMZN": "AMZN",
    "META": "META",

    "BTC": "BTC-USD",
    "ETH": "ETH-USD",

    "XAUUSD": "GC=F",
    "GOLD": "GC=F",
    "SILVER": "SI=F",

    "NAS100": "^NDX",
    "SP500": "^GSPC",
    "DJI": "^DJI",

    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X",
}


TIMEFRAMES = {
    "1m": ("7d", "1m"),
    "5m": ("60d", "5m"),
    "15m": ("60d", "15m"),
    "1h": ("2y", "1h"),
    "4h": ("2y", "1h"),
    "1d": ("10y", "1d"),
}


def normalize_symbol(symbol: str) -> str:
    symbol = symbol.upper().replace("/", "").replace("-", "")
    return SYMBOLS.get(symbol, symbol)


async def get_market_history(
    symbol: str,
    timeframe: str = "1h",
):
    ticker_symbol = normalize_symbol(symbol)

    period, interval = TIMEFRAMES.get(
        timeframe,
        TIMEFRAMES["1h"],
    )

    ticker = yf.Ticker(ticker_symbol)

    df = ticker.history(
        period=period,
        interval=interval,
        auto_adjust=True,
    )

    if df.empty:
        raise Exception(f"No data found for {ticker_symbol}")

    return df