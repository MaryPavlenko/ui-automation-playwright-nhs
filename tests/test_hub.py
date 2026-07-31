import re

import pytest
from playwright.sync_api import Page, expect

from pages.hub_page import HubPage


@pytest.mark.hub
@pytest.mark.smoke
def test_hub_title_and_heading(page: Page):
    """NHS-HUB-01: Hub page has correct title and a single level 1 heading."""
    hub_page = HubPage(page)
    hub_page.open()

    # Title contains the expected text
    expect(page).to_have_title(re.compile("Developer and integration hub"))

    # Exactly one level 1 heading, with the expected text
    heading = hub_page.get_heading()
    expect(heading).to_have_count(1)
    expect(heading).to_have_text("Developer and integration hub")