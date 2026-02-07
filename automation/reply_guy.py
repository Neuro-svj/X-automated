def reply_to_trending(page, replies):
    page.goto("https://x.com/explore")
    page.wait_for_timeout(4000)

    tweets = page.locator("article").all()[:3]
    for t in tweets:
        t.click()
        time.sleep(3)
        reply_box = page.locator("div[role='textbox']")
        reply_box.type(replies.pop(), delay=60)
        page.locator("div[data-testid='tweetButton']").click()
        time.sleep(120)
