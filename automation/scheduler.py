import time
import yaml
import os
from automation.logger import log
from automation.state import bot_state
from automation.browser import post_content
from ai.reinforcement import choose_strategy, reward_strategy
from ai.sentiment import sentiment_score

ACCOUNTS_DIR = "accounts"


def list_accounts():
    if not os.path.exists(ACCOUNTS_DIR):
        return []
    return os.listdir(ACCOUNTS_DIR)


def generate_post(niche, region, strategy):
    return f"{strategy.upper()} | {niche} insights in {region} 🚀"


def start_scheduler():
    while bot_state.running:

        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        accounts = list_accounts()

        if not accounts:
            log("No accounts found.")
            time.sleep(60)
            continue

        for account in accounts:

            strategy = choose_strategy()
            content = generate_post(
                config["niche"],
                config["region"],
                strategy
            )

            score = sentiment_score(content)

            if score < 0:
                log(f"{account}: Negative sentiment skipped.")
                continue

            try:
                post_content(account, content)
                log(f"{account}: Posted successfully.")

                engagement = 50  # placeholder
                reward_strategy(strategy, engagement)

            except Exception as e:
                log(f"{account}: Posting failed - {str(e)}")

            time.sleep(10)

        time.sleep(config["shadow_safe_interval"])
