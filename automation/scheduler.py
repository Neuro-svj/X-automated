import time
import yaml
from automation.learning_engine import analyze_performance
from automation.logger import log
from automation.state import bot_state

def start_scheduler():
    while bot_state.running:
        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        log(f"Running scheduler for niche: {config['niche']}")

        # Placeholder for post creation & posting
        log("Generated and posted content")

        analyze_performance()

        time.sleep(config["shadow_safe_interval"])
