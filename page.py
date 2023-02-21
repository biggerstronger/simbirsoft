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
        select_element = self.find_element(locator=PageLocators.CUSTOMER_SELECT)
        select = Select(select_element)
        select.select_by_index(2)

    def deposit(self, amount: str) -> None:
        self.check_element_appears("Amount to be Deposited :")
        input_field = self.find_element(locator=PageLocators.INPUT_FIELD)
        input_field.send_keys(amount)  # noqa
        input_field.send_keys(Keys.RETURN)  # noqa

    def withdrawal(self, amount: str) -> None:
        self.check_element_appears("Amount to be Withdrawn :")
        input_field = self.find_element(locator=PageLocators.INPUT_FIELD)
        input_field.send_keys(amount)  # noqa
        input_field.send_keys(Keys.RETURN)  # noqa
        self.check_element_appears("Transaction successful")

    def transactions(self) -> any:
        first = self.find_element(locator=PageLocators.TRANSACTION_ONE)
        second = self.find_element(locator=PageLocators.TRANSACTION_TWO)
        self._create_csv(first, second)
        return first, second

    @staticmethod
    def _create_csv(first_t, second_t):
        first_t = first_t.text.replace(",", "").split(" ")  # noqa
        second_t = second_t.text.replace(",", "").split(" ")  # noqa
        first_transaction = [" ".join([first_t[1], first_t[0], first_t[2]]), first_t[3], first_t[5], first_t[6]]
        second_transaction = [" ".join([second_t[1], second_t[0], second_t[2]]), second_t[3], second_t[5], second_t[6]]
        with open('transactions.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(first_transaction)
            writer.writerow(second_transaction)
        allure.attach.file(os.path.abspath("transactions.csv"), attachment_type=allure.attachment_type.CSV)

    @staticmethod
    def find_fibonacci_number() -> str:
        """
                Этот пункт можно посчитать и обычной рекурсией, но в таком случае в метод придется передавать day,
                вместо day + 1, что несколько противоречит условиям ТЗ

                Классический рекурсивный алгоритм:

                def fibonacci(day):
                    if day == 0:
                        return 0
                    elif day == 1 or day == 2:
                        return 1
                    else:
                        return fibonacci(day - 1) + fibonacci(day - 2)
        """
        day = datetime.datetime.now().day + 1
        if day == 1:
            sequence = [0]
        else:
            sequence = [0, 1]
            for i in range(1, day - 1):
                sequence.append(sequence[i - 1] + sequence[i])
        return str(sequence[-1])
