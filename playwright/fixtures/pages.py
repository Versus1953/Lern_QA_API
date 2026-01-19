import pytest 
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.vdi_overview_page import VdiOverviewPage
from tools.cleanup import CleanupManager
from pages.AD_page import ADPage
from pages.user_and_role_page import UserAndRolePage
from pages.vspace_page import VspacePage
from pages.desktop_page import DesktopPage
from pages.template_page import TemplatePage
from playwright.sync_api import Playwright, Page


@pytest.fixture
def login_page(page:Page)-> LoginPage:
    return LoginPage(page=page)

@pytest.fixture
def vdi_overview_page(page:Page)-> VdiOverviewPage:
    return VdiOverviewPage(page=page)

@pytest.fixture
def vdi_overview_page_with_state(page_with_state:Page)-> VdiOverviewPage:
    return VdiOverviewPage(page=page_with_state)

@pytest.fixture
def user_and_role_page(page: Page)-> UserAndRolePage:
    return UserAndRolePage(page=page)

@pytest.fixture
def vspace_page(page: Page) -> VspacePage:
    return VspacePage(page=page)

@pytest.fixture
def desktop_page(page: Page) -> DesktopPage:
    return DesktopPage(page=page)

@pytest.fixture
def template_page(page: Page) -> TemplatePage:
    return TemplatePage(page=page)

@pytest.fixture
def ad_page(page:Page)-> ADPage:
    return ADPage(page=page)






