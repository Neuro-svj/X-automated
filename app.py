from flask import Flask, render_template, redirect, request, jsonify
import sqlite3
import threading
import yaml
import os
from automation.scheduler import start_scheduler
from automation.state import bot_state

app = Flask(__name__)

CONFIG_PATH = "config.yaml"
LOG_PATH = "logs/bot.log"
ACCOUNTS_DIR = "accounts"

os.makedirs(ACCOUNTS_DIR, exist_ok=True)


def get_metrics():
    db = sqlite3.connect("db/database.db")
    metrics = db.execute("SELECT * FROM metrics").fetchall()
    db.close()
    return metrics


def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


def save_config(data):
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(data, f)


def list_accounts():
    return os.listdir(ACCOUNTS_DIR)


@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        metrics=get_metrics(),
        config=load_config(),
        running=bot_state.running,
        accounts=list_accounts()
    )


@app.route("/start")
def start_bot():
    if not bot_state.running:
        bot_state.running = True
        bot_state.thread = threading.Thread(target=start_scheduler)
        bot_state.thread.start()
    return redirect("/")


@app.route("/stop")
def stop_bot():
    bot_state.running = False
    return redirect("/")


@app.route("/update_config", methods=["POST"])
def update_config():
    config = load_config()

    config["niche"] = request.form["niche"]
    config["region"] = request.form["region"]
    config["posts_per_day"] = int(request.form["posts_per_day"])
    config["engagement_threshold"] = int(request.form["engagement_threshold"])

    save_config(config)
    return redirect("/")


@app.route("/logs")
def get_logs():
    if not os.path.exists(LOG_PATH):
        return jsonify({"logs": "No logs yet."})

    with open(LOG_PATH, "r") as f:
        content = f.read()

    return jsonify({"logs": content})


@app.route("/accounts")
def accounts():
    return jsonify({"accounts": list_accounts()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
