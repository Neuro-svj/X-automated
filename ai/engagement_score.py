def score(tweet):
    score = 0
    if "?" in tweet: score += 2
    if len(tweet) < 180: score += 2
    if any(w in tweet.lower() for w in ["you", "this", "why"]): score += 1
    if "thread" in tweet.lower(): score += 1
    return score
