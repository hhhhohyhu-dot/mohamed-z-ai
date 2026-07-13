import pandas as pd


def analyze_volume(
    df: pd.DataFrame,
    period: int = 20,
):
    """
    Analyze trading volume.
    """

    if len(df) < period + 1:

        return {

            "status": "Unknown",

            "relativeVolume": 0,

            "strength": 0,

            "message": "Not enough data.",

        }

    volume = df["Volume"]

    current = float(volume.iloc[-1])

    average = float(
        volume.tail(period).mean()
    )

    rvol = current / average

    # ------------------------
    # VERY STRONG
    # ------------------------

    if rvol >= 2:

        return {

            "status": "Very Strong",

            "relativeVolume": round(
                rvol,
                2,
            ),

            "strength": 100,

            "message": "Exceptional volume confirms market movement.",

        }

    # ------------------------
    # STRONG
    # ------------------------

    if rvol >= 1.5:

        return {

            "status": "Strong",

            "relativeVolume": round(
                rvol,
                2,
            ),

            "strength": 80,

            "message": "Strong participation from buyers or sellers.",

        }

    # ------------------------
    # NORMAL
    # ------------------------

    if rvol >= 0.8:

        return {

            "status": "Normal",

            "relativeVolume": round(
                rvol,
                2,
            ),

            "strength": 60,

            "message": "Normal trading activity.",

        }

    # ------------------------
    # WEAK
    # ------------------------

    return {

        "status": "Weak",

        "relativeVolume": round(
            rvol,
            2,
        ),

        "strength": 25,

        "message": "Weak volume. Signal needs confirmation.",

    }