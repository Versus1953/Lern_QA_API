from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from elements.base_element import BaseElement
from componets.modals.alerts import AlertComponent
from componets.modals.modals import ModalComponent
from componets.navigation.navbar_component import NavbarComponent
from componets.navigation.sidebar_component import SideBarComponent
from componets.tables.tables import TableComponent
from componets.footers.log import LogComponent



class VdiOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        
        """Page Components Implementation"""
        
        """
        ALL Page Components have to be implemented on this Page -VdiOverviewPage
        """
    
        #Navigation Components
        self.navbar = NavbarComponent(page)
        self.sidebar = SideBarComponent(page)
        
        #Footer Components
        self.log = LogComponent(page) 

        #Modal Components
        self.alerts = AlertComponent(page)  
        self.modals = ModalComponent(page)
        
        #Tables
        self.tables = TableComponent(page)
        
        
        
        """HTML Locators"""
    
        self.page_vdioverviewpage_quota_cpu_ghz_ratio = BaseElement(page, '[data-e2e="quota.cpu_ghz.ratio"]', 'quota_cpu_ghz_ratio')
        self.page_vdioverviewpage_quota_ram_gb_ratiop = BaseElement(page, '[data-e2e="quota.ram_gb.ratio"]', 'quota_ram_gb_ratio')
        self.page_vdioverviewpage_quota_storage_gb_ratio = BaseElement(page, '[data-e2e="quota.storage_gb.ratio"]', 'quota.storage_gb_ratio')
      
        
    def check_visible_vdi_quota_setting_components(self):
        self.page_vdioverviewpage_quota_cpu_ghz_ratio.check_visible()
        self.page_vdioverviewpage_quota_ram_gb_ratiop.check_visible()
        self.page_vdioverviewpage_quota_storage_gb_ratio.check_visible()
        
    
        
