import pytest
import os
import time
from config import ObjectsID
from pages.login_page import LoginPage
from tools.allure.allure_tags import AllureTags
from tools.logger.context_manager import handle_failure_with_log_and_screenshot
from pages.vspace_page import VspacePage
from pages.vdi_overview_page import VdiOverviewPage
from tools.random_value_generator import name_generator
from tools.logger.logger import get_logger
from tools.cleanup import CleanupManager
import allure

logger = get_logger("vSpace")


USERNAME_VDI_OWNER = os.getenv('USERNAME_VDI_OWNER')
PASSWORD_VDI_OWNER = os.getenv('PASSWORD_VDI_OWNER')

USERNAME_VDI_MASTER = os.getenv('USERNAME_VDI_MASTER')
PASSWORD_VDI_MASTER = os.getenv('PASSWORD_VDI_MASTER')

USERNAME_VDI_ADMIN = os.getenv('USERNAME_VDI_ADMIN')
PASSWORD_VDI_ADMIN = os.getenv('PASSWORD_VDI_ADMIN')

USERNAME_VDI_VSPACE_ADMIN = os.getenv('USERNAME_vspace_Admin')
PASSWORD_VDI_VSPACE_ADMIN = os.getenv('PASSWORD_vspace_Admin')

USERNAME_VDI_VSPACE_USER = os.getenv('USERNAME_vspace_user')
PASSWORD_VDI_VSPACE_USER = os.getenv('PASSWORD_vspace_user')

USERNAME_VDI_DESKTOP_VIEWER = os.getenv('USERNAME_Desktop_Viewer')
PASSWORD_VDI_DESKTOP_VIEWER = os.getenv('PASSWORD_Desktop_Viewer')

URL_VDI_AUTH = os.getenv('APP_URL')


VSPACE_CREATOR_ROLES = [
    (USERNAME_VDI_OWNER, PASSWORD_VDI_OWNER, "VDI Owner"),
    (USERNAME_VDI_MASTER, PASSWORD_VDI_MASTER, "VDI Master"),
    (USERNAME_VDI_ADMIN, PASSWORD_VDI_ADMIN, "VDI Admin")
]


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.vspace
@allure.tag(AllureTags.VSPACE_MANAGEMENT)
@allure.story("vSpace Lifecycle Management") 
class TestvSpace:
    
    @pytest.mark.parametrize("username,password,role_name", VSPACE_CREATOR_ROLES)
    @allure.description("""
    This test verifies floating vSpace management operations for different user roles.
    Test steps include:
    1. Creating a floating vSpace with automated deployment
    2. Assigning a template to the floating vSpace
    3. Validating template assignment restrictions (only one template allowed)
    4. Verifying floating instance presence after deployment
    """)
    def test_floating_vspace_by_user_role(
        self,
        login_page: LoginPage,
        vspace_page: VspacePage,
        vdi_overview_page: VdiOverviewPage,
        username: str,
        password: str,
        role_name: str,
    ):
        
        vspace_name = name_generator.generate_object_name()
        qpoints_usage = name_generator.generate_int_as_string(min_value=1, max_value=1000) 
        vspace_description = f'vSpace_description - {name_generator.generate_object_name()}'
        qpoints_usage_current = '0'
        qpoint_current = '0'
        
        try:     
            with allure.step(f"Authenticate as {role_name} and navigate to vSpace management"):
                login_page.visit(URL_VDI_AUTH)
                login_page.check_login_form_componets()
                login_page.login(
                    username=username,
                    password=password
                )
                
            with allure.step("Access vSpace"):
                vdi_overview_page.sidebar.click_vdi_main_menu()
                vdi_overview_page.sidebar.click_all_vSpaces()
                vdi_overview_page.tables.check_visible()
            
            with allure.step("Initiate vSpace creation"):
                vdi_overview_page.tables.click_actions_button()
            
            with allure.step(f"Create floating vSpace '{vspace_name}' with automated deployment"):
                vspace_page.create_vspace(vspace_name=vspace_name, 
                                        qpoints_usage=qpoints_usage,
                                        description=vspace_description,
                                        deploy_type="Automated",
                                        provision_type="Floating", 
                                        standby_count="5", 
                                        inactive_timeout="15")

            with allure.step("Verify successful vSpace creation"):
                vdi_overview_page.alerts.check_success_alert_visible()   
                vdi_overview_page.log.get_log_message() 
                vspace_page.page_vspace_template_absence_message_text.check_visible()
            
            with allure.step("Navigate to template assignment section"):
                vspace_page.page_vspace_template_assign_invspace_button.click()
                vspace_page.page_vspace_template_assign_confirm_button.check_disabled()
                vspace_page.page_vspace_template_assign_cancel_button.check_enabled()
                
            with allure.step("Validate single template assignment restriction"):    
                vspace_page.check_template_to_assign(template_id=ObjectsID.template_Ubuntu_id)
                vspace_page.check_template_not_checked(template_id=ObjectsID.template_Windows_id)
                vspace_page.check_template_to_assign(template_id=ObjectsID.template_Windows_id)
                vspace_page.check_template_not_checked(template_id=ObjectsID.template_Ubuntu_id)
                vspace_page.check_template_to_assign(template_id=ObjectsID.template_Ubuntu_id)
                vspace_page.page_vspace_template_assign_confirm_button.check_enabled()
                vspace_page.page_vspace_template_assign_cancel_button.check_enabled()
                
            with allure.step("Confirm template assignment"):
                vspace_page.page_vspace_template_assign_confirm_button.click()
                vdi_overview_page.log.get_log_message() 
                
            # with allure.step("Check desktop status"):      
                # vspace_page.page_vspace_desktop_awaiting_message_text.wait_for_selector()
                # vspace_page.page_vspace_desktop_awaiting_message_text.wait_for_selector(state="hidden", timeout=180000)
                
            with allure.step("Verify floating instance deployment completion"):     
                vdi_overview_page.sidebar.open_last_desktop_container_from_main_tree()
                time.sleep(60)
                vdi_overview_page.sidebar.page_component_sidebar_desktop_floating_instance.wait_for_selector()
                    
                
        finally:
            if vspace_name:
                with allure.step(f"Execute cleanup for vSpace '{vspace_name}' created by {role_name}"):
                    with handle_failure_with_log_and_screenshot(vdi_overview_page):
                        logger.info(f"Initiating cleanup for vSpace: {vspace_name} created by {role_name}")
                        CleanupManager.cleanup_vpace([vspace_name], vdi_overview_page)
                        logger.info(f"Cleanup completed for vSpace: {vspace_name}")
