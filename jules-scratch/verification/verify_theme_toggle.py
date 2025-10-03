from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('index.html')

        # Navigate to the local HTML file
        page.goto(f'file://{file_path}')

        # Take a screenshot of the initial (dark) theme
        page.screenshot(path='jules-scratch/verification/dark_mode.png')

        # Click the theme toggle button
        page.click('#theme-toggle-btn')

        # Wait for the theme change to apply
        page.wait_for_timeout(500)

        # Take a screenshot of the new (light) theme
        page.screenshot(path='jules-scratch/verification/light_mode.png')

        browser.close()

if __name__ == "__main__":
    run()
