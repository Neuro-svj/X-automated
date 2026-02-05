def adjust_strategy(metrics):
    if metrics["avg_likes"] < 5:
        return "more hooks"
    return "threads"
