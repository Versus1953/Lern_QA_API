
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.button import Button
from elements.input import Input
from elements.base_element import BaseElement


class TableComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        #General Table HTML Selectors
        self.page_component_actions_button = Button(page, '[data-e2e="headline-actions"]', 'Actions button')
        self.page_component_table_search_input = Input(page, '[data-e2e-search-field="search-in-sheet"]', 'Search table input')
        self.page_component_table_id_text = BaseElement(page, '[data-e2e-copy-able-content]', 'User ID text')
        self.page_component_table_multilist_in_sheet = Button(page,'[data-e2e-multilist-in-sheet]','Dots Dropdown in Table')
        self.page_component_table_remove_button = BaseElement(page,'[data-e2e-sheet-cleaner]','Remove Button in Table')
        self.page_component_table_vm_import_button = BaseElement(page,'[data-e2e="desktopImport"]','VM Import Button')
       
        #ALL VSpace Table HTML Selectors 
        
        
    #General Methods     
    def check_id_componet_presence(self):
        self.page_component_table_id_text.check_visible()

    def check_visible(self):
        self.page_component_actions_button.check_visible()
        self.page_component_actions_button.check_enabled()
        # self.page_component_table_search_input.check_visible()
        
    def click_actions_button(self):
        self.page_component_actions_button.click()
        
    def send_data_to_table_search_input(self, data: str):
        self.page_component_table_search_input.clear_and_send_keys(data)
        self.page.keyboard.press('Enter')
               
    def check_table_search_input_visible(self):
        self.page_component_table_search_input.check_visible()
        
    def click_dots_dropdown(self):
        self.page_component_table_multilist_in_sheet.click()
        
    def click_dots_dropdown_disabled(self):
        self.page_component_table_multilist_in_sheet.check_disabled()
        
    def click_remove_button(self):
        self.page_component_table_remove_button.click()
        
    def check_table_object_presence_in_table(self, object_name):
        self.page_component_table_object_name = BaseElement(
            self.page, 
            f'[data-e2e-sheet-cell-value="{object_name}"]', 
            'Object in Table'
        )
        self.page_component_table_object_name.check_visible()
        
    def check_table_object_presence_not_in_table(self, object_name):
        self.page_component_table_object_name = BaseElement(
            self.page, 
            f'[data-e2e-sheet-cell-value="{object_name}"]', 
            'Object in Table'
        )
        self.page_component_table_object_name.check_not_visible()
        
    def click_vm_import_button(self):
        self.page_component_table_vm_import_button.click()
        
            
