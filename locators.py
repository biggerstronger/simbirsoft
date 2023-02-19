import dataclasses
from selenium.webdriver.common.by import By


@dataclasses.dataclass
class PageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//button[text()="Customer Login"]')
    CUSTOMER_SELECT = (By.ID, 'userSelect')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Login"]')
    DEPOSIT_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]')
    WITHDRAWAL_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[3]')
    INPUT_FIELD = (By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    TRANSACTION_BUTTON = (By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]')
    TRANSACTION_ONE = (By.XPATH, '//*[@id="anchor0"]')
    TRANSACTION_TWO = (By.XPATH, '//*[@id="anchor1"]')
