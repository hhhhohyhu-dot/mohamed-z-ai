from typing import List

import pandas as pd


def find_support_resistance(
    df: pd.DataFrame,
    window: int = 5,
):

    highs = df["High"].tolist()
    lows = df["Low"].tolist()

    resistance = []
    support = []

    for i in range(window, len(df) - window):

        high = highs[i]
        low = lows[i]

        if high == max(
            highs[i - window : i + window + 1]
        ):
            resistance.append(high)

        if low == min(
            lows[i - window : i + window + 1]
        ):
            support.append(low)

    support = sorted(
        list(set(round(x, 2) for x in support))
    )

    resistance = sorted(
        list(set(round(x, 2) for x in resistance))
    )

    return {

        "supports": support,

        "resistances": resistance,

    }


def nearest_support(
    supports: List[float],
    price: float,
):

    values = [
        s
        for s in supports
        if s < price
    ]

    if not values:
        return None

    return max(values)


def nearest_resistance(
    resistances: List[float],
    price: float,
):

    values = [
        r
        for r in resistances
        if r > price
    ]

    if not values:
        return None

    return min(values)