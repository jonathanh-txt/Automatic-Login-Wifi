from playwright.sync_api import sync_playwright
from pathlib import Path

configPath = Path.home() / "Automatic-Login-Wifi" / "AutomaticLoginWifi.conf"
with open(configPath, "r") as file:
    config = file.readlines()

wifiUsername = config[1].strip()
wifiPassword = config[2].strip()


with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/usr/bin/google-chrome-stable",
        headless=False
    );
    
    page = browser.new_page();
    page.goto("http://50.50.1.1");
    page.locator("input[placeholder='Username']").fill("900");
    page.locator("input[placeholder='Password']").fill("900");
    page.locator("input[type='submit']").click();
    browser.close();