from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from typing import Pattern
from componets.modals.alerts import AlertComponent
 


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        """HTML Locators"""
     
        self.page_login_username_input = Input(page, '[data-e2e="username"]', 'Username input')
        self.page_login_password_input = Input(page, '[data-e2e="password"]', 'Password Input')
        self.page_login_submit_button = Button(page, '[type="submit"]', 'Submit Button')
        self.page_login_AD_tab =Button(page,'[data-e2e="activeDirectory"]','AD user Tab')
        self.page_login_local =Button(page,'[data-e2e="localUser"]','Local User Tab')
                
    def login(self, username: str, password: str, use_ad: bool = False):
        if use_ad:
            self.page_login_AD_tab.click()
        else:
            self.page_login_local.click()    
        self.page_login_username_input.fill(username)
        self.page_login_username_input.check_have_value(username)
        self.page_login_password_input.fill(password)
        self.page_login_password_input.check_have_value(password)
        self.page_login_submit_button.click()
 
    def check_login_form_componets(self):
        self.page_login_username_input.check_visible()
        self.page_login_password_input.check_visible()
        self.page_login_submit_button.check_visible()

