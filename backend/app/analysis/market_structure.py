import pandas as pd


def detect_market_structure(
    df: pd.DataFrame,
):
    """
    Detects:

    Bullish
    Bearish
    Range
    """

    highs = df["High"].tail(6).tolist()
    lows = df["Low"].tail(6).tolist()

    higher_highs = 0
    lower_highs = 0

    higher_lows = 0
    lower_lows = 0

    for i in range(1, len(highs)):

        if highs[i] > highs[i - 1]:
            higher_highs += 1
        else:
            lower_highs += 1

        if lows[i] > lows[i - 1]:
            higher_lows += 1
        else:
            lower_lows += 1

    if (
        higher_highs >= 4
        and higher_lows >= 4
    ):
        structure = "Bullish"

    elif (
        lower_highs >= 4
        and lower_lows >= 4
    ):
        structure = "Bearish"

    else:
        structure = "Range"

    return {
        "structure": structure,
        "higherHighs": higher_highs,
        "higherLows": higher_lows,
        "lowerHighs": lower_highs,
        "lowerLows": lower_lows,
    }