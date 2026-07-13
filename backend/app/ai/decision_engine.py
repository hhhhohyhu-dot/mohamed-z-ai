def analyze_market(
    *,
    price: float,
    ema20: float,
    ema50: float,
    ema200: float,
    rsi: float,
    macd: float,
    atr: float,
):

    score = 0

    strengths = []

    warnings = []

    # ==========================================
    # EMA ANALYSIS
    # ==========================================

    if ema20 > ema50 > ema200:

        score += 30

        strengths.append(
            "Strong bullish EMA alignment."
        )

    elif ema20 < ema50 < ema200:

        score -= 30

        warnings.append(
            "Strong bearish EMA alignment."
        )

    elif ema20 > ema50:

        score += 15

        strengths.append(
            "Bullish short-term trend."
        )

    else:

        score -= 15

        warnings.append(
            "Bearish short-term trend."
        )

    # ==========================================
    # RSI
    # ==========================================

    if rsi < 25:

        score += 20

        strengths.append(
            "Market is heavily oversold."
        )

    elif rsi < 35:

        score += 10

        strengths.append(
            "Buying opportunity detected."
        )

    elif rsi > 75:

        score -= 20

        warnings.append(
            "Market is heavily overbought."
        )

    elif rsi > 65:

        score -= 10

        warnings.append(
            "Buying momentum is weakening."
        )

    else:

        score += 5

        strengths.append(
            "RSI is healthy."
        )

    # ==========================================
    # MACD
    # ==========================================

    if macd > 0:

        score += 20

        strengths.append(
            "Bullish momentum confirmed."
        )

    else:

        score -= 20

        warnings.append(
            "Bearish momentum confirmed."
        )

    # ==========================================
    # ATR
    # ==========================================

    volatility = atr / price

    if volatility < 0.01:

        risk = "Low"

        score += 10

        strengths.append(
            "Low volatility."
        )

    elif volatility < 0.02:

        risk = "Medium"

        warnings.append(
            "Moderate volatility."
        )

    else:

        risk = "High"

        score -= 5

        warnings.append(
            "High volatility."
        )

            # ==========================================
    # FINAL DECISION
    # ==========================================

    if score >= 45:

        signal = "BUY"

    elif score <= -45:

        signal = "SELL"

    else:

        signal = "HOLD"

    confidence = min(
        max(abs(score), 55),
        95,
    )

    trend = (
        "Bullish"
        if ema20 > ema50
        else "Bearish"
    )

    reasons = []

    reasons.extend(strengths)

    reasons.extend(warnings)

    # ==========================================
    # RESULT
    # ==========================================

    return {

        "signal": signal,

        "trend": trend,

        "confidence": confidence,

        "risk": risk,

        "score": score,

        "strengths": strengths,

        "warnings": warnings,

        "reasons": reasons,

    }