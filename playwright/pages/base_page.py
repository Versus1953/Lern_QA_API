import allure
from playwright.sync_api import Page, expect
from typing import Pattern
from tools.logger.logger import get_logger

logger = get_logger("BASE_PAGE")

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
        
    @allure.step("Navigate to URL")
    def visit(self, url: str):
        with allure.step(f"Navigating to: {url}"):
            self.page.goto(url, wait_until='networkidle')
            logger.info(f"Navigated to URL: {url}")
            

    @allure.step("Reload page")
    def reload(self):
        with allure.step("Reloading current page"):
            current_url = self.page.url
            self.page.reload(wait_until='domcontentloaded')
            logger.info(f"Reloaded page: {current_url}")
            

    @allure.step("Check current URL")
    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"Verifying URL matches pattern: {expected_url.pattern}"):
            expect(self.page).to_have_url(expected_url)
            logger.info(f"Verified URL matches pattern: {expected_url.pattern}")
