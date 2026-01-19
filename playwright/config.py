from __future__ import annotations  
from enum import Enum
from typing import Final, List, TypedDict

class VariablesNames():
    VSPACE = 'run_desktop'
    UBUNTU_XRDP_NX_TEMPLATE = 'Ubuntu xrdp & nx middle tttttttttttttt'  #1
    WINDOWS = 'Windows' #2
    UBUNTU_AGENT ="Ubuntu v3"
    Q7 ='44a839bc-6b25-4b77-a277-1b749b617c79'
    Q9 = 'fefa5efe-73c9-11ed-8409-c38eafb91e77'
    DNS_SERVER_DATA0 ="8.8.8.8"
    DNS_SERVER_DATA1 ="8.8.4.4"
    DESKTOP_NAME_00 ='test-import-vl'

  
class AuthUrlPatterns(str, Enum):
    LOGIN_REDIRECT = r'.*/#/auth/'
    VDI_USER_LIST = r".*/#/vdi/users/list"
    VDI_DESKTOP_LIST =r".*/#/vdi/alldesktops"
    VDI_TEMPLATES_LIST =r".*/#/vdi/templates/list"
    VDI_USER_DETAIL_LIST =r".*/vdi/users/detail"
    VDI_ALL_VSPACES_LIST =r".*/vdi/vspace/list"
    VDI_IMPORTABLE_VMS =r".*/vdi/importableVms"
    VDI_AD =r".*/#/vdi/ad/list"


class UiTextPatterns():
    MESSAGE_CHENGE_USER_PASS_SUCCESS = r"(Пользователь.*получил новый пароль|User.*got new password)"
    MESSAGE_APPROVE = r"(Change|Сменить)"
    MESSAGE_CANCEL = r"(Cancel|Отменить)"
    MESSAGE_REDIRECT = r"(Если изменения вступят в силу, вы будете перенаправлены на страницу авторизации|After success you will be redirected to auth page)"
    MESSAGE_DELETE_VSPACE_CONFIRM = r"(Are you sure want to remove vSpace ?|Вы уверены, что хотите удалить рабочее пространство ?)"
    MESSAGE_DELETE_DESKTOP_CONFIRM = r"(?:Are you sure want to remove desktop|Вы уверены, что хотите удалить виртуальный рабочий стол) ([^?]+)\?"
    MESSAGE_CONNECT_DESKTOP_CONFIRM = r"(Вы уверены, что хотите подключиться к рабочему столу.*?|Are you sure want to connect to desktop.*?)"
    MESSAGE_CONNECT_VSPACE_CONFIRM = r"(Вы уверены, что хотите подключиться через рабочее пространство.*?|Are you sure want to connect via floating vSpace.*?)"
    MESSAGE_CONNECT_DESKTOP_CONFIRM_2 = r'(Press "Connect" if you have the app installed or use data below manually:|Нажмите "Соединение", если у вас установлен софт\s+используйте данные для подключения:)'
    MESSAGE_DELETE_TEMPLATE_CONFIRM = r"(?:Are you sure want to delete template|Вы уверены, что хотите удалить шаблон) ([^?]+)\?"
    MESSAGE_USER_CREATED = r".*(User.*id:.*has been created successfully|Был успешно создан пользователь.*id:.*).*"
    MESSAGE_PASSWORD_CHANGED = r".*(User.*password.*changed successfully|Пароль пользователя.*успешно изменен).*"
    MESSAGE_USER_DELETED = r".*(User.*deleted successfully|Пользователь.*успешно удален).*"
    MESSAGE_ROLE_ASSIGNED = r"(Если изменения вступят в силу, вы будете перенаправлены на страницу авторизации|After success you will be redirected to auth page)"
    TEXT_CONFIRMATION_ROLE_ASSIGN_MODAL = r"(Вы уверены, что хотите назначить роль пользователю.*?|Are you sure want to assign a role to user.*?)"
    TEXT_REMOVE_USER_MODAL = r"(Вы уверены, что хотите удалить пользователя.*?|Are you sure want to remove user.*?)"
    TEXT_ROLE_ASSIGNED =  r".*(Получена новая роль|New role assigned)"    
    ROLE_NAME_VDI_OWNER = r"(VDI Infrastructure Owner)"
    CPU_HOVER_TEXT =["Value between 1 and 16 is required","Введите значение от 1 до 16"]
    RAM_HOVER_TEXT =["Value between 1GB and 32GB is required","Введите значение от 1GB до 32GB"]
    DISK_SLOT_HOVER_TEXT =["Slot allows to define disk order","Слот определяет порядковый номер устройства в гостевой ОС"]
    DISK_SIZE_HOVER_TEXT =["Value between 56GB and 2TB is required","Введите значение от 56GB до 2TB"]
    DISK_SECTOR_SIZE_HOVER_TEXT =["Sector Size (physical and logical) for the disk","Размер сектора диска (физический и логический)"]
    DISK_IOPS_LIMIT_HOVER_TEXT =["IOps limit of the disk","IOps лимит диска"]
    DISK_MBPS_LIMIT_HOVER_TEXT =["Throughput limit","Ограничение пропускной способности"]
    QUOTA_USAGE_HOVER_TEXT =["Usage quota","Квота на использование"]
    DATE_TIME_PATTERN = r"(^\d{4}/\d{2}/\d{2} \d{2}:\d{2}$)"
    CREATOR_PROVIDER_TEXT = "local"
    TWOAF_ENABLE_TITILE = r"(Two-factor authentication|Двухфакторная аутентификация)"
    TWOAF_DISABLED_TITILE = r"(Are you sure want to disable two-factor authentication?|Вы уверены, что хотите выключить двухфакторную авторизацию?)"
    TWOAF_INVALID_EMAIL_TEXT =r"(Email не валиден|Email is invalid)"
    TWOAF_WRONG_CODE_MESSAGE =r"(Неверный код. Осталось попыток: 4|Неверный код. Осталось попыток: 4)"
    
    
    
    #Desktop Statuses
    DESKTOP_STATUS_CREATED =r"(Created|Создано)"
    DESKTOP_STATUS_STARTED =r"(Started|Запущено)"
    DESKTOP_STATUS_OFFLINE =r"(Offline|Оффлайн)"
    
    #Desktop Agent Statuses
    DESKTOP_AGENT_STATUS_OFFLINE =r"(Offline|Оффлайн)"

    
    #Desktop Health Statuses
    DESKTOP_HEALTH_STATUS_NORMAL =r"(Normal|Норма)"

  
    # ^\d{4}/ - starts with 4 digits followed by a slash (year)

    # \d{2}/ - 2 digits followed by a slash (month)

    # \d{2} - 2 digits followed by a space (day)

    # \d{2}: - 2 digits followed by a colon (hour)

    # \d{2}$ - 2 digits at the end (minutes)

    
class LogPathPatterns(str, Enum):
    CLUSTER_LOG_PATH = "/var/log/messages"
    ERROR_MARKER = "###"
    EXCLUDE_MARKERS = ["####", "#####"]
    
class ApiMethodsNAmes(str, Enum):
    auth_provider = "auth-providers"
    
class ObjectsID(str):
    vspace_id_00 = '54'
    vspace_id_01 = '3488'
    vspace_name_01 ='run_desktop_floating'
    desktop_id_00 = '6601'
    desktop_id_01 = '740922'
    template_Ubuntu_id = '287'
    template_Windows_id = '370'
    email ='vera.lusheva@vstack.com'
