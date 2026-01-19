import allure        
from playwright.sync_api import expect  
from elements.base_element import BaseElement
from tools.logger.logger import get_logger
import re

logger = get_logger("HOVER")

class Hover(BaseElement):
    def check_text_on_hover(self, expected_texts: list[str], nth: int = 0, timeout: int | None = None,
                       wait_after_hover: int = 1000, max_attempts: int = 3, **kwargs):
        """
        Check text that appears after hovering on an element
        """
        locator = self.get_locator(nth, **kwargs)
        
        for attempt in range(max_attempts):
            try:
                # Hover on the element
                locator.hover(timeout=timeout, force=True)
                self.page.wait_for_timeout(wait_after_hover)
                
                actual_text = ""
                
                # Try common tooltip selectors
                common_tooltip_selectors = [
                    "[role='tooltip']",
                    "[data-tooltip]",
                    "[title]",
                    ".tooltip",
                    ".tooltiptext",
                    ".popup",
                    ".popover",
                    "[data-popover]",
                    "[aria-describedby]"
                ]
                
                for selector in common_tooltip_selectors:
                    try:
                        tooltip_element = self.page.locator(selector)
                        if tooltip_element.count() > 0:
                            if tooltip_element.first.is_visible(timeout=1000):
                                actual_text = tooltip_element.first.inner_text(timeout=1000).strip()
                                if actual_text:
                                    logger.debug(f"Found tooltip text '{actual_text}' using selector '{selector}'")
                                    break
                    except:
                        continue
                        
                # If no tooltip found, try the hovered element itself
                if not actual_text:
                    try:
                        actual_text = locator.inner_text(timeout=timeout).strip()
                    except Exception as e:
                        if "Node is not an HTMLElement" in str(e) or "not an HTMLElement" in str(e):
                            for attr in ["aria-label", "title", "data-tooltip"]:
                                actual_text = (locator.get_attribute(attr, timeout=timeout) or "").strip()
                                if actual_text:
                                    break
                        else:
                            raise
                
                logger.debug(f"Attempt {attempt + 1}: Expected options: {expected_texts}, Actual: '{actual_text}'")
                
                if not actual_text:
                    if attempt < max_attempts - 1:
                        self.page.wait_for_timeout(500)
                        self.page.mouse.move(0, 0)
                        continue
                    
                    try:
                        all_attributes = locator.evaluate("el => el.getAttributeNames().reduce((acc, name) => ({...acc, [name]: el.getAttribute(name)}), {})", timeout=timeout)
                        logger.debug(f"Element attributes: {all_attributes}")
                    except:
                        pass
                        
                    raise AssertionError(
                        f"No text found after hovering on {self.name}. "
                        f"Expected options: {expected_texts}. "
                        f"The element might not have a tooltip."
                    )
                
                # Check if actual text matches any of the expected texts
                found_match = any(expected_text in actual_text for expected_text in expected_texts)
                
                if found_match:
                    logger.info(f"Verified text '{actual_text}' appears after hovering on {self.name}")
                    return
                else:
                    logger.warning(f"Attempt {attempt + 1}: Text mismatch. Expected: {expected_texts}, Actual: '{actual_text}'")
                    if attempt < max_attempts - 1:
                        self.page.wait_for_timeout(500)
                        self.page.mouse.move(0, 0)
                        continue
                    
                    raise AssertionError(
                        f"None of the expected texts {expected_texts} found in actual text '{actual_text}' "
                        f"after hovering on {self.name}"
                    )
                        
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_attempts - 1:
                    self.page.wait_for_timeout(500)
                    self.page.mouse.move(0, 0)
                    continue
                raise
        
        raise AssertionError(
            f"All {max_attempts} attempts failed for hovering on {self.name}. "
            f"Expected texts: {expected_texts}"
        )
