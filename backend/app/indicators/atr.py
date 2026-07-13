from typing import List


def calculate_atr(
    highs: List[float],
    lows: List[float],
    closes: List[float],
    period: int = 14,
) -> float:
    """
    Returns the latest ATR value.
    """

    if len(highs) < period:
        return 0.0

    trs = []

    for i in range(1, len(highs)):

        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1]),
        )

        trs.append(tr)

    atr = sum(trs[-period:]) / period

    return round(atr, 2)


def calculate_atr_series(
    highs: List[float],
    lows: List[float],
    closes: List[float],
    period: int = 14,
) -> List[float]:
    """
    Returns the full ATR series.
    """

    if len(highs) < period:
        return []

    trs = []

    atr_values = [None] * period

    for i in range(1, len(highs)):

        tr = max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1]),
        )

        trs.append(tr)

        if len(trs) >= period:
            atr = sum(trs[-period:]) / period
            atr_values.append(round(atr, 2))

    return atr_values