def analyze_news(article: dict):
    """
    Simple AI sentiment analysis.
    """

    title = article.get("headline", "")
    summary = article.get("summary", "")

    text = f"{title} {summary}".lower()

    bullish_words = [
        "growth",
        "profit",
        "record",
        "beats",
        "buy",
        "bullish",
        "surge",
        "rise",
        "strong",
        "positive",
    ]

    bearish_words = [
        "loss",
        "drop",
        "fall",
        "bearish",
        "sell",
        "weak",
        "decline",
        "crash",
        "negative",
        "miss",
    ]

    bullish_score = sum(word in text for word in bullish_words)
    bearish_score = sum(word in text for word in bearish_words)

    if bullish_score > bearish_score:
        sentiment = "Bullish"
        impact = 85
        confidence = 90

    elif bearish_score > bullish_score:
        sentiment = "Bearish"
        impact = 85
        confidence = 90

    else:
        sentiment = "Neutral"
        impact = 60
        confidence = 75

    return {
        "title": title,
        "summary": summary,
        "sentiment": sentiment,
        "impact": impact,
        "confidence": confidence,
        "assets": [],
    }