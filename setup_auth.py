"""
Helper script: accepts the NHS cookie banner once and saves the browser storage state to storage_state.json.

Run manually when storage_state.json is missing or expired: python setup_auth.py

The generated storage_state.json is gitignored and must not be committed.
"""

from playwright.sync_api import sync_playwright

STORAGE_STATE_PATH = "storage_state.json"
BASE_URL = "https://digital.nhs.uk/developer"


def save_consent_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL, wait_until="domcontentloaded")

        # Wait for the consent button to appear, then click it.
        # Cookiebot loads asynchronously, so we wait explicitly.
        consent_button = page.get_by_role("button", name="Use necessary cookies only")
        consent_button.wait_for(state="visible", timeout=60000)
        consent_button.click()

        # Wait until the banner is gone, confirming the consent cookie is written.
        cookie_dialog = page.get_by_role("dialog", name="Your privacy and cookies")
        cookie_dialog.wait_for(state="hidden", timeout=60000)

        context.storage_state(path=STORAGE_STATE_PATH)
        print(f"Consent state saved to {STORAGE_STATE_PATH}")

        browser.close()

if __name__ == "__main__":
    save_consent_state()