import allure

from selenium import webdriver

from locators import PageLocators
from page import MainPage


@allure.story("Test all cases")
def test_all():
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities={
            "browserName": "firefox",
        }
    )
    locators = PageLocators()
    page_object = MainPage(driver)
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
    page_object.driver.close()
