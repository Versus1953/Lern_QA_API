import allure
import os
import json
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from allure_commons.types import AttachmentType
from tools.playwright.pages import initialize_playwright_page
from io import StringIO


USERNAME_VDI_OWNER = os.getenv('USERNAME_VDI_OWNER')
PASSWORD_VDI_OWNER = os.getenv('PASSWORD_VDI_OWNER')
URL_VDI_AUTH = os.getenv('APP_URL')


HEADLESS = os.getenv('HEADLESS').lower() == 'true'
BROWSERS_CONFIG = StringIO(os.getenv('BROWSERS'))


@pytest.fixture(params=BROWSERS_CONFIG)
def page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright, 
        test_name=request.node.name,
        browser_type=request.param)
    

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()
    page = context.new_page()

    registration_page = LoginPage(page=page)
    registration_page.visit(URL_VDI_AUTH)
    registration_page.fill_login_form(
        username=USERNAME_VDI_OWNER,
        password=PASSWORD_VDI_OWNER)
    registration_page.click_login_submit_button()
    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture(params=BROWSERS_CONFIG)  
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state="browser-state.json"
    )
