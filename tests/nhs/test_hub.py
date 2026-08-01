import re

import pytest
from playwright.sync_api import Page, expect

from pages.nhs.hub_page import HubPage


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


@pytest.mark.hub
def test_primary_entry_points(page: Page):
    """NHS-HUB-02: Three primary entry points are present with correct targets."""
    hub_page = HubPage(page)
    hub_page.open()

    cta_links = hub_page.get_primary_cta_links()

    for name, expected_path in cta_links.items():
        link = hub_page.get_cta_link(name)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", expected_path)