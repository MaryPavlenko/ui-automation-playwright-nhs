from playwright.sync_api import Page


class BookingHomePage:
    """Home page of the Restful Booker Platform demo site (Shady Meadows B&B). This is a public demo application built specifically for practising test automation, which makes it suitable for running in CI."""

    BASE_URL = "https://automationintesting.online"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """Open the home page."""
        self.page.goto(self.BASE_URL)

    def get_heading(self):
        """Return the level 1 heading."""
        return self.page.get_by_role("heading", level=1)

    def get_room_booking_links(self):
        """Return all room booking links. The page also contains an anchor link labelled 'Book Now' that scrolls to the booking section (href='#booking'). Filtering by href keeps this locator stable regardless of link order or number of rooms."""
        return self.page.locator('a[href^="/reservation/"]')

    def get_first_room_booking_link(self):
        """Return the first room booking link."""
        return self.get_room_booking_links().first

    def get_contact_form_field(self, name: str):
        """Return a contact form textbox by its accessible name"""
        return self.page.get_by_role("textbox", name=name)

    def get_submit_button(self):
        """Return the contact form submit button."""
        return self.page.get_by_role("button", name="Submit")