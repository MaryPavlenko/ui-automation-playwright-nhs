import pytest
from playwright.sync_api import Page, expect

from pages.nhs.hub_page import HubPage


@pytest.mark.navigation
@pytest.mark.smoke
def test_primary_navigation_links(page: Page):
    """NHS-NAV-01: Primary navigation contains all six sections with correct targets."""
    hub_page = HubPage(page)
    hub_page.open()

    nav_links = hub_page.get_primary_nav_links()

    for name, expected_path in nav_links.items():
        link = hub_page.get_nav_link(name)
        expect(link).to_be_visible()
        expect(link).to_have_attribute("href", expected_path)