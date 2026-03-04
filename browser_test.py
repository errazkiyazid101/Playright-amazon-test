from playwright.sync_api import sync_playwright
import time

AMAZON_URL = "https://www.amazon.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        viewport={"width": 1280, "height": 800},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"
    )

    page = context.new_page()

    print("Opening Amazon...")
    page.goto(AMAZON_URL, timeout=60000)

    # Wait for body to be visible
    page.wait_for_selector("body")

    # Wait specifically for Amazon homepage element
    page.wait_for_selector("#nav-logo-sprites", timeout=15000)

    print("Amazon homepage loaded.")

    # Extra wait to ensure full render
    time.sleep(5)

    # Take screenshot
    page.screenshot(path="amazon_loaded.png", full_page=False)

    print("Screenshot saved as amazon_loaded.png")
    print("Browser will stay open for 20 seconds...")

    time.sleep(20)

    browser.close()