import csv
import allure
import os.path
import datetime

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from locators import PageLocators
from base_page import BasePage


class MainPage(BasePage):
    def click_button(self, locator: tuple) -> any:
        self.find_element(locator=locator).click()

    def select_customer(self) -> None:
        with allure.step("You are the chosen one, Harry"):
            select_element = self.find_element(locator=PageLocators.CUSTOMER_SELECT)
            select = Select(select_element)
            select.select_by_index(2)
            assert select.first_selected_option.text == "Harry Potter"

    def deposit(self, amount: str) -> None:
        with allure.step("Check if deposit"):
            self.check_element("Amount to be Deposited :")
            assert "Amount to be Deposited :" in self.driver.page_source
        with allure.step("Deposit amount"):
            input_field = self.find_element(locator=PageLocators.INPUT_FIELD)
            input_field.send_keys(amount)  # noqa
            input_field.send_keys(Keys.RETURN)  # noqa
            assert "Deposit Successful" in self.driver.page_source
        with allure.step("Check balance"):
            assert 'Balance : <strong class="ng-binding">{}</strong>'.format(amount) in self.driver.page_source

    def withdrawal(self, amount: str) -> None:
        with allure.step("Check if withdrawal"):
            self.check_element("Amount to be Withdrawn :")
            assert "Amount to be Withdrawn :" in self.driver.page_source
        with allure.step("Withdrawal amount"):
            input_field = self.find_element(locator=PageLocators.INPUT_FIELD)
            input_field.send_keys(amount)  # noqa
            input_field.send_keys(Keys.RETURN)  # noqa
            self.check_element("Transaction successful")
            assert "Transaction successful" in self.driver.page_source
        with allure.step("Check balance is 0"):
            assert 'Balance : <strong class="ng-binding">0</strong>' in self.driver.page_source

    def check_transactions_and_create_csv(self) -> any:
        with allure.step("Check first transaction"):
            first = self.find_element(locator=PageLocators.TRANSACTION_ONE)
            assert first
        with allure.step("Check second transaction"):
            second = self.find_element(locator=PageLocators.TRANSACTION_TWO)
            assert second
        first = first.text.replace(",", "").split(" ")  # noqa
        second = second.text.replace(",", "").split(" ")  # noqa
        first_transaction = [" ".join([first[1], first[0], first[2]]), first[3], first[5], first[6]]
        second_transaction = [" ".join([second[1], second[0], second[2]]), second[3], second[5], second[6]]
        with open('transactions.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(first_transaction)
            writer.writerow(second_transaction)
        allure.attach.file(os.path.abspath("transactions.csv"), attachment_type=allure.attachment_type.CSV)

    @staticmethod
    def find_fibonacci_number() -> str:
        day = datetime.datetime.now().day
        fib_list = [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
        ]
        return str(fib_list[day])
