from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    def find_element(self, locator, time=200) -> any:
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def check_element_appears(self, text, time=10) -> any:
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator=(By.XPATH, f'//*[text()="{text}"]')),
            message=f"Can't find element with text {text}",
        )

    def get_site(self) -> None:
        self.driver.get(self.base_url)
