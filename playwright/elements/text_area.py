import allure
from playwright.sync_api import expect
from tools.logger.logger import get_logger
from elements.base_element import BaseElement

logger = get_logger("TEXTAREA")

class Textarea(BaseElement):
    
    def get_locator(self, nth: int = 0, **kwargs):
        parent_locator = super().get_locator(nth, **kwargs)
        return parent_locator.locator('textarea').first
    
    def fill(self, value: str, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value, timeout=timeout)
        logger.info(f"Filled {self.name} with text (length: {len(value)} chars) (nth: {nth})")
            
    def check_have_value(self, value: str, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value, timeout=timeout)
        logger.info(f"Verified {self.name} has expected value (length: {len(value)} chars) (nth: {nth})")
      
    def clear_and_send_keys(self, value: str, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Clearing and setting value (length: {len(value)} chars) for {self.name} (nth: {nth})"):
            locator.clear(timeout=timeout)
            locator.fill(value, timeout=timeout)
            expect(locator).to_have_value(value, timeout=timeout)
            logger.info(f"Cleared and set value (length: {len(value)} chars) for {self.name} (nth: {nth})")
     
    def clear(self, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.clear(timeout=timeout)
        logger.info(f"Cleared {self.name} (nth: {nth})")
            
    def send_keys(self, value: str, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Sending keys (length: {len(value)} chars) to {self.name} (nth: {nth})"):
            locator.fill(value, timeout=timeout)
            expect(locator).to_have_value(value, timeout=timeout)
            logger.info(f"Sent keys (length: {len(value)} chars) to {self.name} (nth: {nth})")
            
    def get_inner_text(self, nth: int = 0, **kwargs) -> str:
        """
        Fetches the visible text content of this element, mirrors what a user sees.
        """
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Getting visible text from {self.name} (nth: {nth})"):
            text = locator.inner_text()
            clean = text.strip()
            logger.info(f"Text of {self.name}: '{clean}'")
            return clean

    def get_input_value_text(self, nth: int = 0, **kwargs) -> str:
        """
        Reads the *value* of an input-like element, exactly as set in the DOM.
        """
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f"Getting input value from {self.name} (nth: {nth})"):
            text = locator.input_value()
            logger.info(f"Got input-value from {self.name} (length: {len(text)} chars) (nth: {nth})")
            return text
