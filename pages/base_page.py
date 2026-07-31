from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects. Holds the Playwright page and
    elements shared across every page on the site (header navigation,
    breadcrumbs, footer)."""

    BASE_URL = "https://digital.nhs.uk"

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        """Open a page by path relative to the base URL."""
        self.page.goto(f"{self.BASE_URL}{path}")

    def get_breadcrumbs(self):
        """Return the breadcrumb navigation region."""
        return self.page.get_by_role("navigation", name="Breadcrumb")

    def get_primary_navigation(self):
        """Return the primary site navigation region."""
        return self.page.get_by_role("navigation").first