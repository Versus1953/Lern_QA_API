import allure        
from playwright.sync_api import expect  
from elements.base_element import BaseElement
from tools.logger.logger import get_logger

logger = get_logger("CHECKBOX")

class CheckBox(BaseElement):
    def check_is_checked(self, nth: int = 0, timeout: int | None = None, **kwargs):
        """
        Verify that the checkbox/radio button is checked.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_checked(timeout=timeout)
        logger.info(f"Verified that {self.name} is checked (nth: {nth})")

    def check_is_not_checked(self, nth: int = 0, timeout: int | None = None, **kwargs):
        """
        Verify that the checkbox/radio button is not checked.
        """
        locator = self.get_locator(nth, **kwargs)
        expect(locator).not_to_be_checked(timeout=timeout)
        logger.info(f"Verified that {self.name} is not checked (nth: {nth})")
              
