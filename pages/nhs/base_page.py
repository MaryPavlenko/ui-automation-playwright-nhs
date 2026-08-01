from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects. Holds the Playwright page and elements shared across every page on the site (header navigation, breadcrumbs, footer)."""

    BASE_URL = "https://digital.nhs.uk"

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        """Open a page by path relative to the base URL."""
        self.page.goto(f"{self.BASE_URL}{path}")

    def get_header(self):
        """Return the page header (banner) region."""
        return self.page.get_by_role("banner")

    def get_nav_link(self, name: str):
        """Return a primary navigation link by name, scoped to the header
        so it does not clash with the same text elsewhere (e.g. breadcrumbs)."""
        return self.get_header().get_by_role("link", name=name, exact=True)

    def get_primary_nav_links(self):
        """Return the six primary navigation links: name -> expected path."""
        return {
            "Services": "/services",
            "Data": "/data",
            "Cyber": "/cyber",
            "Developer": "/developer",
            "News": "/news",
            "About": "/about-nhs-digital",
        }

    def get_breadcrumbs(self):
        """Return the breadcrumb navigation region."""
        return self.page.get_by_label("Breadcrumbs")