from playwright.sync_api import sync_playwright

def start_browser():
    p = sync_playwright().start()
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(storage_state="session.json")
    page = context.new_page()
    return p, browser, context, page

def save_session(context):
    context.storage_state(path="session.json")
