from typing import List, Any, Dict

from allure_commons._allure import step
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wisebits_qa_automation_task.allocators.try_sql_allocators import TrySqlAllocators


class TrySqlPage:

    def __init__(
            self,
            webdriver: WebDriver,
            path: str="https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
    ):
        webdriver.get(url=path)
        self.webdriver = webdriver

    @step("try_sql_page: set_sql_statemnt {sql_request}")
    def set_sql_statement(self, sql_request: str):
        element: WebElement = WebDriverWait(self.webdriver, 10).until(
            expected_conditions.presence_of_element_located(TrySqlAllocators.SET_STATEMENTS.value)
        )
        actions = ActionChains(self.webdriver)
        for i in range(len(element.text) + 1):
            actions.key_down(Keys.BACKSPACE)
        actions.perform()
        actions.click(element).perform()
        actions.send_keys(sql_request).perform()

    @step("try_sql_page: press_button_run_sql")
    def press_button_run_sql(self):
        element: WebElement = WebDriverWait(self.webdriver, 10).until(
            expected_conditions.presence_of_element_located(TrySqlAllocators.BUTTON_RUN_SQL.value)
        )
        element.click()

    @step("try_sql_page: get result table")
    def get_result(self) -> List[Dict[Any, Any]]:
        element: WebElement = WebDriverWait(self.webdriver, 10).until(
            expected_conditions.presence_of_element_located(TrySqlAllocators.GET_RESULT.value)
        )

        rows = element.find_elements_by_xpath('//*[@id="divResultSQL"]/div/table/tbody/tr')
        fields_element = rows[0]

        table = []
        fields_name = []
        for field_elem in fields_element.find_elements_by_xpath("./th"):
            fields_name.append(field_elem.text)

        for row_element in rows[1:]:
            row = {}
            for count, row_cells in enumerate(row_element.find_elements_by_xpath("./td")):
                row[fields_name[count]] = row_cells.text
            table.append(row)

        return table
