from typing import List


def calculate_rsi(
    prices: List[float],
    period: int = 14,
) -> float:
    """
    Returns the latest RSI value.
    """

    if len(prices) <= period:
        return 50.0

    gains = []
    losses = []

    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]

        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 2)


def calculate_rsi_series(
    prices: List[float],
    period: int = 14,
) -> List[float]:
    """
    Returns the full RSI series.
    """

    if len(prices) <= period:
        return []

    rsi_values = [None] * period

    for end in range(period + 1, len(prices) + 1):

        window = prices[:end]

        gains = []
        losses = []

        for i in range(1, len(window)):
            change = window[i] - window[i - 1]

            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            rsi = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        rsi_values.append(round(rsi, 2))

    return rsi_values