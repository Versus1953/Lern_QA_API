from playwright.sync_api import Page, expect
import re
import allure
import time
from tools.logger.logger import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page  
        self.name = name
        self.locator = locator
        

    def get_locator(self, nth: int = 0,timeout: int | None = None, **kwargs):
        formatted_locator = self.locator.format(**kwargs)
        locator = self.page.locator(formatted_locator).nth(nth)
        # locator.scroll_into_view_if_needed(timeout=timeout)
        return locator
        
    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        formatted_locator = self.locator.format(**kwargs)
        if formatted_locator.startswith('[') and formatted_locator.endswith(']'):
            attribute_part = formatted_locator[1:-1]  # Remove brackets
            return f"//*[@{attribute_part}][{nth + 1}]"
        else:
            return f"//*[{formatted_locator}][{nth + 1}]"
        
    
    def click(self, nth: int = 0, timeout: int | None = None, force: bool = False, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        if force:
            locator.evaluate('element => element.click()')
        else:
            locator.click(timeout=timeout)
        logger.info(f"Clicked on {self.name} (nth: {nth})")
    
                         
    def check_not_visible(self, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).not_to_be_visible(timeout=timeout)
        logger.info(f"Element {self.name} is not visible (nth: {nth})")                     
            
    def check_visible(self, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible(timeout=timeout)
        logger.info(f"Element {self.name} is visible (nth: {nth})")  
                    

    def check_have_text(self, text: str, nth: int = 0, timeout: int | None = None, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_contain_text(re.compile(text, re.IGNORECASE), timeout=timeout)

    def get_inner_text(self, nth: int = 0, **kwargs) -> str:
        """
        Fetches the visible text content of this element, mirrors what a user sees.
        """
        locator = self.get_locator(nth, **kwargs)
        text = locator.inner_text()
        clean = text.strip()
        logger.info(f"Text of {self.name}: '{clean}'")
        return clean
    
    def wait_for_selector(self, state: str = "visible", timeout: int | None = None, nth: int = 0, **kwargs):
        """
        Wait for the element to reach a specific state
        """
        formatted_locator = self.locator.format(**kwargs)
        locator = self.page.locator(formatted_locator).nth(nth)
        
        if state == "visible":
            locator.wait_for(state="visible", timeout=timeout)
        elif state == "hidden":
            locator.wait_for(state="hidden", timeout=timeout)
        elif state == "attached":
            locator.wait_for(state="attached", timeout=timeout)
        elif state == "detached":
            locator.wait_for(state="detached", timeout=timeout)
        else:
            raise ValueError(f"Invalid state: {state}")
        
        logger.info(f"Element {self.name} reached state '{state}' (nth: {nth})")
        return True
    
    def count(self, **kwargs) -> int:
        """Return the number of elements matching the locator"""
        return self.get_locator(**kwargs).count()
    
    # Wait for any elements to appear first, then wait for count
    def wait_for_count(self, expected_count: int, timeout: int = 60000, **kwargs):
        """Wait until the element count matches expected count"""
        start_time = time.time()

        first_element_timeout = min(30000, timeout)  
        while (time.time() - start_time) * 1000 < first_element_timeout:
            if self.count(**kwargs) > 0:
                break
            time.sleep(0.5)
        else:
            raise TimeoutError(f"No elements found for {self.name} within {first_element_timeout}ms")
        
        while (time.time() - start_time) * 1000 < timeout:
            current_count = self.count(**kwargs)
            print(f"DEBUG: Current count for {self.name}: {current_count}")
            if current_count == expected_count:
                logger.info(f"Element {self.name} reached expected count: {expected_count}")
                return True
            time.sleep(1)  
        
        final_count = self.count(**kwargs)
        raise TimeoutError(f"Element {self.name} count did not reach {expected_count} within {timeout}ms. Final count: {final_count}")
    
    def check_boolean_attribute(self, attribute_name: str, expected_value: bool, 
                          nth: int = 0, timeout: int | None = None, **kwargs) -> bool:
        """
        Check if a boolean attribute matches expected value.
        """
        locator = self.get_locator(nth, **kwargs)
        attribute_value = locator.get_attribute(attribute_name)
        
        if attribute_value is None:
            logger.warning(f"Attribute '{attribute_name}' not found on {self.name}")
            return False
 
        actual_bool = attribute_value== "true"
        
        if timeout:
            start_time = time.time()
            while (time.time() - start_time) * 1000 < timeout:
                attribute_value = locator.get_attribute(attribute_name)
                if attribute_value is not None:
                    actual_bool = attribute_value == "true"
                    if actual_bool == expected_value:
                        logger.info(f"Element {self.name} attribute '{attribute_name}' = {actual_bool} (expected: {expected_value})")
                        return True
                time.sleep(0.5)
            return False
        else:
            match = actual_bool == expected_value
            if match:
                logger.info(f"Element {self.name} attribute '{attribute_name}' = {actual_bool} (expected: {expected_value})")
            else:
                logger.warning(f"Element {self.name} attribute '{attribute_name}' = {actual_bool} (expected: {expected_value})")
            return match     
        
    def get_attribute(self, attribute_name: str, nth: int = 0, timeout: int | None = None, **kwargs) -> str | None:
        """
        Get the value of an attribute from the input element.
        """
        locator = self.get_locator(nth, **kwargs)
        
        try:
            attribute_value = locator.get_attribute(attribute_name)
            logger.info(f"Got attribute '{attribute_name}' = '{attribute_value}' from {self.name} (nth: {nth})")
            return attribute_value
        except Exception as e:
            logger.error(f"Failed to get attribute '{attribute_name}' from {self.name}: {e}")
            return None    
        
    
    
