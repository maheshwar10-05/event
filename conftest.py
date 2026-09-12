import pytest
from playwright.sync_api import sync_playwright
from pages.APIlogin import APILogin

@pytest.fixture(scope="session")
def playwright_instance():

    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser_instance(playwright_instance):

    browser = playwright_instance.chromium.launch(
        headless=False
    )

    yield browser

    browser.close()


@pytest.fixture(scope="function")
def api_context(playwright_instance):

    context = playwright_instance.request.new_context(
        base_url="https://api.eventhub.rahulshettyacademy.com"
    )
    


    yield context

    context.dispose()


@pytest.fixture
def page(browser_instance):

    context = browser_instance.new_context()
    page = context.new_page()

    yield page

    context.close()