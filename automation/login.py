from playwright.sync_api import sync_playwright
import time

def login_and_save():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://x.com/login")

        print("Log into X manually in the opened browser...")
        print("You have 120 seconds.")

        time.sleep(120)

        context.storage_state(path="session.json")
        print("✅ Session saved to session.json")

        browser.close()

if __name__ == "__main__":
    login_and_save()
