import allure
import pytest
import traceback
from contextlib import contextmanager

from tools.logger.logger import get_logger
import allure

logger = get_logger("Template")




def _capture_screenshot(page):
    """function to capture screenshot with error handling"""
    try:
        screenshot = page.page.screenshot()
        allure.attach(
            name="Page Screenshot on Failure",
            body=screenshot,
            attachment_type=allure.attachment_type.PNG
        )
        return True
    except Exception as screenshot_error:
        allure.attach(
            name="Screenshot Error",
            body=f"Failed to capture screenshot: {screenshot_error}",
            attachment_type=allure.attachment_type.TEXT
        )
        return False


@contextmanager
def handle_failure(page, capture_logs=True):
    """
    Unified context manager to capture logs and/or screenshot on test failure.
    page: The page object with log and page attributes/
    capture_logs: Whether to capture application logs (default: True)
    """
    try:
        yield
    except Exception as e:
        # Capture traceback 
        tb_str = traceback.format_exc()
        
        log_message = None
        if capture_logs:
            try:
                log_message = page.log.get_log_message()
            except Exception as log_error:
                log_message = f"Failed to retrieve log message: {log_error}"
            
            allure.attach(
                name="Application Logs",
                body=f"{log_message}",
                attachment_type=allure.attachment_type.TEXT
            )
            
        allure.attach(
            name="Exception Traceback",
            body=tb_str,
            attachment_type=allure.attachment_type.TEXT
        )
        
        _capture_screenshot(page)
        if capture_logs:
            # pytest.fail(f"Test failed due to: {e}\nLog: {log_message}")
            logger.error(f"Failed due to: {e}\nLog: {log_message}")
        else:
            # pytest.fail(f"Test failed due to: {e}")
            logger.error(f"Failed due to: {e}\nLog: {log_message}")

@contextmanager
def handle_failure_with_log_and_screenshot(page):
    """Context manager to capture logs and a screenshot on test failure"""
    with handle_failure(page, capture_logs=True):
        yield


@contextmanager
def handle_failure_with_screenshot(page):
    """Context manager to capture a screenshot on test failure"""
    with handle_failure(page, capture_logs=False):
        yield
