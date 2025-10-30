from playwright.sync_api import sync_playwright

browsers = ["chromium", "firefox"]

for browser_type in browsers:
    with sync_playwright() as p:
            if browser_type == "chromium":
                browser = p.chromium.launch(headless=False)
            else:
                browser = p.firefox.launch(headless=False)
            page = browser.new_page()
            page.goto("https://www.saucedemo.com/")
            page.locator("#user-name").fill("standard_user")
            page.locator("#password").fill("secret_sauce")
            page.locator("#login-button").click()
            page.screenshot(path=f"{browser_type}.png")
            browser.close()