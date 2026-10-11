from playwright.sync_api import sync_playwright
from pathlib import Path

configPath = Path.home() / "Automatic-Login-Wifi" / "AutomaticLoginWifi.conf"
with open(configPath, "r") as file:
    config = file.readlines()

wifiUsername = config[1].strip()
wifiPassword = config[2].strip()
wifiPage = config[3].strip()


with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="/usr/bin/google-chrome-stable",
        headless=False
    );
    
    page = browser.new_page();
    page.goto(wifiPage);
    page.locator("input[placeholder='Username']").fill(wifiUsername);
    page.locator("input[placeholder='Password']").fill(wifiPassword);
    page.locator("input[type='submit']").click();
    browser.close();