import time
import random

def post_tweet(page, text):
    page.goto("https://x.com/compose/tweet")
    time.sleep(random.uniform(3,5))

    box = page.locator("div[role='textbox']")
    box.click()
    box.type(text, delay=random.randint(40,90))

    time.sleep(random.uniform(2,4))
    page.locator("div[data-testid='tweetButtonInline']").click()
