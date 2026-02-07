import sqlite3
import yaml
from automation.logger import log

def analyze_performance():
    db = sqlite3.connect("db/database.db")
    rows = db.execute("SELECT likes, rts, replies FROM metrics").fetchall()
    db.close()

    if not rows:
        return

    avg_engagement = sum([r[0] + r[1] + r[2] for r in rows]) / len(rows)

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    if avg_engagement > config["engagement_threshold"]:
        config["posts_per_day"] += 1
        log("Increasing posts per day due to high engagement")

    with open("config.yaml", "w") as f:
        yaml.dump(config, f)
