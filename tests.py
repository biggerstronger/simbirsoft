import allure
import pytest

from selenium import webdriver

from locators import PageLocators
from page import MainPage


@pytest.fixture
def setup_firefox():
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities={
            "browserName": "firefox",
        }
    )
    locators = PageLocators()
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    yield driver, locators, url

    driver.close()


def business_logic(driver, locators, url):
    page_object = MainPage(driver, url)
    page_object.get_site()
    page_object.click_button(locator=locators.CUSTOMER_LOGIN_BUTTON)
    page_object.select_customer()
    page_object.click_button(locator=locators.LOGIN_BUTTON)
    calculated_amount = page_object.find_fibonacci_number()
    page_object.click_button(locator=locators.DEPOSIT_BUTTON)
    page_object.deposit(calculated_amount)
    page_object.click_button(locator=locators.WITHDRAWAL_BUTTON)
    page_object.withdrawal(calculated_amount)
    page_object.click_button(locator=locators.TRANSACTION_BUTTON)
    page_object.check_transactions_and_create_csv()


@allure.story("Test Firefox")
def test_firefox(setup_firefox):
    driver, locators, url = setup_firefox
    business_logic(driver, locators, url)
