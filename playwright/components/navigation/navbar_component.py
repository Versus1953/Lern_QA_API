from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.base_element import BaseElement
from config import UiTextPatterns as pattern
from elements.input import Input
from tools.logger.logger import get_logger
logger = get_logger("UserManagement")


class NavbarComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_component = Button(page, '[data-e2e="menu-value"]', 'Language Menu Dropdown')
        self.refresh_button = Button(page, '[data-e2e="refresh-page-content"]', 'Refresh Loader')
        self.logout_button = Button(page, '[data-e2e-logout]', 'Logout Button') 
        self.password_popup = Button(page, '//*[@data-e2e="open-password-popup"]', 'Password Popup Button')
        #2fa
        self.twofa_button = Button(page,'[data-e2e-2fa-state]','2fa Button')
        self.twofa_title =Input(page,'[class="twofa__title"]','twofa Title')
        self.twofa_close_popup =Button(page,'[data-e2e="close-popup"]','twofa close Popup')
        self.twofa_email_label =BaseElement(page,'[for="twofa-email"]','twofa email Label')
        self.twofa_email_input =Input(page,'[data-e2e="twofa-email"]','twofa email Input')
        self.twofa_send_button =Button(page,'[class="btn btn_primary twofa__send"]','Send Button')
        self.twofa_code_label =BaseElement(page,'[for="twofa-code"]','twofa code Label')
        self.twofa_code_input =Input(page,'[data-e2e="twofa-code"]','twofa code Input')
        self.twofa_code_sent_confirmation =BaseElement(page,'[class="twofa__message text1"]','twofa code sent Confirmation')
        self.twofa_message_error = BaseElement(page,'[class="twofa__message text1 twofa__message_error"]','twofa error Message')
        self.twofa_invalid_email_error =BaseElement(page,'[data-e2e-error-code="emailInvalidFormat"]','Invalid Email Error Message')
        
    def check_visible(self):
        self.menu_component.check_visible()
        
    def check_visible_component(self):
        self.menu_component.check_visible()
    
    def click_menu_component(self):
        self.menu_component.click()
        
    def click_refresh_button(self):
        self.refresh_button.click()
        
    def click_logout_button(self):
        self.logout_button.click()
        
    def click_password_popup(self):
        self.password_popup.click()
        
    #2fa methods
    def check_twofa_visible(self):
        self.twofa_button.check_visible()
        
    def check_twofa_enabled(self):
        self.twofa_button.check_boolean_attribute(attribute_name='data-e2e-2fa-state',
                                                  expected_value='true')
        
    def check_twofa_disabled(self):
        self.twofa_button.check_boolean_attribute(attribute_name='data-e2e-2fa-state',
                                                  expected_value='false')
        
    def check_twofa_click(self):
        self.twofa_button.click()
        
    def check_twofa_title_enable_text(self):
        self.twofa_title.check_have_text(pattern.TWOAF_ENABLE_TITILE)
        
    def check_twofa_title_disabled_text(self):
        self.twofa_title.check_have_text(pattern.TWOAF_DISABLED_TITILE)
        
    def check_twofa_invalid_email_text(self):
        self.twofa_title.check_have_text(pattern.TWOAF_INVALID_EMAIL_TEXT)
        
    def check_attemts_counts(self,attempt_count):
        self.twofa_message_error = BaseElement(self.page,
                                               '[class="twofa__message text1 twofa__message_error"]',
                                               'twofa error Message')
        self.twofa_message_error.check_have_text(f'Неверный код. Осталось попыток: {attempt_count}|Code is wrong. Attempts left: {attempt_count}')
        
        
    def check_invalid_email_message_error(self):
        self.twofa_invalid_email_error.check_have_text(text=pattern.TWOAF_INVALID_EMAIL_TEXT)
        
    def check_close_popup_visible(self):
        self.twofa_close_popup.check_visible()
        
    def check_close_popup_visible(self):
        self.twofa_close_popup.check_enabled()
        
    def check_close_popup_visible(self):
        self.twofa_close_popup.click()
        
    def check_email_label_visible(self):
        self.twofa_email_label.check_visible()
        
    def check_send_button_enabled(self):
        self.twofa_send_button.check_enabled()
        
    def check_send_button_disabled(self):
        self.twofa_send_button.check_disabled()
        
    def check_send_button_click(self):
        self.twofa_send_button.click()
        
    def check_code_label_visible(self):
        self.twofa_code_label.check_visible()
        
    def check_email_input_empty(self):
        self.twofa_email_input.check_empty()
        
    def check_code_input_empty(self):
        self.twofa_code_input.check_empty()
        
    def send_data_to_email_input(self,email:str):
        self.twofa_email_input.send_keys_character_by_character(email)
        
    def check_email_input_has_email(self, email: str):
        value = self.twofa_email_input.get_attribute(attribute_name='data-e2e="twofa-email"')
        if value == email:
            logger.info(f'Email field has value: {email}')
            return True
        else:
            logger.error(f'Email field has value: {value}, expected: {email}')
            return False
        
    def check_code_confirmation_sent_text_visible(self):
        self.twofa_code_sent_confirmation.check_visible()
        
    def send_data_to_code_input(self,code:str):
        self.twofa_code_input.send_keys_character_by_character(code)
        
    def check_code_input_invisible(self):
        self.twofa_code_input.check_not_visible()
                    
    def check_code_input_has_code(self, code: str):
        value = self.twofa_code_input.get_attribute()
        if value == code:
            logger.info(f'Code field has value: {code}')
            return True
        else:
            logger.error(f'Code field has value: {value}, expected: {code}')
            return False
        
    
        
