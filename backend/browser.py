import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://127.0.0.1:5500/")
        
        print("Page Title:", page.title())
        print("Main Heading:", page.locator("h1").inner_text())
        
        # 1. Click "Apply Now" button if present
        apply_btn = page.get_by_text("Apply Now")
        if apply_btn.is_visible():
            apply_btn.click()
        
        # 2. Fill Full Name
        page.get_by_label("Full Name").fill("Jugraj Demo")
        
        # 3. Fill Email
        page.get_by_label("Email Address").fill("jugraj@demo.com")
        
        # 4. Fill Skills
        page.get_by_label("Skills").fill("Python, AI, Playwright")
        
        # 5. Form submission omitted intentionally
        
        # 6. Wait 5 seconds for visual inspection
        time.sleep(5)
        
        # 7. Close browser
        browser.close()

if __name__ == "__main__":
    main()
