import dataclasses
from selenium.webdriver.common.by import By


@dataclasses.dataclass
class PageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//button[text()="Customer Login"]')
    CUSTOMER_SELECT = (By.ID, 'userSelect')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    TRANSACTION_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')
    DEPOSIT_BUTTON = (By.XPATH, '//button[@ng-class="btnClass2"]')
    WITHDRAWAL_BUTTON = (By.XPATH, '//button[@ng-class="btnClass3"]')
    INPUT_FIELD = (By.XPATH, '//div[@class="form-group"]/input')
    TRANSACTION_ONE = (By.XPATH, '//*[@id="anchor0"]')
    TRANSACTION_TWO = (By.XPATH, '//*[@id="anchor1"]')
