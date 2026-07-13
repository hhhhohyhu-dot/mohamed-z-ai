import pandas as pd


def detect_price_action(
    df: pd.DataFrame,
):
    """
    Detect basic candlestick patterns.
    """

    if len(df) < 2:
        return {
            "pattern": "Unknown",
            "signal": "HOLD",
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    open_ = last["Open"]
    high = last["High"]
    low = last["Low"]
    close = last["Close"]

    prev_open = prev["Open"]
    prev_close = prev["Close"]

    body = abs(close - open_)
    candle_range = high - low

    upper_shadow = high - max(open_, close)
    lower_shadow = min(open_, close) - low

    # -------------------------
    # DOJI
    # -------------------------

    if candle_range > 0:

        if body <= candle_range * 0.1:

            return {
                "pattern": "Doji",
                "signal": "HOLD",
            }

    # -------------------------
    # HAMMER
    # -------------------------

    if (
        lower_shadow > body * 2
        and upper_shadow < body
    ):

        return {
            "pattern": "Hammer",
            "signal": "BUY",
        }

    # -------------------------
    # SHOOTING STAR
    # -------------------------

    if (
        upper_shadow > body * 2
        and lower_shadow < body
    ):

        return {
            "pattern": "Shooting Star",
            "signal": "SELL",
        }

    # -------------------------
    # BULLISH ENGULFING
    # -------------------------

    if (
        prev_close < prev_open
        and close > open_
        and close > prev_open
        and open_ < prev_close
    ):

        return {
            "pattern": "Bullish Engulfing",
            "signal": "BUY",
        }

    # -------------------------
    # BEARISH ENGULFING
    # -------------------------

    if (
        prev_close > prev_open
        and close < open_
        and open_ > prev_close
        and close < prev_open
    ):

        return {
            "pattern": "Bearish Engulfing",
            "signal": "SELL",
        }

    return {
        "pattern": "None",
        "signal": "HOLD",
    }