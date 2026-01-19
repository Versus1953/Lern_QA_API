import random
import time
from playwright.sync_api import Page, expect
from config import UiTextPatterns
from pages.base_page import BasePage
from elements.base_element import BaseElement
from config import UiTextPatterns
from config import VariablesNames
from elements.button import Button
from elements.input import Input
from elements.hover import Hover
from tools.logger.logger import get_logger
from functools import wraps

logger = get_logger ("Template Page")

Q7 =VariablesNames.Q7
Q9 =VariablesNames.Q9
class TemplatePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        """HTML Locators"""
        
        #Template Create Form
        
        #Titles & Lables 
        #General Block
        self.page_template_create_form_required_fields_title =BaseElement(page, '[data-e2e-factory-warn-of-required-fields]', 'Required Fields Title')
        self.page_template_name_input_lable = BaseElement(page,'[for="template-name"]','Template Name Input Label')
        self.page_template_cluster_name_input_lable =BaseElement(page,'[for="template-name"]','Cluster Name Input Lable')
        self.page_template_os_type_profile_input_lable = BaseElement(page,'[for="os-profile"]','OS Profile Input Lable')
        self.page_template_pool_input_lable =BaseElement(page,'[for="vm-pool"]','Pool Input Lable')
        self.page_template_cpu_input_lable =BaseElement(page,'[for="vm-cpus"]','CPU Input Lable')
        self.page_template_ram_input_lable =BaseElement(page,'[for="vm-ram"]','RAM Input Lable')
        self.page_template_vcpu_class_input_lable =BaseElement(page,'[for="vm-vcpu-class"]','vCPU class')
        self.page_template_boot_media_input_lable =BaseElement(page,'[for="vm-boot-media"]','Boot media Input Lable')
        self.page_template_cpu_hover =Hover(page,'[data-e2e="tooltip-for-vm-cpus"]','Template CPU Input Hover')
        self.page_template_ram_hover = Hover(page,'[data-e2e="tooltip-for-vm-ram"]','Template RAM Input Hover')
 
        
        #Cluster Data
        self.page_template_cluster_q7_button =Button(page,f'[data-e2e="{Q7}"]','Q7 Cluster Button')
        self.page_template_cluster_q9_button =Button(page,f'[data-e2e="{Q9}"]','Q9 Cluster Button')
        self.page_template_cluster_autochoice_button =Button(page,'[data-e2e="clusterAutoChoice"]','Auto-choice Cluster Button')
        
        self.page_template_cluster_CPU_min_used_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(CPU) min used/total ratio" or normalize-space(.)="(CPU) минимальное отношение used/total")]',
            '(CPU) min used/total ratio Cluster Choice Button')

        self.page_template_cluster_CPU_min_provisioned_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(CPU) min provisioned/total ratio" or normalize-space(.)="(CPU) минимальное отношение provisioned/total")]',
            '(CPU) min provisioned/total ratio Cluster Choice Button')

        self.page_template_cluster_CPU_min_absolute_provisioned_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(CPU) min absolute provisioned" or normalize-space(.)="(CPU) минимальное абсолютное provisioned")]',
            '(CPU) min absolute provisioned Cluster Choice Button')

        self.page_template_cluster_RAM_min_used_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(RAM) min used/total ratio" or normalize-space(.)="(RAM) минимальное отношение used/total")]',
            '(RAM) min used/total ratio Cluster Choice Button')

        self.page_template_cluster_RAM_min_provisioned_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(RAM) min provisioned/total ratio" or normalize-space(.)="(RAM) минимальное отношение provisioned/total")]',
            '(RAM) min provisioned/total ratio Cluster Choice Button')

        self.page_template_cluster_RAM_min_absolute_provisioned_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(RAM) min absolute provisioned" or normalize-space(.)="(RAM) минимальное абсолютное provisioned")]',
            '(RAM) min absolute provisioned Cluster Choice Button')

        self.page_template_cluster_Storage_min_used_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(Storage) min used/total ratio" or normalize-space(.)="(Storage) минимальное отношение used/total")]',
            '(Storage) min used/total ratio Cluster Choice Button')

        self.page_template_cluster_Storage_min_provisioned_total_ratio_button = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="(Storage) min provisioned/total ratio" or normalize-space(.)="(Storage) минимальное отношение provisioned/total")]',
            '(Storage) min provisioned/total ratio Cluster Choice Button')

        
        #OS Data        
        self.page_template_os_type_dropdown_button = Button(page,'[data-e2e="os-type"]','os-type Button')
        self.page_template_os_type_linux_button = Button(page, '[data-e2e="Linux"]', 'Linux Button')
        self.page_template_os_type_windows_button = Button(page, '[data-e2e="Windows"]', 'Windows Button')                
        #Linnux
        self.page_template_ubuntu_VDI_Ubuntu_24_04_v1 = Button(page, '[data-e2e="VDI Ubuntu 24.04 v1"]', 'VDI Ubuntu 24.04 v1')
        self.page_template_ubuntu_VDI_Ubuntu_24_04_v2 = Button(page, '[data-e2e="VDI Ubuntu 24.04 v2"]', 'VDI Ubuntu 24.04 v2')
        self.page_template_ubuntu_VDI_Ubuntu_24_04_v3 = Button(page, '[data-e2e="VDI Ubuntu 24.04 v3"]', 'VDI Ubuntu 24.04 v3')
        
        self.page_template_ubuntu_22_04_1_v1 = Button(page, '[data-e2e="Ubuntu 22.04.1 v1"]', 'Ubuntu 22.04.1 v1')
        self.page_template_ubuntu_22_04_4_v0 = Button(page, '[data-e2e="Ubuntu 22.04.4 v0"]', 'Ubuntu 22.04.4 v0')
        #Windows            
        self.page_template_windows_server_2019_v2 = Button(page, '[data-e2e="Windows Server 2019 v2"]', 'Windows Server 2019 v2')
        self.page_template_windows_server_2022_v2 = Button(page, '[data-e2e="Windows Server 2022 v2"]', 'Windows Server 2022 v2')
        self.page_template_VDI_Windows_Server_2022_v0 = Button(page, '[data-e2e="VDI Windows Server 2022 v0"]', 'VDI Windows Server 2022 v0') 
        
        #Pool Data
        self.page_template_vm_pool = Button(page, '[data-e2e="vm-pool"]', 'vm-pool')
        self.page_template_least_space_provisioned = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="Least space provisioned" or normalize-space(.)="Наименьшее пространство")]',
            'Least space provisioned')

        self.page_template_least_cpu_provisioned = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="Least CPU provisioned" or normalize-space(.)="Наименьшее ЦПУ")]',
            'Least CPU provisioned')

        self.page_template_least_ram_provisioned = Button(page,
            'xpath=//*[@data-e2e-selectmenu-option and (normalize-space(.)="Least RAM provisioned" or normalize-space(.)="Наименьшее ОЗУ")]',
            'Least RAM provisioned')
        
        #RAM Data
        self.page_storeage_units_dropdown_button = Button(page,'[data-e2e="vm-ram-multilist"]','Storeage Units Selector')
        self.page_template_mb = Button(page,
            'xpath=//*[@data-e2e="menu-value" and (normalize-space(.)="MB" or normalize-space(.)="МБ")]','MB')
        self.page_template_gb = Button(page,
            'xpath=//*[@data-e2e="menu-value" and (normalize-space(.)="GB" or normalize-space(.)="ГБ")]','GB')
        self.page_template_tb = Button(page,
            'xpath=//*[@data-e2e="menu-value" and (normalize-space(.)="TB" or normalize-space(.)="ТБ")]','TB')
        
        #vCPU Class
        self.page_template_vcpu_id_0 = Button(page, '[data-e2e="vcpu-id-0"]', 'vcpu-id-0')
        self.page_template_vcpu_id_1 = Button(page, '[data-e2e="vcpu-id-1"]', 'vcpu-id-1')
        self.page_template_vcpu_id_2 = Button(page, '[data-e2e="vcpu-id-2"]', 'vcpu-id-2')
        self.page_template_vcpu_id_3 = Button(page, '[data-e2e="vcpu-id-3"]', 'vcpu-id-3')
        self.page_template_vcpu_id_4 = Button(page, '[data-e2e="vcpu-id-4"]', 'vcpu-id-4')
        self.page_template_vcpu_id_5 = Button(page, '[data-e2e="vcpu-id-5"]', 'vcpu-id-5')

        #Boot Media
        self.page_template_vm_boot_media = Button(page, '[data-e2e="vm-boot-media"]', 'vm-boot-media')
        self.page_template_boot_media_id_0 = Button(page, '[data-e2e="boot-media-id-0"]', 'boot-media-id-0')
        self.page_template_boot_media_id_1 = Button(page, '[data-e2e="boot-media-id-1"]', 'boot-media-id-1')
        self.page_template_boot_media_id_2 = Button(page, '[data-e2e="boot-media-id-2"]', 'boot-media-id-2')
        self.page_template_boot_media_id_100 = Button(page, '[data-e2e="boot-media-id-100"]', 'boot-media-id-100')
    
        
        #Disk Data Block
        self.page_template_disk_input_label =BaseElement(page,'[for="diskName1"]','Disk Name Input Label')
        self.page_template_disk_slot_input_label =BaseElement(page,'[for="disk-slot1"]','Disk Slot Input Label')
        self.page_template_disk_size_input_label =BaseElement(page,'[for="disk-size1"]','Disk Size Input Label')
        self.page_templated_isk_size_sector_size_input_label =BaseElement(page,'[for="sector-size1"]','Disk Sector Size Input Label')
        self.page_template_iops_limit_input_label =BaseElement(page,'[for="iops-limit1"]','Iops Limit Input Label')
        self.page_template_mbps_limit_input_label = BaseElement(page,'[for="mbps-limit1"]','Mbps Limit Input Label')
        
        #Hover --Disk
        self.page_template_disk_slot_hover =Hover(page,'[data-e2e="tooltip-for-disk-slot1"]','Disk Slot Hover')
        self.page_template_disk_size_hover =Hover(page,'[data-e2e="tooltip-for-disk-size1"]','Disk Size Hover')
        self.page_template_disk_sector_size_hover =Hover(page,'[data-e2e="tooltip-for-sector-size1"]','Disk Slot Size Hover')
        self.page_template_disk_iops_hover =Hover(page,'[data-e2e="tooltip-for-iops-limit1"]','Disk Iops Hover')
        self.page_tempalate_disk_mbps_hover =Hover(page,'[data-e2e="tooltip-for-mbps-limit1"]','Disk Mbps Hover')
        
        #Nnetworks
        self.page_template_network_input_label =BaseElement(page,'[for="network-mbps-limit1"]','Networks Input Label')
        self.page_template_network_tooltip =Hover(page,'[data-e2e="tooltip-for-network-mbps-limit1"]','Network Mbps tooltip')
        
        
        #Inputs 
        
        #General Block
        self.page_template_name_input =Input(page,'[data-e2e="template-name"]','Template Name Input')
        self.page_template_cpu_input =Input(page,'[data-e2e="vm-cpus"]','CPU Name Input')
        self.page_template_ram_input =Input(page,'[data-e2e="vm-ram"]','RAM Name Input')
        
        #Disk Data
        
        #disk names data
        self.page_template_disk1_name_input = Input(page,'[data-e2e="diskName1"]','Disk1 Name Input')
        self.page_template_disk2_name_input = Input(page,'[data-e2e="diskName2"]','Disk2 Name Input')
        self.page_template_disk3_name_input = Input(page,'[data-e2e="diskName3"]','Disk3 Name Input')
        self.page_template_disk4_name_input = Input(page,'[data-e2e="diskName4"]','Disk4 Name Input')
        self.page_template_disk5_name_input = Input(page,'[data-e2e="diskName5"]','Disk4 Name Input') 
        
        #disk slots data      
        self.page_template_slot_input = Button(page,'[id="disk-slot1"]','Slot Name Input1')  
        self.page_template_slot_input2 = Button(page,'[id="disk-slot2"]','Slot Name Input2')
        self.page_template_slot_input3 = Button(page,'[id="disk-slot2"]','Slot Name Input3')
        self.page_template_slot_input4 = Button(page,'[id="disk-slot2"]','Slot Name Input4')
        self.page_template_slot_input5 = Button(page,'[id="disk-slot2"]','Slot Name Input5')
        
        #disk size data
        self.page_template_disk1_size_input = Input(page,'[data-e2e="disk-size1"]','Disk1 Size Input')
        self.page_template_disk2_size_input = Input(page,'[data-e2e="disk-size2"]','Disk2 Size Input')
        self.page_template_disk3_size_input = Input(page,'[data-e2e="disk-size3"]','Disk3 Size Input')
        self.page_template_disk4_size_input = Input(page,'[data-e2e="disk-size4"]','Disk4 Size Input')
        self.page_template_disk5_size_input = Input(page,'[data-e2e="disk-size5"]','Disk5 Size Input')  
        
        #disk slot size input data      
        self.page_template_disk_sector_size_input = Button(page,'[data-e2e="sector-size1"]','Disk Sector Size Input1')
        self.page_template_disk2_sector_size_input = Button(page,'[data-e2e="sector-size2"]','Disk Sector Size Input2')
        self.page_template_disk3_sector_size_input = Button(page,'[data-e2e="sector-size3"]','Disk Sector Size Input3')
        self.page_template_disk4_sector_size_input = Button(page,'[data-e2e="sector-size4"]','Disk Sector Size Input4')
        self.page_template_disk5_sector_size_input = Button(page,'[data-e2e="sector-size4"]','Disk Sector Size Input5')
        
        #disk sector size 
        self.page_template_disk2_sector_size_slot_input =  Button(page,'[data-e2e="sector-size2"]','Disk Sector Size Input2')
        self.page_template_disk3_sector_size_slot_input =  Button(page,'[data-e2e="sector-size3"]','Disk Sector Size Input3')
        self.page_template_disk4_sector_size_slot_input =  Button(page,'[data-e2e="sector-size4"]','Disk Sector Size Input4')
        self.page_template_disk5_sector_size_slot_input =  Button(page,'[data-e2e="sector-size5"]','Disk Sector Size Input5')
      
        #disk slot size param data   
        self.page_template_disk_sector_size_param_512= Button(page,'xpath=//*[@data-e2e-selectmenu-option and normalize-space(.)="512"]','Disk Sector Size Param --512')
        self.page_template_disk_sector_size_param_4096= Button(page,'xpath=//*[@data-e2e-selectmenu-option and normalize-space(.)="4096"]','Disk Sector Size Param --4096')
        
        self.page_template_iops_limit_input =Input(page,'[data-e2e="iops-limit1"]','Diks Iops Limit Input')
        self.page_template_mbps_limit_input =Input(page,'[data-e2e="mbps-limit1"]','Disk Mbps Limit Input')
        
        #Networks
        self.page_template_network_input =Input(page,'[data-e2e="network-mbps-limit1"]','Network Mbps Input')
        
        #Guest OS customization
        self.page_template_root_name_input =Button(page,'[data-e2e="user-name0"]','Root Name Input0')
        
        #Username Data
        self.page_template_user1_name_input =Input(page,'[data-e2e="user-name1"]','Username1 Name Input')
        self.page_template_user2_name_input =Input(page,'[data-e2e="user-name2"]','Username2 Name Input')
        self.page_template_user3_name_input =Input(page,'[data-e2e="user-name3"]','Username3 Name Input')
        
        #Password Data
        self.page_template_password1_input =Input(page,'[data-e2e="user-password0"]','Password Name1 Input')
        self.page_template_password2_input =Input(page,'[data-e2e="user-password1"]','Password Name2 Input')
        self.page_template_password3_input =Input(page,'[data-e2e="user-password2"]','Password Name3 Input')        
        self.page_template_hostname_input = Input(page,'[data-e2e="hostname"]','Host Name Input')
        self.page_template_search_item_input = Input(page,'[data-e2e="search"]','Search item for resolver Button')
       
      
        #Buttons
        #General Data
        self.page_template_cluster_id_dropdown = Button(page,'[data-e2e="vm-cluster-id"]','Cluster ID Dropdown')
        self.page_template_os_type_dropdown =Button(page,'[data-e2e="os-type"]',"OS Type Dropdown")
        self.page_template_os_profile_dropdown =BaseElement(page,'[data-e2e="os-profile"]',"OS Profile Dropdown")
        self.page_template_pool_dropdown = Button(page,'[id="vm-pool"]','Pool Dropdown')
        self.page_template_ram_menu =BaseElement(page,'[data-e2e="vm-ram-multilist"]','RAM Input Dropdown')
        self.page_template_vcpu_class =BaseElement(page,'[data-e2e="vm-vcpu-class"]','vCPU Dropdown')
        self.page_template_boot_maedia_dropdown =BaseElement(page,'[data-e2e="vm-boot-media"]','Boot Madia Dropdown')
        self.page_template_next_step_button = Button(page,'[data-e2e-go-to="disks"]','Next Step Button')
        self.page_template_cancel_button =Button(page,'[data-e2e-leave-vm-factory]','Next Step Cancel Button')
        self.page_template_create_button =Button(page,'[data-e2e="desktopTemplateCreate"]','Template Create Button')
        
        
        #Disk Size Data
        self.page_template_disk_size_dropdown =Button(page,'[data-e2e="disk-size1-multilist"]','Disk Size Dropdown')
        self.page_template_add_disk_button =Button(page,'[data-e2e="addDiskToRow"]','Add Disk Button')
        self.page_template_previous_step_to_general_button =Button(page,'[data-e2e-back-to="general"]','Back to General Step')
        self.page_template_next_step_to_network_button = Button(page,'[data-e2e-go-to="networks"]','Next Step to Networks Button')
        
        #Networks
        self.page_template_add_network_button =Button(page,'[data-e2e="addNetwork"]','Add Network Button')
        self.page_template_back_step_to_disk_button = Button(page,'[data-e2e-back-to="disks"]','Back Step to Disks')
        self.page_template_next_step_to_guest_os_button = Button(page,'[data-e2e-go-to="customization"]','Next Step to Guest OS')
        
        
        #Guest OS        
        self.page_template_new_ssh_add_button = BaseElement(page, '[data-e2e="add-ssh-key"]', 'SSH add-option button')
        self.page_template_new_user_add_button =  Button(page, '[data-e2e="add-user"]', 'User add-option button')
        self.page_template_password_protect_icon = BaseElement(page, '[data-e2e="eye-normal"]', 'Pass Protect Icon')
        self.page_template_ssh_input = Input(page, '[name="ssh-key"]', 'SSH Input')
        self.page_template_new_ssh_add_button = Button(page, '[data-e2e="add-ssh-key"]', 'SSH add-option button')
        self.page_template_previous_step_to_networks_button = Button(page,'[data-e2e-back-to="networks"]','Back to Networks Button')
        self.page_template_add_server_button =Button(page,'[data-add-name-server]',' Add DNS Server Button')
        self.page_template_boot_command = BaseElement(page,'[name="unsavedCommand"]','Boot Command')
        self.page_template_submit_create_template_button = Button(page,'[data-e2e-submit-vm-factory]','Create Template Button')
      
         
    #Methods 
    
    #Step 1/4.General properties         
    def click_create_template_button(self):
        self.page_template_create_button.check_visible()
        self.page_template_create_button.click()        
        
    def send_data_to_template_name_input(self,template_name:str):
        self.page_template_name_input.send_keys_character_by_character(template_name)
        
    def check_cluster_menu_components_dropdown(self):
      self.page_template_cluster_id_dropdown.click()          
      self.page_template_cluster_q7_button.check_visible()
      self.page_template_cluster_q9_button.check_visible()
      self.page_template_cluster_autochoice_button.check_visible()
      self.page_template_cluster_autochoice_button.click()
      self.page_template_cluster_CPU_min_used_total_ratio_button.check_visible()
      self.page_template_cluster_CPU_min_provisioned_total_ratio_button.check_visible()
      self.page_template_cluster_CPU_min_absolute_provisioned_button.check_visible()
      self.page_template_cluster_RAM_min_used_total_ratio_button.check_visible()
      self.page_template_cluster_RAM_min_provisioned_total_ratio_button.check_visible()
      self.page_template_cluster_RAM_min_absolute_provisioned_button.check_visible()
      self.page_template_cluster_Storage_min_used_total_ratio_button.check_visible()
      self.page_template_cluster_Storage_min_provisioned_total_ratio_button.check_visible()
      
      
    def choose_cluster(self, cluster_choice: str = None, autochoice_option: str = None, random_choice: bool = False):
      
        self.page_template_cluster_id_dropdown.click()          
        self.page_template_cluster_q7_button.check_visible()
        self.page_template_cluster_q9_button.check_visible()
        self.page_template_cluster_autochoice_button.check_visible()
        
        all_options_mapping = {
            # Direct cluster selections
            "Q7": self.page_template_cluster_q7_button,
            "Q9": self.page_template_cluster_q9_button,
            "autochoice": self.page_template_cluster_autochoice_button,
            
            # Autochoice metrics
            "cpu_used_ratio": self.page_template_cluster_CPU_min_used_total_ratio_button,
            "cpu_provisioned_ratio": self.page_template_cluster_CPU_min_provisioned_total_ratio_button,
            "cpu_absolute_provisioned": self.page_template_cluster_CPU_min_absolute_provisioned_button,
            "ram_used_ratio": self.page_template_cluster_RAM_min_used_total_ratio_button,
            "ram_provisioned_ratio": self.page_template_cluster_RAM_min_provisioned_total_ratio_button,
            "ram_absolute_provisioned": self.page_template_cluster_RAM_min_absolute_provisioned_button,
            "storage_used_ratio": self.page_template_cluster_Storage_min_used_total_ratio_button,
            "storage_provisioned_ratio": self.page_template_cluster_Storage_min_provisioned_total_ratio_button,
        }
        
        # Random autochoice among all options
        if random_choice:
            selected_option = random.choice(list(all_options_mapping.keys()))
            selected_button = all_options_mapping[selected_option]
            (f"Randomly selected: {selected_option}")
        
        # Specific choice provided
        else:
            choice = cluster_choice or autochoice_option
            if not choice:
                raise ValueError("Either cluster_choice, autochoice_option, or random_choice=True must be provided")
            
            selected_button = all_options_mapping.get(choice)
            if not selected_button:
                raise ValueError(f"Invalid choice: {choice}. Available options: {list(all_options_mapping.keys())}")
        
        # Handle autochoice metrics - click autochoice button first
        choice_used = cluster_choice or autochoice_option or selected_option
        if choice_used in ["cpu_used_ratio", "cpu_provisioned_ratio", "cpu_absolute_provisioned", 
                        "ram_used_ratio", "ram_provisioned_ratio", "ram_absolute_provisioned",
                        "storage_used_ratio", "storage_provisioned_ratio"]:
            self.page_template_cluster_autochoice_button.click()
        
        selected_button.check_visible()
        selected_button.click()
                          
    def choose_OS_via_dropdown(self,os_type:str):
      self.page_template_os_type_dropdown_button.click()      
      self.page_template_os_type_linux_button.check_visible()
    #   self.page_template_os_type_windows_button.check_visible()     
      self.page_template_os_type_button = Button(self.page, f'[data-e2e="{os_type}"]', 'OS Type Button') 
      self.page_template_os_type_button.click()
      
    
    def choose_OS_profile_via_dropdown(self, os_profile: str = None, os_type: str = None, random_choice: bool = False):
        self.page_template_os_profile_dropdown.click()
        
        profile_mapping = {
            # "Ubuntu 22.04 v1": self.page_template_ubuntu_22_04_1_v1,
            # "Ubuntu 22.04 v0": self.page_template_ubuntu_22_04_4_v0,
            # "Ubuntu VDI 24.04 v1": self.page_template_ubuntu_VDI_Ubuntu_24_04_v1,
            # "Ubuntu VDI 24.04 v2": self.page_template_ubuntu_VDI_Ubuntu_24_04_v2,
            "VDI Ubuntu 24.04 v3":self.page_template_ubuntu_VDI_Ubuntu_24_04_v3,
            "VDI Windows Server 2022 v0":self.page_template_VDI_Windows_Server_2022_v0,
            # "Windows Server 2019 v2": self.page_template_windows_server_2019_v2,
            # "Windows Server 2022 v2": self.page_template_windows_server_2022_v2,
        }
        
        os_profiles = {
            # "Linux": ["Ubuntu 22.04 v1", "Ubuntu 22.04 v0", "Ubuntu VDI 24.04 v1"],
            # "Linux": ["Ubuntu VDI 24.04 v1"],
            "Linux": ["VDI Ubuntu 24.04 v3"],
            "Windows": ["VDI Windows Server 2022 v0"]
        }
        
        if random_choice:
            if os_type:
                # Random choice from specified OS type
                available_profiles = os_profiles[os_type]
            else:
                # Completely random choice from all profiles
                available_profiles = list(profile_mapping.keys())
            
            selected_profile_name = random.choice(available_profiles)
            selected_button = profile_mapping[selected_profile_name]
            logger.info(f"Randomly selected: {selected_profile_name}")
            selected_button.click()
            return selected_profile_name, os_type
        
        if not os_profile:
            raise ValueError("OS profile is required when not using random_choice")
        
        if os_profile not in profile_mapping:
            available_profiles = list(profile_mapping.keys())
            raise ValueError(f"Invalid OS profile: {os_profile}. Available options: {available_profiles}")
        
        selected_button = profile_mapping[os_profile]
        selected_button.click()
        return os_profile, os_type
        
    def choose_pool_location_strategies(self, pool_location_strategie: str = None, random_choice: bool = False):
        self.page_template_pool_dropdown.click()              
        choice_mapping = {      
            "Least space provisioned": self.page_template_least_space_provisioned,
            "Least CPU provisioned": self.page_template_least_cpu_provisioned,
            "Least RAM provisioned": self.page_template_least_ram_provisioned       
            }
        
        if random_choice:
            pool_location_strategie = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected pool strategy: {pool_location_strategie}")
        
        selected_button = choice_mapping.get(pool_location_strategie)            
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid pool choice: {pool_location_strategie}. Available options: {list(choice_mapping.keys())}")
                    
    def check_cpu_input_hover_presence(self):
        self.page_template_cpu_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.CPU_HOVER_TEXT) 
        
    def check_ram_input_hover_presence(self):
        self.page_template_ram_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.RAM_HOVER_TEXT)    
         
    def send_data_to_cpu_input(self,cpu_param:str):
        self.page_template_cpu_input.send_keys_character_by_character(cpu_param)
        
    def send_data_to_ram_input(self,ram_param:str):
        self.page_template_ram_input.send_keys_character_by_character(ram_param)
        
   
    def choose_data_storeage_units_via_dropdown(self,storeage_units:str):
        self.page_storeage_units_dropdown_button.click()
        choice_mapping = {
            "MB":self.page_template_mb,
            "GB":self.page_template_gb,
            "TB":self.page_template_tb
            }
        selected_button = choice_mapping.get(storeage_units)
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid storeage unit choice: {storeage_units}. Available options: {list(choice_mapping.keys())}")
        
    def choose_vCPU_class_via_dropdown(self, vCPU_class: str = None, random_choice: bool = False):
        self.page_template_vcpu_class.click()
        
        choice_mapping = {
            "0": self.page_template_vcpu_id_0,
            "1": self.page_template_vcpu_id_1,
            "2": self.page_template_vcpu_id_2,
            "3": self.page_template_vcpu_id_3,
            "4": self.page_template_vcpu_id_4,
            "5": self.page_template_vcpu_id_5
        }
        
        if random_choice:
            vCPU_class = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected vCPU class: {vCPU_class}")
        
        selected_button = choice_mapping.get(vCPU_class)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid vCPU_class choice: {vCPU_class}. Available options: {list(choice_mapping.keys())}")

    def choose_boot_media_via_dropdown(self, boot_media: str = None, random_choice: bool = False):
        self.page_template_vm_boot_media.click()
        
        choice_mapping = {
            "None": self.page_template_boot_media_id_0,
            "FreeBSD 12.2-RELEASE": self.page_template_boot_media_id_1,
            "SystemRescue CD 10.01": self.page_template_boot_media_id_2,
            "Windaz test": self.page_template_boot_media_id_100,
        }
        
        if random_choice:
            boot_media = random.choice(list(choice_mapping.keys()))
            logger.info(f"Randomly selected boot media: {boot_media}")
        
        selected_button = choice_mapping.get(boot_media)
        
        if selected_button:
            selected_button.check_visible()
            selected_button.click()
        else:
            raise ValueError(f"Invalid boot_media choice: {boot_media}. Available options: {list(choice_mapping.keys())}")
            
    def check_go_to_disks_button_disabled(self):
        self.page_template_next_step_button.check_visible()
        self.page_template_next_step_button.check_disabled()
        
    def check_go_to_disks_button_enabled(self):
        self.page_template_next_step_button.check_visible()
        self.page_template_next_step_button.check_enabled(timeout=60000)
        
    def check_go_to_disks_button_click(self):
        self.page_template_next_step_button.check_visible()
        self.page_template_next_step_button.click()
        
        
    #Step 2/4.Disks    
    def send_data_to_disk_name_input(self,disk_count,disk_name:str):
      
        choice_mapping = {
            "disk_name1": self.page_template_disk1_name_input,
            "disk_name2": self.page_template_disk2_name_input,
            "disk_name3": self.page_template_disk3_name_input,
            "disk_name4": self.page_template_disk4_name_input,
            "disk_name5": self.page_template_disk5_name_input
        }
        selected_button = choice_mapping.get(disk_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.send_keys_character_by_character(disk_name)
        else:
            raise ValueError(f"Invalid disk name selectors list choice: {disk_count}. Available options: {list(choice_mapping.keys())}")
           
    
    def send_data_to_disk_size_input(self,disk_count,disk_param:str):
      
        choice_mapping = {
            "disk1": self.page_template_disk1_size_input,
            "disk2": self.page_template_disk2_size_input,
            "disk3": self.page_template_disk3_size_input,
            "disk4": self.page_template_disk4_size_input,
            "disk5": self.page_template_disk5_size_input
        }
        selected_button = choice_mapping.get(disk_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.send_keys_character_by_character(disk_param)
        else:
            raise ValueError(f"Invalid disk size selectors list choice: {disk_count}. Available options: {list(choice_mapping.keys())}")
           
           
    def check_first_disk_slot_disabled(self):
        """Check first disk slot is enabled"""
        self.page_template_slot_input.check_disabled()
        
        
    def check_specific_disk_slot_enabled(self,disk_count:str):
        """Check specific disk slot is enabled"""
        choice_mapping = {
            "disk_slot2": self.page_template_slot_input2,
            "disk_slot3": self.page_template_slot_input3,
            "disk_slot4": self.page_template_slot_input4,
            "disk_slot5": self.page_template_slot_input5         
        }
        selected_button = choice_mapping.get(disk_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.check_enabled()
        else:
            raise ValueError(f"Invalid disk slot selectors list choice: {disk_count}. Available options: {list(choice_mapping.keys())}")
    
        
    def check_first_sector_size_disabled(self):
        self.page_template_disk_sector_size_input.check_disabled()
        
    def check_specific_sector_size_enabled(self,disk_count):
        """Check specific disk slot is enabled"""
        choice_mapping = {
            "disk_slot2": self.page_template_slot_input2,
            "disk_slot3": self.page_template_slot_input3,
            "disk_slot4": self.page_template_slot_input4,
            "disk_slot5": self.page_template_slot_input5         
        }
        selected_button = choice_mapping.get(disk_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.check_enabled()
        else:
            raise ValueError(f"Invalid disk size slot selectors list choice: {disk_count}. Available options: {list(choice_mapping.keys())}")
        
        
    def choose_sector_size(self, disk_count: str = None, disk_slot_size: str = None, random_disk: bool = False, random_sector: bool = False):
        """disk slot and sector size with flexible random options"""
        
        disk_slot_mapping = {
            "disk_slot2": self.page_template_disk2_sector_size_slot_input,
            "disk_slot3": self.page_template_disk3_sector_size_slot_input,
            "disk_slot4": self.page_template_disk4_sector_size_slot_input,
            "disk_slot5": self.page_template_disk5_sector_size_slot_input
        }
        
        sector_size_mapping = {
            "512": self.page_template_disk_sector_size_param_512,    
            "4096": self.page_template_disk_sector_size_param_4096,      
        }
        
        if random_disk:
            disk_key = random.choice(list(disk_slot_mapping.keys()))
            selected_disk_button = disk_slot_mapping[disk_key]
            logger.info(f"Randomly selected disk slot: {disk_key}")
        else:
            if not disk_count:
                raise ValueError("disk count is required when random_disk=False")
            selected_disk_button = disk_slot_mapping.get(disk_count)
            if not selected_disk_button:
                raise ValueError(f"Invalid disk count: {disk_count}. Available: {list(disk_slot_mapping.keys())}")
            disk_key = disk_count
        
        if random_sector:
            sector_key = random.choice(list(sector_size_mapping.keys()))
            selected_sector_button = sector_size_mapping[sector_key]
            logger.info(f"Randomly selected sector size: {sector_key}")
        else:
            if not disk_slot_size:
                raise ValueError("disk slot size is required when random_sector=False")
            selected_sector_button = sector_size_mapping.get(disk_slot_size)
            if not selected_sector_button:
                raise ValueError(f"Invalid disk slot size: {disk_slot_size}. Available: {list(sector_size_mapping.keys())}")
            sector_key = disk_slot_size
        
        selected_disk_button.click()
        selected_disk_button.check_enabled()
        selected_sector_button.click()
        selected_sector_button.check_enabled()
    
        
    def check_disk_slot_input_hover_presence(self):
        self.page_template_disk_slot_hover(expected_texts=
                                            UiTextPatterns.DISK_SLOT_HOVER_TEXT)         
    def check_disk_size_slot_input_hover_presence(self):
        self.page_template_disk_size_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.DISK_SIZE_HOVER_TEXT)        
    def check_disk_size_sector_size_input_hover_presence(self):
        self.page_template_disk_sector_size_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.DISK_SECTOR_SIZE_HOVER_TEXT)        
    def check_disk_iops_limit_input_hover_presence(self):
        self.page_template_disk_iops_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.DISK_IOPS_LIMIT_HOVER_TEXT)
    def check_disk_mbps_limit_input_hover_presence(self):
        self.page_tempalate_disk_mbps_hover.check_text_on_hover(expected_texts=
                                                                    UiTextPatterns.DISK_MBPS_LIMIT_HOVER_TEXT)       
    def send_data_to_template_iop_input(self,iops_param:str):
        self.page_template_iops_limit_input.send_keys_character_by_character(iops_param)
        
    def send_data_to_template_mpbs_input(self,mbps_param:str):
        self.page_template_mbps_limit_input.send_keys_character_by_character(mbps_param)
        
    def click_add_new_disk_button(self):
        self.page_template_add_disk_button.check_visible()
        self.page_template_add_disk_button.click()
        
    def check_back_to_general_step_button_enabled(self):
        self.page_template_previous_step_to_general_button.check_visible()
        self.page_template_previous_step_to_general_button.check_enabled()
        
    def check_back_to_general_step_button_disabled(self):
        self.page_template_previous_step_to_general_button.check_visible()
        self.page_template_previous_step_to_general_button.check_disabled()
        
    def click_back_to_general_step_button(self):
        self.page_template_previous_step_to_general_button.check_visible()
        self.page_template_previous_step_to_general_button.click()
                
    def check_template_next_step_to_network_button_enabled(self):
        self.page_template_next_step_to_network_button.check_visible()
        self.page_template_next_step_to_network_button.check_enabled()
        
    def check_template_next_step_to_network_button_disabled(self):
        self.page_template_next_step_to_network_button.check_visible()
        self.page_template_next_step_to_network_button.check_disabled()
        
    def click_template_next_step_to_network_button(self):
        self.page_template_next_step_to_network_button.check_visible()
        self.page_template_next_step_to_network_button.click()
        
            
    #Step 3/4.Networks  
    #Check Hover Text --Need to be replace Disk->Network  
    def check_network_mbps_limit_input_hover_presence(self):
        self.page_template_network_tooltip.check_text_on_hover(UiTextPatterns.DISK_MBPS_LIMIT_HOVER_TEXT)
        
    def send_data_to_networks_mbps_limit_nput(self,mbps_param:str):
        self.page_template_network_input.send_keys_character_by_character(mbps_param)

    def click_add_new_network_button(self):
        self.page_template_add_network_button.check_visible()
        self.page_template_add_network_button.click()    
        
    def check_back_to_disks_step_button_enabled(self):
        self.page_template_back_step_to_disk_button.check_visible()
        self.page_template_back_step_to_disk_button.check_enabled()
        
    def check_back_to_disks_step_button_disabled(self):
        self.page_template_back_step_to_disk_button.check_visible()
        self.page_template_back_step_to_disk_button.check_disabled()
        
    def click_back_to_disks_step_button(self):
        self.page_template_back_step_to_disk_button.check_visible()
        self.page_template_back_step_to_disk_button.click()
        
        
    def check_next_to_guest_os_step_button_enabled(self):
        self.page_template_next_step_to_guest_os_button.check_visible()
        self.page_template_next_step_to_guest_os_button.check_enabled()
        
    def check_next_to_guest_os_step_button_disabled(self):
        self.page_template_next_step_to_guest_os_button.check_visible()
        self.page_template_next_step_to_guest_os_button.check_disabled()
        
    def click_next_to_guest_os_step_button(self):
        self.page_template_next_step_to_guest_os_button.check_visible()
        self.page_template_next_step_to_guest_os_button.click()
        
    #Step 4/4.Guest OS customization    
    def check_template_root_name_input_disabled(self):
        self.page_template_root_name_input.check_visible()
        self.page_template_root_name_input.check_disabled()
        
    def send_data_to_password_template_input(self,pass_count,pass_name:str):
      
        choice_mapping = {
            "pass1": self.page_template_password1_input,
            "pass2": self.page_template_password2_input,
            "pass3": self.page_template_password3_input,
        }
        selected_button = choice_mapping.get(pass_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.send_keys_character_by_character(pass_name)
        else:
            raise ValueError(f"Invalid password selectors list choice: {pass_count}. Available options: {list(choice_mapping.keys())}")
        
        
    def send_data_to_ssh_name_input(self, ssh: str, enable_ssh: bool = True):
        """Send data to SSH input only if SSH is provided"""
        if ssh and enable_ssh:
            self.page_template_ssh_input.fill(ssh)
            logger.info("SSH key successfully entered")
        else:
            logger.warning("No SSH key provided or SSH disabled, skipping SSH input")
                
    def check_password_protect_icon_presence(self):
        self.page_template_password_protect_icon.check_visible()
        
    def check_ssh_add_button_enabled(self):
        self.page_template_new_ssh_add_button.check_visible()
        self.page_template_new_ssh_add_button.check_enabled()
        
    def click_ssh_add_button(self):
        self.page_template_new_ssh_add_button.check_visible()
        self.page_template_new_ssh_add_button.click()
            
    def check_user_add_button_enabled(self):
        self.page_template_new_user_add_button.check_visible()
        self.page_template_new_user_add_button.check_enabled()
        
    def click_user_add_button(self):
        self.page_template_new_user_add_button.check_visible()
        self.page_template_new_user_add_button.click()
        
            
    def send_data_to_username_template_input(self,user_count,user_name:str):
      
        choice_mapping = {
            "user1": self.page_template_user1_name_input,
            "user2": self.page_template_user2_name_input,
            "user3": self.page_template_user3_name_input,
        }
        selected_button = choice_mapping.get(user_count)       
        if selected_button:
            selected_button.check_visible()
            selected_button.send_keys_character_by_character(user_name)
        else:
            raise ValueError(f"Invalid user selectors list choice: {user_count}. Available options: {list(choice_mapping.keys())}")
                
    def send_data_to_hostname_input(self,hostname:str):
        self.page_template_hostname_input.send_keys_character_by_character(hostname)
        
    def send_data_to_search_resolver_input(self,resolver:str):
        self.page_template_search_item_input.send_keys_character_by_character(resolver)
        
    def send_data_to_name_server_input(self,dns_server_count:str,dns_server_data:str):
        server_input= self.page_template_name_server1_input = Input(self.page,
                                                                    f'[data-e2e="name-server{dns_server_count}"]',
                                                                    f'Name Server Input{dns_server_count}')
        server_input.send_keys_character_by_character(dns_server_data)
              
    def check_add_server_button_enabled(self):
        self.page_template_add_server_button.check_enabled()
        
    def click_add_server_button(self):
        self.page_template_add_server_button.click()
        
    def check_back_to_networks_step_button_enabled(self):
        self.page_template_previous_step_to_networks_button.check_visible()
        self.page_template_previous_step_to_networks_button.check_enabled()
        
    def check_back_to_networks_step_button_disabled(self):
        self.page_template_previous_step_to_networks_button.check_visible()
        self.page_template_previous_step_to_networks_button.check_disabled()
        
    def click_back_to_networks_step_button(self):
        self.page_template_previous_step_to_networks_button.check_visible()
        self.page_template_previous_step_to_networks_button.click()        
       
    def check_create_template_button_enabled(self):
        self.page_template_submit_create_template_button.check_visible()
        self.page_template_submit_create_template_button.check_enabled()
        
    def check_create_template_button_disabled(self):
        self.page_template_submit_create_template_button.check_visible()
        self.page_template_submit_create_template_button.check_disabled()
        
    def click_create_template_button_button(self):
        self.page_template_submit_create_template_button.check_visible()
        self.page_template_submit_create_template_button.click()
                
    def check_cancel_template_button_enabled(self):
        self.page_template_cancel_button.check_enabled()
        
    def check_cancel_template_button_disabled(self):
        self.page_template_cancel_button.check_visible()
        self.page_template_submit_create_template_button.check_disabled()
        
    def click_cancel_template_button(self):
        self.page_template_cancel_button.check_visible()
        self.page_template_submit_create_template_button.click()
        
   
        
    # def create_template(
    #     self, 
    #     template_name: str,
    #     os_type: str,
    #     cpu_param: str,
    #     ram_param: str,
    #     disk_size: str,
    #     mbps_param: str,
    #     iops_param: str,
    #     disk_name: str,
    #     user_pass1: str,
    #     hostname_data: str,  
    #     resolver_data: str,  
    #     ssh: str = None, 
    #     additional_username: str = None,
    #     additional_password: str = None,
    #     cluster_choice: str = None,
    #     autochoice_option: str = None,
    #     random_cluster: bool = True,
    #     os_profile: str = None,
    #     random_os_profile: bool = True,
    #     pool_strategy: str = None,
    #     random_pool_strategy: bool = True,
    #     vcpu_class: str = None,
    #     random_vcpu_class: bool = True,
    #     boot_media: str = None,
    #     random_boot_media: bool = True,
    #     # ADDITIONAL DISKS PARAMETERS 
    #     additional_disk2_name: str = None,
    #     additional_disk2_size: str = None,
    #     additional_disk2_sector_size: str = None,
    #     additional_disk3_name: str = None,
    #     additional_disk3_size: str = None,
    #     additional_disk3_sector_size: str = None,
    #     additional_disk4_name: str = None,
    #     additional_disk4_size: str = None,
    #     additional_disk4_sector_size: str = None,
    #     additional_disk5_name: str = None,
    #     additional_disk5_size: str = None,
    #     additional_disk5_sector_size: str = None
    # ):
    #     """
    #     Create a template with support for multiple additional disks (up to 5 total)
    #     """
    #     # Step 1/4: General Properties
    #     logger.info("Step 1/4: General Properties")
    #     self.click_create_template_button()
    #     self.check_go_to_disks_button_disabled()
    #     self.check_cancel_template_button_enabled()
    #     self.send_data_to_template_name_input(template_name=template_name)
        
    #     # Configure cluster settings
    #     if random_cluster:
    #         self.choose_cluster(random_choice=True)
    #         logger.info("Using random cluster selection")
    #     elif cluster_choice:
    #         self.choose_cluster(cluster_choice=cluster_choice, random_choice=False)
    #         logger.info(f"Using specific cluster: {cluster_choice}")
    #     elif autochoice_option:
    #         self.choose_cluster(autochoice_option=autochoice_option, random_choice=False)
    #         logger.info(f"Using autochoice metric: {autochoice_option}")
    #     else:
    #         self.choose_cluster(random_choice=True)
    #         logger.info("No cluster specified, using random selection")
        
    #     # Configure OS settings
    #     self.choose_OS_via_dropdown(os_type=os_type)
        
    #     # Configure OS profile
    #     if random_os_profile:
    #         selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
    #             os_type=os_type, 
    #             random_choice=True
    #         )
    #         logger.info(f"Using random OS profile: {selected_profile}")
    #     elif os_profile:
    #         selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
    #             os_profile=os_profile,
    #             os_type=os_type,
    #             random_choice=False
    #         )
    #         logger.info(f"Using specific OS profile: {selected_profile}")
    #     else:
    #         selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
    #             os_type=os_type,
    #             random_choice=True
    #         )
    #         logger.info(f"No OS profile specified, using random selection: {selected_profile}")
        
    #     # Configure pool location strategy
    #     if random_pool_strategy:
    #         self.choose_pool_location_strategies(random_choice=True)
    #         logger.info("Using random pool location strategy")
    #     elif pool_strategy:
    #         self.choose_pool_location_strategies(
    #             pool_location_strategie=pool_strategy, 
    #             random_choice=False
    #         )
    #         logger.info(f"Using specific pool strategy: {pool_strategy}")
    #     else:
    #         self.choose_pool_location_strategies(random_choice=True)
    #         logger.info("No pool strategy specified, using random selection")
        
    #     # Set CPU and RAM
    #     self.send_data_to_cpu_input(cpu_param=cpu_param)
    #     self.send_data_to_ram_input(ram_param=ram_param)

    #     # Configure vCPU class
    #     if random_vcpu_class:
    #         self.choose_vCPU_class_via_dropdown(random_choice=True)
    #         logger.info("Using random vCPU class selection")
    #     elif vcpu_class:
    #         self.choose_vCPU_class_via_dropdown(
    #             vCPU_class=vcpu_class, 
    #             random_choice=False
    #         )
    #         logger.info(f"Using specific vCPU class: {vcpu_class}")
    #     else:
    #         self.choose_vCPU_class_via_dropdown(random_choice=True)
    #         logger.info("No vCPU class specified, using random selection")
        
    #     # Configure boot media
    #     if random_boot_media:
    #         self.choose_boot_media_via_dropdown(random_choice=True)
    #         logger.info("Using random boot media selection")
    #     elif boot_media:
    #         self.choose_boot_media_via_dropdown(
    #             boot_media=boot_media, 
    #             random_choice=False
    #         )
    #         logger.info(f"Using specific boot media: {boot_media}")
    #     else: 
    #         self.choose_boot_media_via_dropdown(random_choice=True)
    #         logger.info("No boot media specified, using random selection")
        
    #     self.check_go_to_disks_button_enabled()
    #     self.check_cancel_template_button_enabled()
    #     self.check_go_to_disks_button_click()
        
    #     # Step 2/4: Disks Configuration
    #     logger.info("Step 2/4: Disks Configuration")
    #     self.check_template_next_step_to_network_button_disabled()
    #     self.check_back_to_general_step_button_enabled()
        
    #     # Configure first disk (required)
    #     self.send_data_to_disk_name_input(disk_count='disk_name1', disk_name=disk_name)
    #     self.check_first_disk_slot_disabled()
    #     self.send_data_to_disk_size_input(disk_count='disk1', disk_param=disk_size)
    #     self.check_first_sector_size_disabled()
        
    #     self.send_data_to_template_mpbs_input(mbps_param=mbps_param)
    #     self.send_data_to_template_iop_input(iops_param=iops_param)
        
    #     # ADDITIONAL DISKS LOGIC 
    #     # Disk 2
    #     if all([additional_disk2_name, additional_disk2_size]):
    #         logger.info(f"Adding disk 2: {additional_disk2_name}")
    #         self.click_add_new_disk_button()
    #         self.send_data_to_disk_name_input(disk_count='disk_name2', disk_name=additional_disk2_name)
    #         self.send_data_to_disk_size_input(disk_count='disk2', disk_param=additional_disk2_size)
    #         self.check_specific_disk_slot_enabled(disk_count='disk_slot2')
            
    #         if additional_disk2_sector_size:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot2',
    #                 disk_slot_size=additional_disk2_sector_size,
    #                 random_disk=False,
    #                 random_sector=False
    #             )
    #             logger.info(f"Using specific sector size for disk 2: {additional_disk2_sector_size}")
    #         else:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot2', 
    #                 disk_slot_size=None,
    #                 random_disk=False,
    #                 random_sector=True
    #             )
    #             logger.info("Using random sector size for disk 2")
                
    #         logger.info(f"Successfully added disk 2: {additional_disk2_name}")
    #     else:
    #         logger.info("No disk 2 to add - both disk name and size are required")
        
    #     # Disk 3
    #     if all([additional_disk3_name, additional_disk3_size]):
    #         logger.info(f"Adding disk 3: {additional_disk3_name}")
    #         self.click_add_new_disk_button()
    #         self.send_data_to_disk_name_input(disk_count='disk_name3', disk_name=additional_disk3_name)
    #         self.send_data_to_disk_size_input(disk_count='disk3', disk_param=additional_disk3_size)
    #         self.check_specific_disk_slot_enabled(disk_count='disk_slot3')
            
    #         if additional_disk3_sector_size:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot3',
    #                 disk_slot_size=additional_disk3_sector_size,
    #                 random_disk=False,
    #                 random_sector=False
    #             )
    #             logger.info(f"Using specific sector size for disk 3: {additional_disk3_sector_size}")
    #         else:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot3', 
    #                 disk_slot_size=None,
    #                 random_disk=False,
    #                 random_sector=True
    #             )
    #             logger.info("Using random sector size for disk 3")
                
    #         logger.info(f"Successfully added disk 3: {additional_disk3_name}")
    #     else:
    #         logger.info("No disk 3 to add - both disk name and size are required")
        
    #     # Disk 4
    #     if all([additional_disk4_name, additional_disk4_size]):
    #         logger.info(f"Adding disk 4: {additional_disk4_name}")
    #         self.click_add_new_disk_button()
    #         self.send_data_to_disk_name_input(disk_count='disk_name4', disk_name=additional_disk4_name)
    #         self.send_data_to_disk_size_input(disk_count='disk4', disk_param=additional_disk4_size)
    #         self.check_specific_disk_slot_enabled(disk_count='disk_slot4')
            
    #         if additional_disk4_sector_size:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot4',
    #                 disk_slot_size=additional_disk4_sector_size,
    #                 random_disk=False,
    #                 random_sector=False
    #             )
    #             logger.info(f"Using specific sector size for disk 4: {additional_disk4_sector_size}")
    #         else:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot4', 
    #                 disk_slot_size=None,
    #                 random_disk=False,
    #                 random_sector=True
    #             )
    #             logger.info("Using random sector size for disk 4")
                
    #         logger.info(f"Successfully added disk 4: {additional_disk4_name}")
    #     else:
    #         logger.info("No disk 4 to add - both disk name and size are required")
        
    #     # Disk 5
    #     if all([additional_disk5_name, additional_disk5_size]):
    #         logger.info(f"Adding disk 5: {additional_disk5_name}")
    #         self.click_add_new_disk_button()
    #         self.send_data_to_disk_name_input(disk_count='disk_name5', disk_name=additional_disk5_name)
    #         self.send_data_to_disk_size_input(disk_count='disk5', disk_param=additional_disk5_size)
    #         self.check_specific_disk_slot_enabled(disk_count='disk_slot5')
            
    #         if additional_disk5_sector_size:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot5',
    #                 disk_slot_size=additional_disk5_sector_size,
    #                 random_disk=False,
    #                 random_sector=False
    #             )
    #             logger.info(f"Using specific sector size for disk 5: {additional_disk5_sector_size}")
    #         else:
    #             self.choose_sector_size(
    #                 disk_count='disk_slot5', 
    #                 disk_slot_size=None,
    #                 random_disk=False,
    #                 random_sector=True
    #             )
    #             logger.info("Using random sector size for disk 5")
                
    #         logger.info(f"Successfully added disk 5: {additional_disk5_name}")
    #     else:
    #         logger.info("No disk 5 to add - both disk name and size are required")
        
    #     self.check_back_to_general_step_button_enabled()
    #     self.check_template_next_step_to_network_button_enabled()
    #     self.click_template_next_step_to_network_button()
        
    #     # Step 3/4: Networks Configuration
    #     logger.info("Proceeding to Step 3/4: Networks Configuration")
    #     self.check_back_to_disks_step_button_enabled()
    #     self.check_next_to_guest_os_step_button_enabled()
    #     self.check_cancel_template_button_enabled()
        
    #     self.send_data_to_networks_mbps_limit_nput(mbps_param=mbps_param)
        
    #     self.check_back_to_disks_step_button_enabled()
    #     self.check_next_to_guest_os_step_button_enabled()
    #     self.click_next_to_guest_os_step_button()
        
    #     # Step 4/4: Guest OS Customization
    #     logger.info("Proceeding to Step 4/4: Guest OS Customization")
    #     self.check_cancel_template_button_enabled()
    #     self.check_back_to_networks_step_button_enabled()
    #     self.check_template_root_name_input_disabled()
    #     self.check_password_protect_icon_presence()

    #     # Configure root user (user0)
    #     self.send_data_to_password_template_input(pass_count="pass1", pass_name=user_pass1)

    #     # Configure SSH only if enabled
    #     if ssh:
    #         logger.info("Configuring SSH key")
    #         self.send_data_to_ssh_name_input(ssh=ssh, enable_ssh=True)
    #         self.check_ssh_add_button_enabled()
    #         self.click_ssh_add_button()
    #     else:
    #         logger.info("SSH configuration skipped - no key provided or SSH disabled")
        
    #     # ADDITIONAL USER LOGIC 
    #     if all([additional_username, additional_password]):
    #         logger.info(f"Adding additional user: {additional_username}")
    #         self.check_user_add_button_enabled()
    #         self.click_user_add_button()
    #         self.send_data_to_username_template_input(user_count="user1", user_name=additional_username)
    #         self.send_data_to_password_template_input(pass_count="pass2", pass_name=additional_password)           
    #         logger.info(f"Successfully added additional user: {additional_username}")
    #     else:
    #         logger.info("No additional user to add - both username and password are required")
        
    #     # Configure system settings
    #     self.send_data_to_hostname_input(hostname=hostname_data)
    #     self.send_data_to_search_resolver_input(resolver=resolver_data)
        
    #     # Configure DNS settings
    #     self.check_add_server_button_enabled()
    #     self.send_data_to_name_server_input(
    #         dns_server_count="0",
    #         dns_server_data=VariablesNames.DNS_SERVER_DATA0
    #     )
    #     self.click_add_server_button()
    #     self.send_data_to_name_server_input(
    #         dns_server_count="1", 
    #         dns_server_data=VariablesNames.DNS_SERVER_DATA1
    #     )        
    #     self.check_back_to_networks_step_button_enabled()
    #     self.check_create_template_button_enabled()
    #     self.check_cancel_template_button_enabled()
    #     self.click_create_template_button_button()
                        
    def create_template(
    self, 
    template_name: str,
    os_type: str,
    cpu_param: str,
    ram_param: str,
    disk_size: str,
    mbps_param: str,
    iops_param: str,
    disk_name: str,
    resolver_data: str,  
    # cluster_choice: str = None,
    # autochoice_option: str = None,
    # random_cluster: bool = True,
    os_profile: str = None,
    random_os_profile: bool = True,
    pool_strategy: str = None,
    random_pool_strategy: bool = True,
    vcpu_class: str = None,
    random_vcpu_class: bool = True,
    boot_media: str = None,
    random_boot_media: bool = True,
    # ADDITIONAL DISKS PARAMETERS 
    additional_disk2_name: str = None,
    additional_disk2_size: str = None,
    additional_disk2_sector_size: str = None,
    additional_disk3_name: str = None,
    additional_disk3_size: str = None,
    additional_disk3_sector_size: str = None,
    additional_disk4_name: str = None,
    additional_disk4_size: str = None,
    additional_disk4_sector_size: str = None,
    additional_disk5_name: str = None,
    additional_disk5_size: str = None,
    additional_disk5_sector_size: str = None
):
        """
        Create a template with support for multiple additional disks (up to 5 total)
        Hostname, SSH, and all user configuration removed
        """
        # Step 1/4: General Properties
        logger.info("Step 1/4: General Properties")
        self.click_create_template_button()
        self.check_go_to_disks_button_disabled()
        self.check_cancel_template_button_enabled()
        self.send_data_to_template_name_input(template_name=template_name)
        
        # Configure cluster settings
        # if random_cluster:
        #     self.choose_cluster(random_choice=True)
        #     logger.info("Using random cluster selection")
        # elif cluster_choice:
        #     self.choose_cluster(cluster_choice=cluster_choice, random_choice=False)
        #     logger.info(f"Using specific cluster: {cluster_choice}")
        # elif autochoice_option:
        #     self.choose_cluster(autochoice_option=autochoice_option, random_choice=False)
        #     logger.info(f"Using autochoice metric: {autochoice_option}")
        # else:
        #     self.choose_cluster(random_choice=True)
        #     logger.info("No cluster specified, using random selection")
        
        # Configure OS settings
        self.choose_OS_via_dropdown(os_type=os_type)
        
        # Configure OS profile
        if random_os_profile:
            selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
                os_type=os_type, 
                random_choice=True
            )
            logger.info(f"Using random OS profile: {selected_profile}")
        elif os_profile:
            selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
                os_profile=os_profile,
                os_type=os_type,
                random_choice=False
            )
            logger.info(f"Using specific OS profile: {selected_profile}")
        else:
            selected_profile, profile_os_type = self.choose_OS_profile_via_dropdown(
                os_type=os_type,
                random_choice=True
            )
            logger.info(f"No OS profile specified, using random selection: {selected_profile}")
        
        # Configure pool location strategy
        if random_pool_strategy:
            self.choose_pool_location_strategies(random_choice=True)
            logger.info("Using random pool location strategy")
        elif pool_strategy:
            self.choose_pool_location_strategies(
                pool_location_strategie=pool_strategy, 
                random_choice=False
            )
            logger.info(f"Using specific pool strategy: {pool_strategy}")
        else:
            self.choose_pool_location_strategies(random_choice=True)
            logger.info("No pool strategy specified, using random selection")
        
        # Set CPU and RAM
        self.send_data_to_cpu_input(cpu_param=cpu_param)
        self.send_data_to_ram_input(ram_param=ram_param)

        # Configure vCPU class
        if random_vcpu_class:
            self.choose_vCPU_class_via_dropdown(random_choice=True)
            logger.info("Using random vCPU class selection")
        elif vcpu_class:
            self.choose_vCPU_class_via_dropdown(
                vCPU_class=vcpu_class, 
                random_choice=False
            )
            logger.info(f"Using specific vCPU class: {vcpu_class}")
        else:
            self.choose_vCPU_class_via_dropdown(random_choice=True)
            logger.info("No vCPU class specified, using random selection")
        
        # Configure boot media
        if random_boot_media:
            self.choose_boot_media_via_dropdown(random_choice=True)
            logger.info("Using random boot media selection")
        elif boot_media:
            self.choose_boot_media_via_dropdown(
                boot_media=boot_media, 
                random_choice=False
            )
            logger.info(f"Using specific boot media: {boot_media}")
        else: 
            self.choose_boot_media_via_dropdown(random_choice=True)
            logger.info("No boot media specified, using random selection")
        
        self.check_go_to_disks_button_enabled()
        self.check_cancel_template_button_enabled()
        self.check_go_to_disks_button_click()
        
        # Step 2/4: Disks Configuration
        logger.info("Step 2/4: Disks Configuration")
        self.check_template_next_step_to_network_button_disabled()
        self.check_back_to_general_step_button_enabled()
        
        # Configure first disk (required)
        self.send_data_to_disk_name_input(disk_count='disk_name1', disk_name=disk_name)
        self.check_first_disk_slot_disabled()
        self.send_data_to_disk_size_input(disk_count='disk1', disk_param=disk_size)
        self.check_first_sector_size_disabled()
        
        self.send_data_to_template_mpbs_input(mbps_param=mbps_param)
        self.send_data_to_template_iop_input(iops_param=iops_param)
        
        # ADDITIONAL DISKS LOGIC 
        # Disk 2
        if all([additional_disk2_name, additional_disk2_size]):
            logger.info(f"Adding disk 2: {additional_disk2_name}")
            self.click_add_new_disk_button()
            self.send_data_to_disk_name_input(disk_count='disk_name2', disk_name=additional_disk2_name)
            self.send_data_to_disk_size_input(disk_count='disk2', disk_param=additional_disk2_size)
            self.check_specific_disk_slot_enabled(disk_count='disk_slot2')
            
            if additional_disk2_sector_size:
                self.choose_sector_size(
                    disk_count='disk_slot2',
                    disk_slot_size=additional_disk2_sector_size,
                    random_disk=False,
                    random_sector=False
                )
                logger.info(f"Using specific sector size for disk 2: {additional_disk2_sector_size}")
            else:
                self.choose_sector_size(
                    disk_count='disk_slot2', 
                    disk_slot_size=None,
                    random_disk=False,
                    random_sector=True
                )
                logger.info("Using random sector size for disk 2")
                
            logger.info(f"Successfully added disk 2: {additional_disk2_name}")
        else:
            logger.info("No disk 2 to add - both disk name and size are required")
        
        # Disk 3
        if all([additional_disk3_name, additional_disk3_size]):
            logger.info(f"Adding disk 3: {additional_disk3_name}")
            self.click_add_new_disk_button()
            self.send_data_to_disk_name_input(disk_count='disk_name3', disk_name=additional_disk3_name)
            self.send_data_to_disk_size_input(disk_count='disk3', disk_param=additional_disk3_size)
            self.check_specific_disk_slot_enabled(disk_count='disk_slot3')
            
            if additional_disk3_sector_size:
                self.choose_sector_size(
                    disk_count='disk_slot3',
                    disk_slot_size=additional_disk3_sector_size,
                    random_disk=False,
                    random_sector=False
                )
                logger.info(f"Using specific sector size for disk 3: {additional_disk3_sector_size}")
            else:
                self.choose_sector_size(
                    disk_count='disk_slot3', 
                    disk_slot_size=None,
                    random_disk=False,
                    random_sector=True
                )
                logger.info("Using random sector size for disk 3")
                
            logger.info(f"Successfully added disk 3: {additional_disk3_name}")
        else:
            logger.info("No disk 3 to add - both disk name and size are required")
        
        # Disk 4
        if all([additional_disk4_name, additional_disk4_size]):
            logger.info(f"Adding disk 4: {additional_disk4_name}")
            self.click_add_new_disk_button()
            self.send_data_to_disk_name_input(disk_count='disk_name4', disk_name=additional_disk4_name)
            self.send_data_to_disk_size_input(disk_count='disk4', disk_param=additional_disk4_size)
            self.check_specific_disk_slot_enabled(disk_count='disk_slot4')
            
            if additional_disk4_sector_size:
                self.choose_sector_size(
                    disk_count='disk_slot4',
                    disk_slot_size=additional_disk4_sector_size,
                    random_disk=False,
                    random_sector=False
                )
                logger.info(f"Using specific sector size for disk 4: {additional_disk4_sector_size}")
            else:
                self.choose_sector_size(
                    disk_count='disk_slot4', 
                    disk_slot_size=None,
                    random_disk=False,
                    random_sector=True
                )
                logger.info("Using random sector size for disk 4")
                
            logger.info(f"Successfully added disk 4: {additional_disk4_name}")
        else:
            logger.info("No disk 4 to add - both disk name and size are required")
        
        # Disk 5
        if all([additional_disk5_name, additional_disk5_size]):
            logger.info(f"Adding disk 5: {additional_disk5_name}")
            self.click_add_new_disk_button()
            self.send_data_to_disk_name_input(disk_count='disk_name5', disk_name=additional_disk5_name)
            self.send_data_to_disk_size_input(disk_count='disk5', disk_param=additional_disk5_size)
            self.check_specific_disk_slot_enabled(disk_count='disk_slot5')
            
            if additional_disk5_sector_size:
                self.choose_sector_size(
                    disk_count='disk_slot5',
                    disk_slot_size=additional_disk5_sector_size,
                    random_disk=False,
                    random_sector=False
                )
                logger.info(f"Using specific sector size for disk 5: {additional_disk5_sector_size}")
            else:
                self.choose_sector_size(
                    disk_count='disk_slot5', 
                    disk_slot_size=None,
                    random_disk=False,
                    random_sector=True
                )
                logger.info("Using random sector size for disk 5")
                
            logger.info(f"Successfully added disk 5: {additional_disk5_name}")
        else:
            logger.info("No disk 5 to add - both disk name and size are required")
        
        self.check_back_to_general_step_button_enabled()
        self.check_template_next_step_to_network_button_enabled()
        self.click_template_next_step_to_network_button()
        
        # Step 3/4: Networks Configuration
        logger.info("Proceeding to Step 3/4: Networks Configuration")
        self.check_back_to_disks_step_button_enabled()
        self.check_next_to_guest_os_step_button_enabled()
        self.check_cancel_template_button_enabled()
        
        self.send_data_to_networks_mbps_limit_nput(mbps_param=mbps_param)
        
        self.check_back_to_disks_step_button_enabled()
        self.check_next_to_guest_os_step_button_enabled()
        self.click_next_to_guest_os_step_button()
        
        # Step 4/4: Guest OS Customization
        logger.info("Proceeding to Step 4/4: Guest OS Customization")
        self.check_cancel_template_button_enabled()
        self.check_back_to_networks_step_button_enabled()
        
        # Configure search domain (resolver)
        self.send_data_to_search_resolver_input(resolver=resolver_data)
        
        # Configure DNS settings
        self.check_add_server_button_enabled()
        self.send_data_to_name_server_input(
            dns_server_count="0",
            dns_server_data=VariablesNames.DNS_SERVER_DATA0
        )
        self.click_add_server_button()
        self.send_data_to_name_server_input(
            dns_server_count="1", 
            dns_server_data=VariablesNames.DNS_SERVER_DATA1
        )        
        self.check_back_to_networks_step_button_enabled()
        self.check_create_template_button_enabled()
        self.check_cancel_template_button_enabled()
        self.click_create_template_button_button()            
                        
