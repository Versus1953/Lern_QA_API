from playwright.async_api import Page
from pages.base_page import BasePage
from typing import Optional
from elements.base_element import BaseElement
from componets.navigation.sidebar_list_item_component import SidebarListItemComponent
from config import AuthUrlPatterns
import re 

class SideBarComponent(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        
        self.page_component_sidebar_vdi_switcher = BaseElement(page, '[data-e2e-item-id="vdiMenuPoint"]', 'ALL vSpaces Menu Point')
        self.page_component_sidebar_vspace_switcher = BaseElement(page, '[data-e2e-branch-switcher="vspace"]', 'ALL vSpaces Menu Point')
        self.page_component_sidebar_vspace_rubricators = BaseElement(page, '[data-e2e-branch-type="vspace"]', 'vSpace Rubricators')
        self.page_component_sidebar_desktop_rubricators = BaseElement(page, '[data-e2e-branch-switcher="desktop"]', 'Desktop Rubricators')
                
        self.page_component_sidebar_users_and_roles_rubricator =  SidebarListItemComponent(page,identifier="vdiUsers")
        self.page_component_sidebar_all_virtual_desktops_rubricator = SidebarListItemComponent(page,identifier="allDesktops")
        self.page_component_sidebar_all_templates_rubricator = SidebarListItemComponent(page,identifier="templates")
        self.page_component_sidebar_all_vSpaces_rubricator = SidebarListItemComponent(page,identifier="vspace")
        self.page_component_sidebar_importable_VMs = SidebarListItemComponent(page,identifier="importableVm")
        self.page_component_sidebar_AD = SidebarListItemComponent(page,identifier="activeDirectory")
        
        
        #Desktop Tree
        self.page_component_sidebar_desktop_floating_instance = BaseElement(self.page, 
                                                                            'a[data-e2e-tree-link="Floating Instance"]',
                                                                            'Desktop Floating Desktop')
    def click_vdi_main_menu(self):
        self.page_component_sidebar_vdi_switcher.click(timeout=60000)
        self.page_component_sidebar_all_vSpaces_rubricator.check_visible(timeout=60000)
            
    def click_vdi_main_menu_by_role_name(self, 
                            check_users_and_roles: Optional[bool] = True,
                            check_virtual_desktops: Optional[bool] = True,
                            check_templates: Optional[bool] = True,
                            check_vspaces: Optional[bool] = True,
                            check_AD:Optional[bool] = True,
                            check_Importable_VM:Optional[bool] = True,
                            timeout: int = 60000):
        """
        Unified VDI main menu checkup and click - conditionally verifies visible components.
        True to check, False to skip
        """
        self.page_component_sidebar_vdi_switcher.click(timeout=timeout)
        
        if check_users_and_roles:
            self.page_component_sidebar_users_and_roles_rubricator.check_visible(timeout=timeout)
        if check_virtual_desktops:
            self.page_component_sidebar_all_virtual_desktops_rubricator.check_visible(timeout=timeout)
        if check_templates:
            self.page_component_sidebar_all_templates_rubricator.check_visible(timeout=timeout)
        if check_vspaces:
            self.page_component_sidebar_all_vSpaces_rubricator.check_visible(timeout=timeout)
        if check_AD:
            self.page_component_sidebar_AD.check_visible(timeout=timeout)
        if check_Importable_VM:
            self.page_component_sidebar_importable_VMs.check_visible(timeout=timeout)
            
            
    def click_vdi_main_menu_by_role(self, role_name: Optional[str] = None, timeout: int = 30000):
        """
        VDI main menu clickup with role-specific checks
        If role_name is None use default behavior
        """
        if role_name is None:
            return self.click_vdi_main_menu_by_role_name(timeout=timeout)
        
        # Roles
        vdi_main_menu_check_VDI_Admin = ["VDI Admin"]
        vdi_main_menu_check_vSpace_Admin = ["vSpace Admin"] 
        vdi_main_menu_check_vSpace_User = ["vSpace User"]
        vdi_main_menu_check_vspace_Desktop_User = ["Desktop User"]
        
        if role_name in vdi_main_menu_check_vSpace_User:
            return self.click_vdi_main_menu_by_role_name(
                check_users_and_roles=False,
                check_virtual_desktops=False,
                check_Importable_VM=False,
                check_AD=False,
                timeout=timeout
            )
        elif role_name in vdi_main_menu_check_vspace_Desktop_User:
            return self.click_vdi_main_menu_by_role_name(
                check_users_and_roles=False,
                check_templates=False,
                check_AD=False,
                check_Importable_VM=False,
                timeout=timeout
            )                
        elif role_name in vdi_main_menu_check_vSpace_Admin:
            return self.click_vdi_main_menu_by_role_name(
                check_users_and_roles=False,
                check_Importable_VM=False,
                check_AD=False,
                timeout=timeout
            )   
        elif role_name in vdi_main_menu_check_VDI_Admin:
            return self.click_vdi_main_menu_by_role_name(
                check_Importable_VM=False,
                timeout=timeout
            )                               
        else:
            return self.click_vdi_main_menu_by_role_name(timeout=timeout)

     #Choose vSpace depends on navigation pattern
    def choose_specified_vspace_from_main_tree(
        self, 
        vspace_id: str,
        vspace_name: str,
        timeout: int = 30000
    ):
        self.page_component_sidebar_vspace_switcher.click(timeout=timeout)
        
        # Click rubricator if ID provided
        if vspace_id:
            rubricator = BaseElement(
                self.page, f'[data-e2e-item-id="{vspace_id}"]', 'vSpace Rubricator ID')
            rubricator.click(timeout=timeout)
        
        # Click the vSpace name directly
        vspace_element = BaseElement(
            self.page, f'[data-e2e-tree-link=" {vspace_name}"]', 'vSpace Name')
        vspace_element.click(timeout=timeout)
        
    #Choose vSpace with role-specific behavior
    #vspace_id: Optional rubricator ID (some roles not need it)
    def choose_specified_vspace_by_role(
        self,
        vspace_name: str,
        role_name: Optional[str] = None,
        vspace_id: Optional[str] = None,
        timeout: int = 30000
    ):
        
        roles_with_rubricator_access = ["VDI Admin", "vSpace Admin"]
        roles_without_rubricator_access = ["vSpace User", "Desktop User"]
        
        if role_name in roles_without_rubricator_access:
            # navigate directly to assigned vSpace-different navigation pattern
            return self.choose_specified_vspace_from_main_tree(
                vspace_id=None,  
                vspace_name=vspace_name,
                timeout=timeout
            )
        elif role_name in roles_with_rubricator_access:
            if not vspace_id:
                raise ValueError(f"vspace_id is required for role: {role_name}")
            
            self.page_component_sidebar_vspace_switcher.click(timeout=timeout)
            self.page_component_sidebar_vspace_rubricators.check_visible(timeout=timeout)
            
            return self.choose_specified_vspace_from_main_tree(
                vspace_id=vspace_id,
                vspace_name=vspace_name,
                timeout=timeout
            )
        else:
            return self.choose_specified_vspace_from_main_tree(
                vspace_id=vspace_id,
                vspace_name=vspace_name,
                timeout=timeout
            )
                         
    def choose_specified_desktop_from_main_tree(self, vspace_id, desktop_id):
        self.page_component_sidebar_vspace_switcher.click()
        self.page_component_sidebar_vspace_rubricators.check_visible()       
        self.page_component_sidebar_vspace_specified_rubricator_id = BaseElement(
            self.page, f'[data-e2e-item-id="{vspace_id}"]', 'vSpace Rubricator ID')
        self.page_component_sidebar_vspace_specified_rubricator_id.click()        
        self.page_component_sidebar_desktop_rubricators.click()        
        self.page_component_sidebar_desktop_id = BaseElement(
            self.page, f'[href="#/vdi/virtualDesktop/detail/{vspace_id}/{desktop_id}"]', 'Desktop ID')
        self.page_component_sidebar_desktop_id.click()        
        self.page_component_sidebar_desktop_id_detail_desktop_page = BaseElement(
            self.page, f'[data-e2e-copy-able-content]', 'Desktop Detail Page').check_visible()
        
    def open_last_desktop_container_from_main_tree(self):  
        self.page_component_sidebar_vspace_specified_rubricator_id = BaseElement(
            self.page, 'xpath=(//*[@data-e2e-item-id])[last()]', 'Last vSpace Rubricator ID')
        self.page_component_sidebar_vspace_specified_rubricator_id.click()        
        self.page_component_sidebar_desktop_rubricators.click()        
                
        self.page_component_sidebar_desktop_id_detail_desktop_page = BaseElement(
            self.page, '[data-e2e-copy-able-content]', 'Desktop Detail Page').check_visible()
        
    def open_specified_desktop_last_desktop_container_from_main_tree(self,desktop_name):  
        self.page_component_sidebar_vspace_specified_rubricator_id = BaseElement(
            self.page, 'xpath=(//*[@data-e2e-item-id])[last()]', 'Last vSpace Rubricator ID')
        self.page_component_sidebar_vspace_specified_rubricator_id.click()        
        self.page_component_sidebar_desktop_rubricators.click()        
        self.page_component_sidebar_vspace_specified_desktop_name = BaseElement(
            self.page, f'[data-e2e-tree-link="{desktop_name}"]', 'Specified Desktop') 
        self.page_component_sidebar_vspace_specified_desktop_name.click()
        self.page_component_sidebar_desktop_id_detail_desktop_page = BaseElement(
            self.page, '[data-e2e-copy-able-content]', 'Desktop Detail Page').check_visible()
        
    def check_desktop_container_empty(self):  
        # self.page_component_sidebar_vspace_specified_rubricator_id = BaseElement(
        #     self.page, 'xpath=(//*[@data-e2e-item-id])[last()]', 'Last vSpace Rubricator ID')
        # self.page_component_sidebar_vspace_specified_rubricator_id.click()        
        # self.page_component_sidebar_desktop_rubricators.click()        
                
        self.page_component_sidebar_desktop_id_detail_desktop_page = BaseElement(
            self.page, '[data-e2e-copy-able-content]', 'Desktop Detail Page').check_not_visible()
                
        
    def click_menu_icon_users_and_roles(self):
        self.page_component_sidebar_users_and_roles_rubricator.navigate_url(re.compile(AuthUrlPatterns.VDI_USER_LIST))
        
    def click_all_virtual_desktops(self):
        self.page_component_sidebar_all_virtual_desktops_rubricator.navigate_url(re.compile(AuthUrlPatterns.VDI_DESKTOP_LIST))
        
    def click_menu_icon_templates(self):
        self.page_component_sidebar_all_templates_rubricator.navigate_url(re.compile(AuthUrlPatterns.VDI_TEMPLATES_LIST))
        
    def click_all_vSpaces(self):
        self.page_component_sidebar_all_vSpaces_rubricator.navigate_url(re.compile(AuthUrlPatterns.VDI_ALL_VSPACES_LIST))
        
    def click_importable_VMs(self):
        self.page_component_sidebar_importable_VMs.navigate_url(re.compile(AuthUrlPatterns.VDI_IMPORTABLE_VMS))
        
    def click_Active_Directory(self):
        self.page_component_sidebar_AD.navigate_url(re.compile(AuthUrlPatterns.VDI_AD))
        
        
    
        
        
   

