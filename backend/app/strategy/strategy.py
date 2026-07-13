from app.indicators.ema import calculate_ema
from app.indicators.rsi import calculate_rsi
from app.indicators.macd import calculate_macd


def get_signal(closes: list[float]) -> str:
    """
    Returns:
    BUY
    SELL
    HOLD
    """

    if len(closes) < 200:
        return "HOLD"

    ema20 = calculate_ema(closes, 20)
    ema50 = calculate_ema(closes, 50)
    ema200 = calculate_ema(closes, 200)

    rsi = calculate_rsi(closes)

    macd = calculate_macd(closes)

    buy = (
        ema20 > ema50
        and ema50 > ema200
        and macd > 0
        and 45 <= rsi <= 70
    )

    sell = (
        ema20 < ema50
        and ema50 < ema200
        and macd < 0
        and 30 <= rsi <= 55
    )

    if buy:
        return "BUY"

    if sell:
        return "SELL"

    return "HOLD"