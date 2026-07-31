import re

from playwright.sync_api import Page, expect


def test_developer_hub_loads_without_cookie_banner(page: Page):
    page.goto("https://digital.nhs.uk/developer")

    # Заголовок страницы верный
    expect(page).to_have_title(re.compile("Developer and integration hub"))

    # Cookie-баннер НЕ появляется, потому что consent загружен из storage_state
    cookie_dialog = page.get_by_role("dialog", name="Your privacy and cookies")
    expect(cookie_dialog).not_to_be_visible()