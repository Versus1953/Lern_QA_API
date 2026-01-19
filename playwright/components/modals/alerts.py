from playwright.async_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.base_element import BaseElement


class AlertComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_component_alerts_success_alert = BaseElement(page, '[data-e2e-message-tone="success"]','Success Message')
        self.page_component_alerts_alert_close_button = BaseElement(page, '[data-e2e="messenger-close"]','Alert Close Button')
        self.page_components_alerts_warning_message_alert=BaseElement(page,'[data-e2e-message-tone="warning"]','Warning Message')
  
    def check_success_alert_visible(self):
        self.page_component_alerts_success_alert.check_visible(timeout=60000)
        self.page_component_alerts_alert_close_button.click()
        
    def check_warning_alert_visible(self):
        self.page_components_alerts_warning_message_alert.check_visible(timeout=60000)
        self.page_component_alerts_alert_close_button.click()
        
        
    def check_success_message_have_text(self, message_text:str=None):
        self.page_component_alerts_success_alert.check_have_text(message_text)
            
