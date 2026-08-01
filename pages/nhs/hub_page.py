from playwright.sync_api import Page

from pages.nhs.base_page import BasePage


class HubPage(BasePage):
    """Developer and integration hub landing page (/developer)."""

    PATH = "/developer"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        """Open the Developer hub page."""
        super().open(self.PATH)

    def get_heading(self):
        """Return the level 1 heading of the hub page."""
        return self.page.get_by_role("heading", level=1)

    def get_primary_cta_links(self):
        """Return the three primary call-to-action links on the hub. Keys are stable labels; values are the expected relative URLs."""
        return {
            "Get started": "/developer/getting-started",
            "Browse catalogue": "/developer/api-catalogue",
            "View documentation": "/developer/guides-and-documentation",
        }

    def get_cta_link(self, name: str):
        """Return a primary call-to-action link by its accessible name."""
        return self.page.get_by_role("link", name=name)