import os
import httpx

from dotenv import load_dotenv

from app.news.news_ai import analyze_news

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")


async def get_market_news(symbol: str):

    url = "https://finnhub.io/api/v1/company-news"

    params = {
        "symbol": symbol.upper(),
        "from": "2026-07-01",
        "to": "2026-07-12",
        "token": FINNHUB_API_KEY,
    }

    async with httpx.AsyncClient(timeout=20) as client:

        response = await client.get(url, params=params)

        response.raise_for_status()

        articles = response.json()

    result = []

    for article in articles[:10]:

        result.append(analyze_news(article))

    return result