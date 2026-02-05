def log_metrics(db, tweet_id, likes, rts):
    db.execute(
        "INSERT INTO metrics VALUES (?, ?, ?)",
        (tweet_id, likes, rts)
    )
