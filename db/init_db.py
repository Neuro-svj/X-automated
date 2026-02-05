import sqlite3
from pathlib import Path

DB_PATH = Path("db/database.db")
DB_PATH.parent.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Posts table
c.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT,
    type TEXT,               -- tweet | thread | reply
    niche TEXT,
    region TEXT,
    posted_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Metrics table
c.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    post_id INTEGER,
    likes INTEGER DEFAULT 0,
    reposts INTEGER DEFAULT 0,
    replies INTEGER DEFAULT 0,
    impressions INTEGER DEFAULT 0,
    collected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(post_id) REFERENCES posts(id)
)
""")

# Strategy feedback
c.execute("""
CREATE TABLE IF NOT EXISTS strategy_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signal TEXT,
    value TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("✅ Database initialized")
