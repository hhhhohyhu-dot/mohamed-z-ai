from .ema import (
    calculate_ema,
    calculate_ema_series,
)


def calculate_macd(prices):
    """
    Returns the latest MACD value.
    """

    ema12 = calculate_ema(prices, 12)
    ema26 = calculate_ema(prices, 26)

    return round(ema12 - ema26, 2)


def calculate_macd_series(prices):
    """
    Returns the full MACD series.
    """

    ema12 = calculate_ema_series(prices, 12)
    ema26 = calculate_ema_series(prices, 26)

    macd = []

    for i in range(len(prices)):

        if (
            i >= len(ema12)
            or i >= len(ema26)
            or ema12[i] is None
            or ema26[i] is None
        ):
            macd.append(None)
        else:
            macd.append(
                round(ema12[i] - ema26[i], 2)
            )

    return macd