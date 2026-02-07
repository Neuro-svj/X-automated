import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(message):
    logging.info(message)
