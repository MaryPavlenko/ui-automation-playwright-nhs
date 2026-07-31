from playwright.sync_api import Page, expect


def test_homepage_has_correct_title(page: Page):
    page.goto("https://digital.nhs.uk/")
    expect(page).to_have_title("NHS England Digital")