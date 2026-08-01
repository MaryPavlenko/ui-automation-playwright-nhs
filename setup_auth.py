"""
Helper script: writes the NHS/Cookiebot consent cookie directly and saves
the browser storage state to storage_state.json.

We set the consent cookie programmatically instead of clicking the banner,
because the Cookiebot banner is not reliably shown in all environments
(e.g. CI data-centre IPs). This is more robust and environment-independent.

Run manually when storage_state.json is missing or expired:
    python setup_auth.py
"""

import json
import time

from playwright.sync_api import sync_playwright

STORAGE_STATE_PATH = "storage_state.json"
BASE_URL = "https://digital.nhs.uk/developer"


def build_consent_cookie():
    """Build a Cookiebot 'necessary only' consent cookie value."""
    consent = {
        "stamp": "auto-generated",
        "necessary": True,
        "preferences": False,
        "statistics": False,
        "marketing": False,
        "method": "explicit",
        "ver": 1,
        "utc": int(time.time() * 1000),
        "region": "gb",
    }
    # Cookiebot stores the value as a JSON-like string
    value = json.dumps(consent, separators=(",", ":"))
    return {
        "name": "CookieConsent",
        "value": value,
        "domain": "digital.nhs.uk",
        "path": "/",
        "secure": True,
        "sameSite": "Lax",
    }


def save_consent_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Set the consent cookie before visiting the site
        context.add_cookies([build_consent_cookie()])

        # Visit once so the state is associated with the site
        page = context.new_page()
        page.goto(BASE_URL, wait_until="domcontentloaded")

        context.storage_state(path=STORAGE_STATE_PATH)
        print(f"Consent state saved to {STORAGE_STATE_PATH}")

        browser.close()


if __name__ == "__main__":
    save_consent_state()