import re
from datetime import date

import pytest
from playwright.sync_api import Page, expect

from pages.booking_demo.home_page import BookingHomePage


@pytest.mark.booking_demo
@pytest.mark.smoke
def test_home_page_loads(page: Page):
    """DEMO-01: Home page loads with the expected level 1 heading."""
    home = BookingHomePage(page)
    home.open()

    heading = home.get_heading()
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Welcome to Shady Meadows B&B")


@pytest.mark.booking_demo
def test_room_card_has_booking_link(page: Page):
    """DEMO-02: Room cards expose a working 'Book now' link."""
    home = BookingHomePage(page)
    home.open()

    book_now = home.get_first_room_booking_link()
    expect(book_now).to_be_visible()
    expect(book_now).to_have_attribute("href", re.compile(r"^/reservation/\d+"))


@pytest.mark.booking_demo
def test_booking_link_uses_current_dates(page: Page):
    """DEMO-03: Booking link contains a check-in date matching today.

    The site generates check-in and check-out dates dynamically, so the test
    compares against today's date rather than a hard-coded value.
    """
    home = BookingHomePage(page)
    home.open()

    book_now = home.get_first_room_booking_link()
    href = book_now.get_attribute("href")

    today = date.today().isoformat()
    assert f"checkin={today}" in href, f"Expected checkin={today} in {href}"
    assert "checkout=" in href


@pytest.mark.booking_demo
def test_contact_form_shows_validation_errors_when_empty(page: Page):
    """DEMO-04: Submitting the empty contact form shows validation errors.

    Negative scenario. No data is created, because the submission is expected
    to fail validation.
    """
    home = BookingHomePage(page)
    home.open()

    home.get_submit_button().click()

    # At least one validation message is displayed
    alerts = page.get_by_role("alert")
    expect(alerts.first).to_be_visible()