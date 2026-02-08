import os
import time
from playwright.sync_api import sync_playwright


SESSIONS_DIR = "sessions"
DEFAULT_SESSION = "default.json"


def ensure_sessions_dir():
    if not os.path.exists(SESSIONS_DIR):
        os.makedirs(SESSIONS_DIR)


# ===============================
# 1️⃣ MANUAL LOGIN (LOCAL ONLY)
# ===============================
def login_and_save(account_name="default"):
    """
    Opens a visible browser for manual login.
    Saves session to sessions/{account_name}.json
    Run locally only.
    """

    ensure_sessions_dir()
    session_path = os.path.join(SESSIONS_DIR, f"{account_name}.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://x.com/login")

        print("======================================")
        print("Log into X manually in the opened browser")
        print("You have 120 seconds...")
        print("======================================")

        time.sleep(120)

        context.storage_state(path=session_path)
        print(f"✅ Session saved to {session_path}")

        browser.close()


# ===============================
# 2️⃣ START BROWSER (PRODUCTION)
# ===============================
def start_browser(account_name="default", headless=True):
    """
    Launch browser using saved session.
    """

    ensure_sessions_dir()
    session_path = os.path.join(SESSIONS_DIR, f"{account_name}.json")

    if not os.path.exists(session_path):
        raise FileNotFoundError(
            f"Session file not found for account '{account_name}'. "
            f"Run login_and_save('{account_name}') locally first."
        )

    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )

    context = browser.new_context(storage_state=session_path)
    page = context.new_page()

    return p, browser, context, page


# ===============================
# 3️⃣ VALIDATE LOGIN
# ===============================
def validate_session(page):
    """
    Check if logged in by verifying homepage loads without redirect.
    """

    page.goto("https://x.com/home", timeout=60000)
    time.sleep(5)

    if "login" in page.url:
        return False

    return True


# ===============================
# 4️⃣ SAVE UPDATED SESSION
# ===============================
def save_session(context, account_name="default"):
    ensure_sessions_dir()
    session_path = os.path.join(SESSIONS_DIR, f"{account_name}.json")
    context.storage_state(path=session_path)


# ===============================
# 5️⃣ CLEAN SHUTDOWN
# ===============================
def close_browser(p, browser):
    browser.close()
    p.stop()


# ===============================
# CLI USAGE
# ===============================
if __name__ == "__main__":
    # Example:
    # python automation/browser.py
    # Creates sessions/default.json

    login_and_save("default")
