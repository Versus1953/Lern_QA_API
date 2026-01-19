import random
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.base_element import BaseElement
from elements.text_area import Textarea
from elements.checkbox import CheckBox
from config import UiTextPatterns
from elements.button import Button
from elements.input import Input
from elements.hover import Hover
from tools.logger.logger import get_logger

logger = get_logger ("Vspace Page")
class VspacePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        """HTML Locators"""
        
        #vSpace Create Form
        
        #Titles & Lables 
        self.page_vspace_create_button = BaseElement(page, '[data-e2e="vspaceCreate"]', 'vSpace Create Button')
        self.page_vspace_create_form_title = BaseElement(page, '[data-e2e-factory-title="VspaceFactory"]', 'vSpace Create From Title')
        self.page_vspace_create_form_vsname_input_lable= BaseElement(page, '[for="vspace-name"]', 'vSpace Create From vSpace name Input Lable')
        self.page_vspace_create_form_qpoints_usage_input_lable = BaseElement(page, '[for="vspace-usage-pool"]', 'vSpace Create From Qpoints usage pool Input Lable')
        self.page_vspace_create_form_description_input_lable = BaseElement(page, '[for="vspace-description"]', 'vSpace Create From Description Input Lable')
        
        #Inputs
        self.page_vspace_vsname_input = Input(page, '[data-e2e="vspace-name"]', 'vSpace Name Input')
        self.page_vspace_qpoints_usage_input = Input(page, '[data-e2e="vspace-usage-pool"]', 'vSpace Qpoints Usage Input')
        self.page_vspace_description_input = Input(page, '[data-e2e="vspace-description"]', 'vSpace Description Input')
        
        #Buttons
        self.page_vspace_create_vspace_button = Button(page, '[data-create-vspace-factory]', 'vSpace Create Button')
        self.page_vspace_create_vspace_cancel_button = Button(page, '[data-cancel-vspace-creation]', 'vSpace Create Button')
        self.page_component_delete_action_button =Button(page,'[data-e2e="vspaceDelete"]','Vspace Delete Button')
        
        # vSpace Details & Information
        self.page_vspace_actions_button = Button(page, '[data-e2e="vspace-actions"]','vSpace Actions Button')
        self.page_vspace_delete_vspace_button =Button(page,'[data-e2e="vspaceDelete"]','vSpace Delete Button')
        self.page_vspace_general_properties_section =BaseElement(page,
                                                                 '[data-e2e-accordion-switcher="vspace-general-properties"]',
                                                                 'vSpace General Properties Section')
        self.page_vspace_vspace_usage_pool_tooltip = Button(page,'[data-e2e="tooltip-for-vspace-usage-pool"]','vSpace Usage Pool')
        self.page_vspace_templates_section = BaseElement(page,'[data-e2e-accordion-switcher="templates-area"]','vSpace Templates Section')
        self.page_vspace_templates_assign_button =Button(page, '[data-e2e="addSnapsot"]','Assign Template Button')
        self.page_vspace_save_changes_button = Button(page, '[data-e2e="save-new-vspace-properties"]','Save New vSpace Propertis Button ')
        self.page_vspace_templates_counter= BaseElement(page,'[data-e2e-accordion-counter]','Tamplates Counter')
        self.page_vspace_quota_usage_pool_hover= Hover(page,'button[data-e2e="tooltip-for-vspace-usage-pool"] svg.svg-icon:nth-of-type(2)',
                                                       'Tamplates Hover')        
        self.page_vspace_created_section =BaseElement(page,'[data-e2e-pair-content="vspace-created"]','vSpace Create Section')
        self.page_vspace_modified_section =BaseElement(page,'[data-e2e-pair-content="vspace-modified"]','vSpace Modified Section')
        self.page_vspace_creator_username_section =BaseElement(page,'[data-e2e-pair-content="vspace-creator-username"]','vSpace Creator Username Section')
        self.page_vspace_creator_provider =BaseElement(page,'[data-e2e-pair-content="vspace-creator-provider"]','vSpace Creator Provider Section')
        self.page_vspace_qpoint_current_section =BaseElement(page,'[data-e2e-pair-content="vspace-qpoints-current"]','vSpace Qpoints Current Section')
        self.page_vspace_qpoints_usage_current =BaseElement(page,'[data-e2e-pair-content="vspace-qpoints-current"]','Qpoints usage current Section')
        self.page_vspace_name_link = BaseElement(page, '[href="#/vdi/vspace/detail/{vspace}"]', 'vSpace name link')
        self.page_vspace_template_assign_invspace_button =Button(page,'[data-e2e="addTemplate"]','Template Assign Button')
        self.page_vspace_template_assign_confirm_button =Button(page,'[class="templates-manager__send btn btn_secondary btn_with_preloader"]','Template Assign Confirm Button')
        self.page_vspace_template_assign_cancel_button =Button(page,'[class="templates-manager__cancel btn btn_primary"]','Template Assign Cancel Button')
        self.page_vspace_template_absence_message_text = BaseElement(page,'[data-e2e="noAssignedTemplatesWarning"]','Template Absence Text')
        self.page_vspace_desktop_awaiting_message_text = BaseElement(page,'[data-e2e="waitingForDesktops"]','desktop awaiting Text')
        #Template section
        self.page_vspace_template_add_button =Button(page,'[data-e2e="assign-template"]','Template Add Button')
        self.page_vspace_template_assign_button =Button(page,'[data-e2e="addSnapsot"]','Template Assign Button')
        self.page_vspace_template_choose_menu =BaseElement(page,'[data-e2e="template-for-assignment"]','Template Choose Menu')
        self.page_vspace_template_search_filed =Textarea(page,'[data-e2e-search-field="dropdown-search"]','Template Search Field')
        self.page_user_and_role_templatemenu_selectmenu = Button(page, '[data-e2e-selectmenu-option]', 'Template selectmenu-option')
        
        self.page_user_and_role_templatemenu_selectmenu = Button(page, '[data-e2e-selectmenu-option]', 'Template selectmenu-option')
        
        
        #vspace types 
        #Deploy type
        self.page_vspace_deploy_type_dropdown = Button(page, '[data-e2e="vspace-factory-deploy-type"]', 'Deploy Type Menu')
        self.page_vspace_deploy_type_automated = Button(page, '//*[@data-e2e-selectmenu-option and normalize-space(.)="Automated"]', 'Deploy Type AUTOMATED')
        self.page_vspace_deploy_type_manual = Button(page, '//*[@data-e2e-selectmenu-option and normalize-space(.)="Manual"]', 'Deploy Type MANUAL')
        
        #Provision type
        self.page_vspace_provision_type_dropdown = Button(page, '[data-e2e="vspace-factory-provision-type"]', 'Provision Type Menu')
        self.page_vspace_provision_type_persistent = Button(page, '//*[@data-e2e-selectmenu-option and normalize-space(.)="Persistent"]', 'Provision Type Persistent')
        self.page_vspace_provision_type_floating = Button(page, '//*[@data-e2e-selectmenu-option and normalize-space(.)="Floating"]', 'Provision Type Floating')
        self.page_vspace_standby_count = Input(page, '[data-e2e="vspace-factory-standby-count"]', 'Standby Count')
        
        #Session end policies
        self.page_vspace_logoff_dropdown = Button(page, '[data-e2e="vspace-factory-logoff"]', 'Logoff Dropdown')
        self.page_vspace_logoff_none = Button(page, '[data-e2e-selectmenu-option and normalize-space(.)="None"]', 'Logoff Dropdown --None Type')
        self.page_vspace_logoff_shutdown = Button(page, '[data-e2e-selectmenu-option and normalize-space(.)="Shutdown"]', 'Logoff Dropdown --Shutdown Type')
        self.page_vspace_inactive_timeout_field = Input(page, '[data-e2e="vspace-inactive-timeout"]', 'Inactive Tiemout')
        
        #Import data
        self.page_vspace_import_desktop_menu_field = Input(page, '[data-e2e="vspace-as-import-area"]', 'Import Area Field')
        
        #Connect
        self.page_vspace_connect_button =Button(page, '[data-e2e="vspaceConnect"]','Vspace Connect Button')
        

            
    #Methods    
    
    #Create Form Methods 
    
    
    def check_visible(self):
        self.page_vspace_create_form_title.check_visible()
        self.page_vspace_create_form_vsname_input_lable.check_visible()
        # self.page_vspace_create_form_qpoints_usage_input_lable.check_visible()
        self.page_vspace_create_form_description_input_lable.check_visible()
        
        self.page_vspace_vsname_input.check_visible()
        # self.page_vspace_qpoints_usage_input.check_visible()
        self.page_vspace_description_input.check_visible()
        
        self.page_vspace_create_vspace_button.check_visible()
        self.page_vspace_create_vspace_cancel_button.check_visible()
        
        
    def click_create_vspace_form_button(self):
        self.page_vspace_create_button.click()
        
    def click_delete_vspace_button_in_general_table(self):
        self.page_component_delete_action_button.click()
  
    def send_data_to_vspace_name_input(self,name:str):
        self.page_vspace_vsname_input.fill(name)
        
    def send_data_to_vspace_qpoints_usage_input(self,name: str):
        self.page_vspace_qpoints_usage_input.send_keys_character_by_character(name)
        
    def send_data_to_description_input(self,name: str):
        self.page_vspace_description_input.fill(name)
        
    def check_create_vspace_button_disabled(self):
        self.page_vspace_create_vspace_button.check_disabled()
        
    def check_cancel_create_vspace_button_disabled(self):
        self.page_vspace_create_vspace_cancel_button.check_disabled()
        
    def check_create_vspace_button_enabled(self):
        self.page_vspace_create_vspace_button.check_enabled()
        
    def check_cancel_create_vspace_button_enabled(self):
        self.page_vspace_create_vspace_cancel_button.check_enabled()
        
    def click_create_vspace_button(self):
        self.page_vspace_create_vspace_button.click()
        
    def click_create_vspacel_cancel_button(self):
        self.page_vspace_create_vspace_cancel_button.click()
    
    #vSpace types methods    
    def choose_vspace_type(self, vspace_type: str = None, random_choice: bool = False):
        self.page_vspace_deploy_type_dropdown.click()
        
        choice_mapping = {
            "Automated": self.page_vspace_deploy_type_automated,
            "Manual": self.page_vspace_deploy_type_manual,           
        }
        
        if random_choice:
            vspace_type = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected vspace_type: {vspace_type}")
        
        selected_button = choice_mapping.get(vspace_type)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid vspace_type choice: {vspace_type}. Available options: {list(choice_mapping.keys())}")
        
        
    def choose_provision_type(self, provision_type: str = None, random_choice: bool = False):
        self.page_vspace_provision_type_dropdown.click()
        
        choice_mapping = {
            "Persistent": self.page_vspace_provision_type_persistent,
            "Floating": self.page_vspace_provision_type_floating,           
        }
        
        if random_choice:
            provision_type = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected provision_type: {provision_type}")
        
        selected_button = choice_mapping.get(provision_type)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid provision_type choice: {provision_type}. Available options: {list(choice_mapping.keys())}")
        
        
    def send_data_to_standbycount_field(self,standbycount:str):
        self.page_vspace_standby_count.send_keys_character_by_character(standbycount)
        
            
    # def choose_logoff_type(self, logoff_type: str = None, random_choice: bool = False):
    #     self.page_vspace_logoff_dropdown.click()
        
    #     choice_mapping = {
    #         "None": self.page_vspace_logoff_none,
    #         "Shutdown": self.page_vspace_logoff_shutdown,           
    #     }
        
    #     if random_choice:
    #         provision_type = random.choice(list(choice_mapping.keys()))
    #         logger.info(f"Randomly selected logoff_type: {provision_type}")
        
    #     selected_button = choice_mapping.get(provision_type)
        
    #     if selected_button:
    #         selected_button.check_visible()
    #         selected_button.click()
    #     else:
    #         raise ValueError(f"Invalid logoff_type choice: {provision_type}. Available options: {list(choice_mapping.keys())}")    
        
    def send_data_to_inactivetimeout_field(self,standbycount:str):
        self.page_vspace_standby_count.send_keys_character_by_character(standbycount)            

    
    # vSpace Details & Information Section Methods

    def check_detail_page_vspace_components_presence(self):
        self.page_vspace_actions_button.check_visible()
        self.page_vspace_actions_button.check_enabled()
        self.page_vspace_general_properties_section.check_visible()
        self.page_vspace_vspace_usage_pool_tooltip.check_visible()
        self.page_vspace_templates_section.check_visible()
        self.page_vspace_save_changes_button.check_visible()
        self.page_vspace_save_changes_button.check_disabled()
        # self.page_vspace_templates_counter.check_not_visible()
        
    def check_counter_hover_presence(self):
        self.page_vspace_quota_usage_pool_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.QUOTA_USAGE_HOVER_TEXT)
        
    def check_vspace_name_text(self,name:str):
        self.page_vspace_vsname_input.check_have_value(name)
        
    def check_vspace_quota_usage_pool_quantity_text(self,usage_pool_quantity:str):
        self.page_vspace_qpoints_usage_input.check_have_value(usage_pool_quantity)
        
    def check_vspace_description_text(self,description_text:str):
        self.page_vspace_description_input.check_have_value(description_text)
        
    def click_vspace_in_table(self, vspace_name: str):
        vspace_link = self.page_vspace_name_link.get_locator(vspace_name=vspace_name)
        vspace_link.click(force=True)
                
    def check_created_section_text_pattern(self,date_time_pattern:str):
        self.page_vspace_created_section.check_have_text(date_time_pattern)
        
    def check_modified_section_text_pattern(self,date_time_pattern:str):
        self.page_vspace_modified_section.check_have_text(date_time_pattern)
        
    def check_creator_provider_text(self,provider:str):
        self.page_vspace_creator_provider.check_have_text(provider)
        
    def check_creator_username_text(self,creator_username:str):
        self.page_vspace_creator_username_section.check_have_text(creator_username)
        
    def check_qpoint_current_quantity(self,qpoint_current:str):
        self.page_vspace_qpoint_current_section.check_have_text(qpoint_current)
        
    def check_qpoints_usage_current(self,qpoints_usage_current:str):
        self.page_vspace_qpoints_usage_current.check_have_text(qpoints_usage_current)
        
    def click_vpace_action_button(self):
        self.page_vspace_actions_button.click()
    
    def click_delete_vspace_button(self):
        self.page_vspace_delete_vspace_button.click()
        
    def assert_vspace_not_in_table(self):
        self.page_vspace_name_link.check_not_visible()
        
    def check_template_to_assign(self,template_id):
        self.page_vspace_template_id= CheckBox(self.page,
            f"//*[@data-e2e='sheetCheckbox-{template_id}']",
            f"Template Checkbox {template_id}")
        self.page_vspace_template_id.click()
        self.page_vspace_template_id.check_is_checked()
        
    def check_template_not_checked(self,template_id):
        self.page_vspace_template_id= CheckBox(self.page,
            f"//*[@data-e2e='sheetCheckbox-{template_id}']",
            f"Template Checkbox {template_id}")
        self.page_vspace_template_id.check_is_not_checked()
        
  
    
        
   #Template Section 
   
    def click_template_assign_button(self):
       self.page_vspace_template_assign_button.click()
              
    def check_template_create_template_enabled(self):
        self.page_vspace_template_add_button.check_enabled()
        
    def click_template_create_template(self):
        self.page_vspace_template_add_button.click()
        
    def click_choose_template_menu(self):
        self.page_vspace_template_choose_menu.click()
        
    def send_data_to_search_template_filed(self,template_name):
        self.page_vspace_template_search_filed.check_visible()
        self.page_vspace_template_search_filed.send_keys(template_name)
        
    def choose_out_template(self,template_name):
        self.page_vspace_template_search_filed= BaseElement(self.page,
            f"//*[@data-e2e-selectmenu-option and normalize-space(.)='{template_name}']")
        
        self.page_vspace_template_search_filed.click()
        
        
    #Complete Workflows 
    # def assign_template_to_vspace(self,template_name:str):
    #     self.click_template_assign_button()
    #     self.check_template_create_template_enabled()
    #     self.click_choose_template_menu()
    #     self.choose_out_template(template_name)
    #     self.click_template_create_template()
        
        
    #Complete Workflows  --Old
    def create_vspace(self,vspace_name:str,
                      qpoints_usage: str=None,
                      description:str=None):
        """
        Complete vspace-createing workflow 
        """
        self.click_create_vspace_form_button()
        self.check_visible()
        self.check_create_vspace_button_disabled()
        self.check_cancel_create_vspace_button_enabled()
        self.send_data_to_vspace_name_input(vspace_name)
        self.send_data_to_vspace_qpoints_usage_input(qpoints_usage)
        self.send_data_to_description_input(description)        
        self.check_create_vspace_button_enabled()
        self.check_cancel_create_vspace_button_enabled()
        self.click_create_vspace_button()
        
    #Complete Workflows  --Different vsapce types  
    def create_vspace(self, vspace_name: str,
                  qpoints_usage: str = None,
                  description: str = None,
                  deploy_type: str = None,
                  provision_type: str = None,
                  standby_count: str = None,
                #   logoff_type: str = None,
                  inactive_timeout: str = None):
        """
        Complete vspace-creating workflow with deploy type handling
        """
        self.click_create_vspace_form_button()
        self.check_visible()
        self.check_create_vspace_button_disabled()
        self.check_cancel_create_vspace_button_enabled()
        self.send_data_to_vspace_name_input(vspace_name)
        self.send_data_to_vspace_qpoints_usage_input(qpoints_usage)
        self.send_data_to_description_input(description)
        
        # deploy type selection
        if deploy_type:
            self.choose_vspace_type(deploy_type)
            
            # Automated deploy type
            if deploy_type == "Automated":
                if not provision_type:
                    raise ValueError("Provision type is required for Automated deploy type")
                
                self.choose_provision_type(provision_type)
               
                # Automated Persistent type
                if provision_type == "Persistent":
                    # Not available: Standby Count
                    # Available: Logoff and Inactive Timeout
                    # if standby_count:
                    #     logger.info("Ignoring Standby Count for Automated Persistent type")
                    
                    # if logoff_type:
                    #     self.choose_logoff_type(logoff_type)
            
                    if inactive_timeout:
                        self.send_data_to_inactivetimeout_field(inactive_timeout)
                
                # Automated Floating type  
                elif provision_type == "Floating":
                    # Available: Standby Count and Inactive Timeout
                    # Logoff not required to fill in
                    if standby_count:
                        self.send_data_to_standbycount_field(standby_count)
                    
                    if inactive_timeout:
                        self.send_data_to_inactivetimeout_field(inactive_timeout)
                    
                    # if logoff_type:
                    #     logger.info("Logoff is not required for Automated Floating type - ignoring")
            
            # Manual deploy type
            elif deploy_type == "Manual":
                # Not available: Provision Type, Standby Count
                # Available: Logoff and Inactive Timeout
                if provision_type:
                    logger.info("Ignoring Provision type for Manual deploy type")
                
                if standby_count:
                    logger.info("Ignoring Standby for Manual deploy type")
                
                # if logoff_type:
                #     self.choose_logoff_type(logoff_type)
                
                if inactive_timeout:
                    self.send_data_to_inactivetimeout_field(inactive_timeout)
        
        self.check_create_vspace_button_enabled()
        self.check_cancel_create_vspace_button_enabled()
        self.click_create_vspace_button()
    
     #vSpace types methods    
    def choose_vspace_type(self, vspace_type: str = None, random_choice: bool = False):
        self.page_vspace_deploy_type_dropdown.click()
        
        choice_mapping = {
            "Automated": self.page_vspace_deploy_type_automated,
            "Manual": self.page_vspace_deploy_type_manual,           
        }
        
        if random_choice:
            vspace_type = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected vspace_type: {vspace_type}")
        
        selected_button = choice_mapping.get(vspace_type)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid vspace_type choice: {vspace_type}. Available options: {list(choice_mapping.keys())}")
        
        
    def choose_provision_type(self, provision_type: str = None, random_choice: bool = False):
        self.page_vspace_provision_type_dropdown.click()
        
        choice_mapping = {
            "Persistent": self.page_vspace_provision_type_persistent,
            "Floating": self.page_vspace_provision_type_floating,           
        }
        
        if random_choice:
            provision_type = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected provision_type: {provision_type}")
        
        selected_button = choice_mapping.get(provision_type)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid provision_type choice: {provision_type}. Available options: {list(choice_mapping.keys())}")
        
        
    def send_data_to_standbycount_field(self,standbycount:str):
        self.page_vspace_standby_count.send_keys_character_by_character(standbycount)
        
            
    # def choose_logoff_type(self, logoff_type: str = None, random_choice: bool = False):
    #     self.page_vspace_logoff_dropdown.click()
        
    #     choice_mapping = {
    #         "None": self.page_vspace_logoff_none,
    #         "Shutdown": self.page_vspace_logoff_shutdown,           
    #     }
        
    #     if random_choice:
    #         provision_type = random.choice(list(choice_mapping.keys()))
    #         logger.info(f"Randomly selected logoff_type: {provision_type}")
        
    #     selected_button = choice_mapping.get(provision_type)
        
    #     if selected_button:
    #         selected_button.check_visible()
    #         selected_button.click()
    #     else:
    #         raise ValueError(f"Invalid logoff_type choice: {provision_type}. Available options: {list(choice_mapping.keys())}")    
        
    def send_data_to_inactivetimeout_field(self,inactive_timeout:str):
        self.page_vspace_inactive_timeout_field.send_keys_character_by_character(inactive_timeout) 
        
    #Import Desktop Data
    def import_desktop_to_vspace(self,vspace_name):
        self.page_vspace_import_desktop_menu_field.click()
        self.page_vspace_vsapce_name= BaseElement(self.page,
            f'//*[@data-e2e-selectmenu-option and normalize-space(.)="{vspace_name}"]',
            f"Vspace Name {vspace_name}")
        self.page_vspace_vsapce_name.click()
        
    #Connect      
    def check_connect_vspace_button_enabled(self):
      self.page_vspace_connect_button.check_visible()
      self.page_vspace_connect_button.check_enabled()
      
    def check_connect_vspace_button_disabled(self):
      self.page_vspace_connect_button.check_visible()
      self.page_vspace_connect_button.check_disabled()
      
    def click_connect_vspace_button(self):
      self.page_vspace_connect_button.check_visible()
      self.page_vspace_connect_button.click()
        
        
    
     
        
        
        
        
        
      
        
        
        
