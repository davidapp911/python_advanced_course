from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def user_login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.USERNAME_INPUT)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.PASSWORD_INPUT)
        ).send_keys(password)

        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        sleep(5)

    def check_title(self):
        title = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.PAGE_TITLE)
        ).text

        return title

    def error_message(self):
        error = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.ERROR_MESSAGE)
        )

        return error.is_displayed()

    def add_item_to_cart(self, n):
        inventory_list = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(Locators.INVENTORY_ITEM)
        )

        items = []
        for i in range(n):
            name = inventory_list[i].find_element(*Locators.ITEM_NAME).text
            items.append(name)

            inventory_list[i].find_element(*Locators.ADD_TO_CART).click()

        return items

    def navigate_to_cart(self):
        self.driver.find_element(*Locators.SHOPPING_CART).click()

    def items_in_cart(self, items):
        cart_list = self.driver.find_element(*Locators.CART_LIST)

        flag = True

        for item in items:
            if item not in cart_list.text:
                flag = False

        return flag

    def navigate_to_checkout(self):
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()
        self.driver.find_element(*Locators.FIRSTNAME_FIELD).send_keys("John")
        self.driver.find_element(*Locators.LASTNAME_FIELD).send_keys("Doe")
        self.driver.find_element(*Locators.POSTALCODE_FIELD).send_keys("12345")
        self.driver.find_element(*Locators.CONTINUE_BUTTON).click()

    def cart_total(self):
        total = self.driver.find_element(*Locators.TOTAL_LABEL).text
        total = float(total.replace("Total: $", ""))
        return total

    def complete_purchase(self):
        self.driver.find_element(*Locators.FINISH_BUTTON).click()

        message = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.COMPLETED_MESSAGE)
        )

        return message.is_displayed()