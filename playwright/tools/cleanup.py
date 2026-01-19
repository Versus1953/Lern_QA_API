
from playwright.sync_api import Page, expect
from pages.user_and_role_page import UserAndRolePage
from pages.vdi_overview_page import VdiOverviewPage
from pages.template_page import TemplatePage
from pages.vspace_page import VspacePage
from pages.desktop_page import DesktopPage
from tools.logger.logger import get_logger
import traceback
import os
import time

logger = get_logger("Cleanup_Manager")

# Environment variables
USERNAME_VDI_OWNER = os.getenv('USERNAME_VDI_OWNER')
PASSWORD_VDI_OWNER = os.getenv('PASSWORD_VDI_OWNER')
URL_VDI_AUTH = os.getenv('APP_URL')
WINDOWS_TEMP="Windows medium"
LINUX_TEMP="Ubuntu+Agent"

class CleanupManager:
    """Class for cleanup operations."""

    @staticmethod
    def _perform_cleanup(
        object_name: str, 
        objects: list[str], 
        vdi_overview_page: VdiOverviewPage, 
        page_to_use, 
        cleanup_function
    ):
        """Helper function to perform cleanup operations."""
        for obj in objects:
            try:
                logger.info(f"Attempting to cleanup {object_name}: {obj}")
                cleanup_function(vdi_overview_page, page_to_use, obj)
                logger.info(f"Successfully cleaned up {object_name}: {obj}")
            except Exception as e:
                error_msg = f"Failed to cleanup {object_name} {obj}: {e}"
                tb_str = traceback.format_exc()
                logger.error(error_msg) 
                logger.error(tb_str)
                logger.error(e) 
                          
                raise RuntimeError(error_msg) from e

    @staticmethod
    def _cleanup_user(vdi_overview_page: VdiOverviewPage, user_and_role_page: UserAndRolePage, username: str):
        """Cleanup a user."""
        try:
            vdi_overview_page.sidebar.click_menu_icon_users_and_roles()
        except:
            vdi_overview_page.sidebar.click_vdi_main_menu()
            vdi_overview_page.sidebar.click_menu_icon_users_and_roles()
          
        user_and_role_page.check_usersandrole_elements_presence()
        user_and_role_page.click_user_section_in_table()
        vdi_overview_page.tables.send_data_to_table_search_input(username)
        time.sleep(2)        
        user_and_role_page.assert_user_in_table(username, "cell-value")
        user_and_role_page.click_user_in_table(username)
        user_and_role_page.check_user_action_list(has_roles_assigned=True)
        user_and_role_page.click_user_remove_button()
        vdi_overview_page.modals.click_approve_button()
        
        vdi_overview_page.alerts.check_success_alert_visible()
        vdi_overview_page.log.get_log_message()
        vdi_overview_page.tables.send_data_to_table_search_input(username)
        user_and_role_page.assert_user_not_in_table(username, "cell-value")

    @staticmethod
    def cleanup_users(usernames: list[str], vdi_overview_page: VdiOverviewPage):
        """Cleanup multiple users."""
        user_and_role_page = UserAndRolePage(vdi_overview_page.page)
        CleanupManager._perform_cleanup(
            "user", 
            usernames, 
            vdi_overview_page, 
            user_and_role_page, 
            CleanupManager._cleanup_user
        )

    @staticmethod
    def _cleanup_vspace(vdi_overview_page: VdiOverviewPage, vspace_page: VspacePage, vspace: str):
        """Cleanup a vspace."""
        # vdi_overview_page.sidebar.click_vdi_main_menu()
        try:
            vdi_overview_page.sidebar.click_all_vSpaces()
        except:   
            pass         
        vdi_overview_page.tables.check_visible()
        vdi_overview_page.tables.send_data_to_table_search_input(vspace)
        time.sleep(2)
        vdi_overview_page.tables.click_dots_dropdown()
        vspace_page.click_delete_vspace_button_in_general_table()
        vdi_overview_page.modals.check_approve_button_enabled()
        vdi_overview_page.modals.check_cancel_button_enabled()
        vdi_overview_page.modals.check_confirmation_window_remove_vspace_text()
        vdi_overview_page.modals.click_approve_button()
        vdi_overview_page.alerts.check_success_alert_visible()
        vdi_overview_page.log.get_log_message()
        vdi_overview_page.tables.send_data_to_table_search_input(vspace)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=vspace)

    @staticmethod
    def cleanup_vpace(vspaces: list[str], vdi_overview_page: VdiOverviewPage):
        """Cleanup multiple vspaces."""
        vspace_page = VspacePage(vdi_overview_page.page)
        CleanupManager._perform_cleanup(
            "vspace", 
            vspaces, 
            vdi_overview_page, 
            vspace_page, 
            CleanupManager._cleanup_vspace
        )

    @staticmethod
    def _cleanup_desktop(vdi_overview_page: VdiOverviewPage, desktop_page: DesktopPage, desktop: str):
        """Cleanup a desktop."""
               
        # vdi_overview_page.sidebar.click_vdi_main_menu()
        try:
            vdi_overview_page.sidebar.click_all_virtual_desktops()
        except:
            vdi_overview_page.sidebar.click_vdi_main_menu()
            vdi_overview_page.sidebar.click_all_virtual_desktops()
            
        vdi_overview_page.tables.check_table_search_input_visible()
        vdi_overview_page.tables.send_data_to_table_search_input(desktop)
        time.sleep(2)
        vdi_overview_page.tables.click_dots_dropdown()
        desktop_page.click_desktop_delete_button()
        vdi_overview_page.modals.check_approve_button_enabled()
        vdi_overview_page.modals.check_cancel_button_enabled()
        vdi_overview_page.modals.check_confirmation_window_remove_desktop_text()
        vdi_overview_page.modals.click_approve_button()
        vdi_overview_page.alerts.check_success_alert_visible()
        vdi_overview_page.log.get_log_message()
        vdi_overview_page.tables.send_data_to_table_search_input(desktop)
        time.sleep(1)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=desktop)
                

    @staticmethod
    def cleanup_desktop(desktops: list[str], vdi_overview_page: VdiOverviewPage):
        """Cleanup multiple desktops."""
        desktop_page = DesktopPage(vdi_overview_page.page)
        CleanupManager._perform_cleanup(
            "desktop", 
            desktops, 
            vdi_overview_page, 
            desktop_page, 
            CleanupManager._cleanup_desktop
        )
        
    # @staticmethod
    # def _cleanup_template(vdi_overview_page: VdiOverviewPage, template: str):
    #     """Cleanup a template"""
        
    #     if  vdi_overview_page.tables.check_table_search_input_visible():            
    #         vdi_overview_page.tables.send_data_to_table_search_input(template)
    #         vdi_overview_page.tables.click_dots_dropdown()
    #         vdi_overview_page.tables.check_table_object_presence_in_table(object_name=template)
    #         vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=WINDOWS_TEMP)
    #         vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=LINUX_TEMP) 
    #         vdi_overview_page.tables.click_remove_button()                               
    #         vdi_overview_page.modals.check_approve_button_enabled()
    #         vdi_overview_page.modals.check_cancel_button_enabled()
    #         vdi_overview_page.modals.check_confirmation_window_remove_template_text()
    #         vdi_overview_page.modals.click_approve_button()
    #         vdi_overview_page.alerts.check_success_alert_visible()
    #         vdi_overview_page.log.get_log_message()
    #         vdi_overview_page.tables.send_data_to_table_search_input(template)
    #         vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=template)
            

    # @staticmethod
    # def cleanup_template(templates: list[str], vdi_overview_page: VdiOverviewPage):
    #     """Cleanup multiple desktops."""
    #     template_page = TemplatePage(vdi_overview_page.page)
    #     CleanupManager._perform_cleanup(
    #         "template", 
    #         templates, 
    #         vdi_overview_page, 
    #         template_page, 
    #         CleanupManager._cleanup_template
    #     )
        
    @staticmethod
    def _cleanup_template(vdi_overview_page: VdiOverviewPage, template_page: TemplatePage, template: str):
        """Cleanup a template."""
        vdi_overview_page.sidebar.click_vdi_main_menu()
        try:
            vdi_overview_page.sidebar.click_menu_icon_templates()
        except:
            pass
        vdi_overview_page.tables.check_visible()
        vdi_overview_page.tables.send_data_to_table_search_input(template)
        vdi_overview_page.tables.check_table_object_presence_in_table(object_name=template)
        time.sleep(2)
        # vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=WINDOWS_TEMP)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=LINUX_TEMP)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=WINDOWS_TEMP)
        vdi_overview_page.tables.click_remove_button()                            
        vdi_overview_page.modals.check_approve_button_enabled()
        vdi_overview_page.modals.check_cancel_button_enabled()
        vdi_overview_page.modals.check_confirmation_window_remove_template_text()
        vdi_overview_page.modals.click_approve_button()
        vdi_overview_page.alerts.check_success_alert_visible()
        vdi_overview_page.log.get_log_message()
        vdi_overview_page.tables.send_data_to_table_search_input(template)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=template)
        
    

    @staticmethod
    def cleanup_template(templates: list[str], vdi_overview_page: VdiOverviewPage):
        """Cleanup multiple vspaces."""
        template_page = VspacePage(vdi_overview_page.page)
        CleanupManager._perform_cleanup(
            "template", 
            templates, 
            vdi_overview_page, 
            template_page, 
            CleanupManager._cleanup_template
        )
        
    @staticmethod
    def _cleanup_roles(vdi_overview_page: VdiOverviewPage, user_and_role_page: UserAndRolePage, role: str):
        """Cleanup a role."""
        vdi_overview_page.sidebar.click_vdi_main_menu()
        try:
            vdi_overview_page.sidebar.click_menu_icon_users_and_roles()
        except:
            pass
        user_and_role_page.check_usersandrole_elements_presence()
        user_and_role_page.click_role_section_in_table()
        vdi_overview_page.tables.send_data_to_table_search_input(role)
        time.sleep(2)
        vdi_overview_page.tables.click_dots_dropdown()
        user_and_role_page.click_role_remove_button()
        vdi_overview_page.modals.check_approve_button_enabled()
        vdi_overview_page.modals.check_cancel_button_enabled()
        user_and_role_page.check_revoke_checkbox_option()
        vdi_overview_page.modals.click_approve_button()        
        vdi_overview_page.alerts.check_success_alert_visible()
        vdi_overview_page.log.get_log_message()
        vdi_overview_page.tables.send_data_to_table_search_input(role)
        vdi_overview_page.tables.check_table_object_presence_not_in_table(object_name=role)
    @staticmethod
    def cleanup_roles(roles: list[str], vdi_overview_page: VdiOverviewPage):
        """Cleanup multiple roles."""
        user_and_role_page = UserAndRolePage(vdi_overview_page.page)
        CleanupManager._perform_cleanup(
            "role", 
            roles, 
            vdi_overview_page, 
            user_and_role_page, 
            CleanupManager._cleanup_roles
        )
