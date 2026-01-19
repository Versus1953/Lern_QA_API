from playwright.async_api import Page, expect
from typing import Pattern
from pages.base_page import BasePage
from elements.base_element import BaseElement

class SidebarListItemComponent(BaseElement):
    def __init__(self, page: Page, identifier: str):
        self.identifier = identifier
        locator = f'[data-e2e-branch-link="{identifier}"]'
        name = f'Tree Link Dropdown: {identifier}'
        super().__init__(page, locator, name)
        
        self.base_page = BasePage(page)
        self.icon = BaseElement(page, locator, name)
        
    def navigate_url(self, expected_url: Pattern[str]):
        self.click()  
        self.base_page.check_current_url(expected_url)


