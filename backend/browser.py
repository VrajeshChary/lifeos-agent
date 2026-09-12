import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to http://127.0.0.1:5500/...")
        page.goto("http://127.0.0.1:5500/")
        
        print("Page Title:", page.title())
        
        # 2. Detect and click the cookie consent "Accept" button
        accept_btn = page.get_by_role("button", name="Accept")
        if accept_btn.is_visible():
            print("Found cookie consent 'Accept' button. Clicking...")
            accept_btn.click()
            print("Cookie consent modal dismissed.")
        
        # 3. Find application/start button using accessible role and text
        start_btn = page.get_by_role("link", name="Start Application")
        if not start_btn.is_visible():
            start_btn = page.get_by_text("Start Application")
            
        if start_btn.is_visible():
            print(f"Found application button ('{start_btn.inner_text()}'). Clicking...")
            start_btn.click()
            print("Successfully clicked application start button.")
            
        # 6. Wait 5 seconds for visual inspection
        print("Waiting 5 seconds...")
        time.sleep(5)
        
        # 7. Close browser
        print("Closing browser.")
        browser.close()

if __name__ == "__main__":
    main()
