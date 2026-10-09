from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/usr/bin/google-chrome-stable",
        headless=False
    )
    
    page = browser.new_page()
    page.goto("http://50.50.1.1")
    page.locator("input[placeholder='Username']").fill("900")
    page.locator("input[placeholder='Password']").fill("900")
    page.locator("input[type='submit']").click()
    browser.close()