import os
from playwright.sync_api import sync_playwright

ACCOUNTS_DIR = "accounts"
os.makedirs(ACCOUNTS_DIR, exist_ok=True)


def start_browser(username, headless=True):
    """
    Starts browser session for a specific account.
    """
    session_path = f"{ACCOUNTS_DIR}/{username}/storage_state.json"

    p = sync_playwright().start()
    browser = p.chromium.launch(
        headless=headless,
        args=["--disable-blink-features=AutomationControlled"]
    )

    if os.path.exists(session_path):
        context = browser.new_context(storage_state=session_path)
    else:
        context = browser.new_context()

    page = context.new_page()

    return p, browser, context, page


def manual_login(username):
    """
    Run this locally to login manually and save session.
    """
    os.makedirs(f"{ACCOUNTS_DIR}/{username}", exist_ok=True)

    p, browser, context, page = start_browser(username, headless=False)

    page.goto("https://x.com/login")

    print("Login manually in browser. You have 90 seconds...")
    page.wait_for_timeout(90000)

    context.storage_state(
        path=f"{ACCOUNTS_DIR}/{username}/storage_state.json"
    )

    print("Session saved successfully.")

    browser.close()
    p.stop()


def post_content(username, content):
    """
    Headless posting using saved session.
    """
    p, browser, context, page = start_browser(username, headless=True)

    page.goto("https://x.com/compose/post")
    page.wait_for_timeout(3000)

    page.fill("div[role='textbox']", content)
    page.keyboard.press("Control+Enter")

    page.wait_for_timeout(3000)

    browser.close()
    p.stop()
