from playwright.sync_api import Page

from pages.base_page import BasePage


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