from playwright.async_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.base_element import BaseElement
from config import UiTextPatterns


class ModalComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        #Generals Components 
        
        self.page_component_modals_close_popup_button = BaseElement(page, '[data-e2e="overlapClose"]', 'Close popup button')

        #Role Assignment Modal
        self.page_component_modals_confirmation_title = BaseElement(page, '[data-e2e="confirm-title"]','Confirmation Title --Role Assignment Modal')
        self.page_component_modals_approve_button = Button(page, '[data-e2e-popup-button="approve"]', 'Approve Button')
        self.page_component_modals_cancel_button = Button(page, '[data-e2e-popup-button="cancel"]', 'Cancel Button --Role Assignment Modal')
        self.page_component_modals_roles_dropdown_label = BaseElement(page, '[for="user-roles-for-assignment"]','Roles Dropdown_label --Role Assignment Modal')
   
        
        #Password Change Modal
        self.page_component_modals_close_alert_button = BaseElement(page, '[data-e2e="close-popup"]', 'Close Popup')
        self.page_component_modals_change_password_alert_title = BaseElement(page, 'h2.confirm_title', 'Change Password Text Title')
        self.page_component_modals_password_input_label = BaseElement(page, '[for="new-user-password"]', 'Password Field Name')
        self.page_component_modals_repeat_password_input_label = BaseElement(page, '[for="repeat-new-user-password"]', 'Repeat Password Field Name')
        self.page_component_modals_repeat_password_input = Input(page, '[name="repeat-new-user-password"]', 'Repeat Password Input')
        self.page_component_modals_change_password_alert_text = BaseElement(page, '[data-e2e="popup-description"]', 'Popup Description')
        self.page_component_modals_password_input = Input(page, '[name="new-user-password"]', 'Password Input')
        
             
    def check_visible(self):
        # self.page_component_modals_confirmation_title.check_visible()
        self.page_component_modals_approve_button.check_visible()
        self.page_component_modals_cancel_button.check_visible()
        # self.page_component_modals_roles_dropdown_label.check_visible()
        
    def check_confirmation_have_text(self, message_text:str=None):
        self.page_component_modals_confirmation_title(message_text)
        
    def click_approve_button(self):
        self.page_component_modals_approve_button.click()
    
    def check_password_popup_base_components(self, include_repeat_password=True):
        self.page_component_modals_close_alert_button.check_visible()
        self.page_component_modals_password_input.check_visible()
        self.page_component_modals_password_input_label.check_visible()
        self.page_component_modals_approve_button.check_visible()
        self.page_component_modals_cancel_button.check_visible()
        
        if include_repeat_password:
            self.page_component_modals_repeat_password_input.check_visible()
            self.page_component_modals_repeat_password_input_label.check_visible()
        
    def fill_password_field(self, field_type: str, password: str, repeat_password: str = None):
        """Fill password fields based on context"""
        if field_type == "validate_existing_password":
            self.page_component_modals_password_input.fill(password)
            self.page_component_modals_password_input.check_have_value(password)
            self.page_component_modals_repeat_password_input.fill(repeat_password)
            self.page_component_modals_repeat_password_input.check_have_value(repeat_password)
        elif field_type == "validate_new_password":
            self.page_component_modals_password_input.fill(password)
            self.page_component_modals_password_input.check_have_value(password)
        
    def clear_and_send_keys_repeat_password_filed(self, password: str):
        self.page_component_modals_repeat_password_input.clear_and_send_keys(password)

    def check_visible_close_popup(self):
        self.page_component_modals_close_alert_button.check_visible()

    def check_approve_button_text(self):
        self.page_component_modals_approve_button.check_have_text(UiTextPatterns.MESSAGE_APPROVE)
        
    def check_cancel_button_text(self):
        self.page_component_modals_cancel_button.check_have_text(UiTextPatterns.MESSAGE_CANCEL)
        
    def check_confirmation_window_text(self):
        self.page_component_modals_change_password_alert_text.check_have_text(UiTextPatterns.MESSAGE_REDIRECT)
        
    def check_confirmation_window_remove_vspace_text(self):
        self.page_component_modals_confirmation_title.check_have_text(UiTextPatterns.MESSAGE_DELETE_VSPACE_CONFIRM)
        
    def check_confirmation_window_remove_desktop_text(self):
        self.page_component_modals_confirmation_title.check_have_text(UiTextPatterns.MESSAGE_DELETE_DESKTOP_CONFIRM)
        
    def check_confirmation_window_remove_template_text(self):
        self.page_component_modals_confirmation_title.check_have_text(UiTextPatterns.MESSAGE_DELETE_TEMPLATE_CONFIRM)

    def check_approve_button_enabled(self):
        self.page_component_modals_approve_button.check_enabled(timeout=30000)
        
    def check_approve_button_disabled(self):
        self.page_component_modals_approve_button.check_disabled()
        
    def check_cancel_button_enabled(self):
        self.page_component_modals_cancel_button.check_enabled()
        
    def check_cancel_button_disabled(self):
        self.page_component_modals_cancel_button.check_disabled()  
        
    def click_approve_button(self):
        self.page_component_modals_approve_button.click()
        
        
    
        
    
            
