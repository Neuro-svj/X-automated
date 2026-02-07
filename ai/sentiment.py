def sentiment_score(text):
    """
    Simple placeholder sentiment scoring.
    Returns a score between -1 and 1.
    """

    positive_words = ["good", "great", "win", "growth", "profit", "success"]
    negative_words = ["bad", "loss", "fail", "drop", "risk", "down"]

    score = 0

    for word in positive_words:
        if word in text.lower():
            score += 1

    for word in negative_words:
        if word in text.lower():
            score -= 1

    # Normalize
    return max(-1, min(1, score / 3))
