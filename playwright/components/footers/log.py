import allure 
import datetime
import time
from playwright.async_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.base_element import BaseElement
from tools.logger.logger import get_logger


logger = get_logger("LogComponent")


class LogComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_component_log_weblog_button = BaseElement(page, '[data-e2e="log-toggler"]', 'Log Button')
        self.page_component_log_request_id_text = BaseElement(page, '[data-e2e-sheet-column-id="logs-guid"]', 'Request ID')
        self.page_component_log_method_text = BaseElement(page, '[data-e2e-sheet-column-id="logs-method"]', 'Method')
        self.attachment_counter = 0  # Counter for unique attachment names

    def get_log_message(self, context: str = "log") -> str:
        """Get log message with unique attachment name"""
        try:
      
            unique_id =  f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
            
            # Check if log button is visible
            self.page_component_log_weblog_button.check_visible()
            self.page_component_log_weblog_button.click()
            self.page_component_log_request_id_text.check_visible()
            self.page_component_log_method_text.check_visible()
            request_id_text = self.page_component_log_request_id_text.get_inner_text()
            method_text = self.page_component_log_method_text.get_inner_text()
            time.sleep(1)
            
            log_message = f"Request ID: {request_id_text}, Method: {method_text}"
            logger.info(log_message)
            
            allure.attach(
                log_message,
                name=f"log_data_{unique_id}",
                attachment_type=allure.attachment_type.TEXT
            )
            
            self.page_component_log_weblog_button.click()
            return log_message
            
        except Exception as e:
            error_message = f"Logs not available due to error: {e}"
            logger.error(error_message)
            
          
            allure.attach(
                error_message,
                name=f"log_error_{unique_id}",
                attachment_type=allure.attachment_type.TEXT
            )
            
            return error_message
