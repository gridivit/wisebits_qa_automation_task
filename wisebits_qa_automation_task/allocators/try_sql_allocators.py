from enum import Enum

from selenium.webdriver.common.by import By


class TrySqlAllocators(Enum):
    SET_STATEMENTS = (By.CSS_SELECTOR, ".CodeMirror")
    BUTTON_RUN_SQL = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/button")
    GET_RESULT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div/div/table')
