from app.services.yfinance_service import get_market_history

from app.indicators.ema import (
    calculate_ema,
    calculate_ema_series,
)

from app.indicators.rsi import (
    calculate_rsi,
    calculate_rsi_series,
)

from app.indicators.macd import (
    calculate_macd,
    calculate_macd_series,
)

from app.indicators.atr import (
    calculate_atr,
    calculate_atr_series,
)

from app.analysis.support_resistance import (
    find_support_resistance,
    nearest_support,
    nearest_resistance,
)

from app.analysis.market_structure import (
    detect_market_structure,
)

from app.analysis.price_action import (
    detect_price_action,
)

from app.analysis.volume import (
    analyze_volume,
)

from app.ai.decision_engine import analyze_market


def _series(df, column: str):

    value = df[column]

    if hasattr(value, "columns"):
        value = value.iloc[:, 0]

    return value.astype(float)


async def get_market_data(
    symbol: str,
    timeframe: str = "1h",
):

    df = await get_market_history(
        symbol,
        timeframe,
    )

    opens = _series(df, "Open")
    highs = _series(df, "High")
    lows = _series(df, "Low")
    closes = _series(df, "Close")
    volumes = _series(df, "Volume")

    close_list = closes.tolist()
    high_list = highs.tolist()
    low_list = lows.tolist()

    current_price = round(
        close_list[-1],
        2,
    )

    ema20 = round(
        calculate_ema(close_list, 20),
        2,
    )

    ema50 = round(
        calculate_ema(close_list, 50),
        2,
    )

    ema200 = round(
        calculate_ema(close_list, 200),
        2,
    )

    rsi = round(
        calculate_rsi(close_list),
        2,
    )

    macd = round(
        calculate_macd(close_list),
        2,
    )

    atr = round(
        calculate_atr(
            high_list,
            low_list,
            close_list,
        ),
        2,
    )

    trend = (
        "Bullish"
        if ema20 > ema50
        else "Bearish"
    )

    sr = find_support_resistance(df)

    support = nearest_support(
        sr["supports"],
        current_price,
    )

    resistance = nearest_resistance(
        sr["resistances"],
        current_price,
    )

    structure = detect_market_structure(
        df,
    )

    price_action = detect_price_action(
        df,
    )

    volume = analyze_volume(
        df,
    )

    decision = analyze_market(
        price=current_price,
        ema20=ema20,
        ema50=ema50,
        ema200=ema200,
        rsi=rsi,
        macd=macd,
        atr=atr,
    )

    signal = decision["signal"]

    confidence = decision["confidence"]

    if support is None:
        support = round(
            current_price - atr,
            2,
        )

    if resistance is None:
        resistance = round(
            current_price + atr,
            2,
        )

    entry = current_price

    stop_loss = round(
        support - atr * 0.5,
        2,
    )

    take_profit1 = round(
        resistance,
        2,
    )

    take_profit2 = round(
        resistance + atr * 2,
        2,
    )

    return {

        "symbol": symbol,

        "timeframe": timeframe,

        "price": current_price,

        "trend": trend,

        "signal": signal,

        "confidence": confidence,

        "risk": decision["risk"],

        "score": decision["score"],

        "reasons": decision["reasons"],

        "ema20": ema20,

        "ema50": ema50,

        "ema200": ema200,

        "rsi": rsi,

        "macd": macd,

        "atr": atr,

        "support": support,

        "resistance": resistance,

        "marketStructure": structure["structure"],

        "priceAction": price_action["pattern"],

        "priceActionSignal": price_action["signal"],

        "volumeStatus": volume["status"],

        "relativeVolume": volume["relativeVolume"],

        "volumeStrength": volume["strength"],

        "entry": entry,

        "stopLoss": stop_loss,

        "takeProfit1": take_profit1,

        "takeProfit2": take_profit2,

        "analysis": (

            f"Trend: {trend}\n"

            f"Signal: {signal}\n"

            f"Confidence: {confidence}%\n"

            f"Structure: {structure['structure']}\n"

            f"Price Action: {price_action['pattern']}\n"

            f"Volume: {volume['status']}\n"

            f"Support: {support}\n"

            f"Resistance: {resistance}\n\n"

            + "\n".join(
                decision["reasons"]
            )

        ),

    }

async def get_chart_data(
    symbol: str,
    timeframe: str = "1h",
):

    df = await get_market_history(
        symbol,
        timeframe,
    )

    opens = _series(df, "Open")
    highs = _series(df, "High")
    lows = _series(df, "Low")
    closes = _series(df, "Close")
    volumes = _series(df, "Volume")

    close_list = closes.tolist()
    high_list = highs.tolist()
    low_list = lows.tolist()

    ema20 = calculate_ema_series(
        close_list,
        20,
    )

    ema50 = calculate_ema_series(
        close_list,
        50,
    )

    ema200 = calculate_ema_series(
        close_list,
        200,
    )

    rsi = calculate_rsi_series(
        close_list,
    )

    macd = calculate_macd_series(
        close_list,
    )

    atr = calculate_atr_series(
        high_list,
        low_list,
        close_list,
    )

    candles = []

    ema20_data = []
    ema50_data = []
    ema200_data = []

    rsi_data = []
    macd_data = []
    atr_data = []

    volume_data = []

    for i, index in enumerate(df.index):

        timestamp = int(
            index.to_pydatetime().timestamp()
        )

        candles.append(
            {
                "time": timestamp,
                "open": round(
                    float(opens.iloc[i]),
                    2,
                ),
                "high": round(
                    float(highs.iloc[i]),
                    2,
                ),
                "low": round(
                    float(lows.iloc[i]),
                    2,
                ),
                "close": round(
                    float(closes.iloc[i]),
                    2,
                ),
            }
        )

        if (
            i < len(ema20)
            and ema20[i] is not None
        ):

            ema20_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        ema20[i]
                    ),
                }
            )

        if (
            i < len(ema50)
            and ema50[i] is not None
        ):

            ema50_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        ema50[i]
                    ),
                }
            )

        if (
            i < len(ema200)
            and ema200[i] is not None
        ):

            ema200_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        ema200[i]
                    ),
                }
            )

        if (
            i < len(rsi)
            and rsi[i] is not None
        ):

            rsi_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        rsi[i]
                    ),
                }
            )

        if (
            i < len(macd)
            and macd[i] is not None
        ):

            macd_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        macd[i]
                    ),
                }
            )

        if (
            i < len(atr)
            and atr[i] is not None
        ):

            atr_data.append(
                {
                    "time": timestamp,
                    "value": float(
                        atr[i]
                    ),
                }
            )

        volume_data.append(
            {
                "time": timestamp,
                "value": float(
                    volumes.iloc[i]
                ),
            }
        )

    return {

        "candles": candles,

        "ema20": ema20_data,

        "ema50": ema50_data,

        "ema200": ema200_data,

        "rsi": rsi_data,

        "macd": macd_data,

        "atr": atr_data,

        "volume": volume_data,

    }