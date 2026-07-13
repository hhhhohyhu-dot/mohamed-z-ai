from typing import List


def calculate_ema(
    prices: List[float],
    period: int,
) -> float:
    """
    Returns only the latest EMA value.
    """

    if len(prices) < period:
        return 0.0

    multiplier = 2 / (period + 1)

    ema = sum(prices[:period]) / period

    for price in prices[period:]:
        ema = (price - ema) * multiplier + ema

    return round(ema, 2)


def calculate_ema_series(
    prices: List[float],
    period: int,
) -> List[float]:
    """
    Returns the full EMA series for chart plotting.
    """

    if len(prices) < period:
        return []

    multiplier = 2 / (period + 1)

    ema = sum(prices[:period]) / period

    series = [None] * (period - 1)
    series.append(round(ema, 2))

    for price in prices[period:]:
        ema = (price - ema) * multiplier + ema
        series.append(round(ema, 2))

    return series