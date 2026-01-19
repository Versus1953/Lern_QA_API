import allure        
from playwright.sync_api import expect  
from elements.base_element import BaseElement
from tools.logger.logger import get_logger
import re

logger = get_logger("BUTTON")

class Button(BaseElement):
    def check_enabled(self, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_enabled(timeout=timeout)
        logger.info(f"Button '{self.name}' is enabled (nth: {nth})")

        
    def check_disabled(self, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_disabled(timeout=timeout)
        logger.info(f"Button '{self.name}' is disabled (nth: {nth})")
            

    def check_disabled_by_class(self, nth: int = 0, timeout: int | None = None, **kwargs) -> bool:
        """Check if element is disabled specifically by class"""
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_class(re.compile(r".*dropdown-option_disabled.*"), timeout=timeout)
        logger.info(f"Element {self.name} has disabled class")
            

    def check_disabled_by_data_attribute(self, nth: int = 0, timeout: int | None = None, **kwargs) -> bool:
        """Check if element is disabled specifically by data-e2e-disabled attribute"""
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_attribute("data-e2e-disabled", "true", timeout=timeout)
        logger.info(f"Element {self.name} has data-e2e-disabled='true'")
              
