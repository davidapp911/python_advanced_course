from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.demoblaze.com/")

    def click_login_link(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.LOGIN_LINK)
        ).click()

        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(Locators.MODAL)
        )

    def login_fields_presence(self):
        username = self.driver.find_element(*Locators.USERNAME_INPUT)
        password = self.driver.find_element(*Locators.PASSWORD_INPUT)

        return username.is_displayed() and password.is_displayed() and username.is_enabled() and password.is_enabled()

    def submit_login_form(self, username, password):
        self.driver.find_element(*Locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        sleep(1)

    def check_login_message(self, username):
        login_message = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.LOGIN_MESSAGE)
        )

        return login_message.text == f"Welcome {username}"

    def navigate_to_monitors_page(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.MONITORS_LINK)
        ).click()

        sleep(2)

    def click_highest_price_monitor(self):
        monitors_row = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.MONITOR_ROW)
        )

        monitors = WebDriverWait(monitors_row, 10).until(
            ec.presence_of_all_elements_located(Locators.MONITOR_CARD)
        )

        product_name = ""
        highest_price = 0
        expensive_monitor = ""

        for monitor in monitors:
            price = monitor.find_element(*Locators.MONITOR_PRICE).text
            price = int(price.replace("$", ""))

            if price > highest_price:
                highest_price = price
                expensive_monitor = monitor
                product_name = monitor.find_element(*Locators.MONITOR_LINK).text

        expensive_monitor.click()

        return product_name, highest_price

    def add_monitor_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.CART_BUTTON)
        ).click()

        sleep(2)

        alert = self.driver.switch_to.alert
        alert.accept()

    def navigate_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.CART_LINK)
        ).click()

        cart_entry = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.CART_ENTRY)
        )

        tds = cart_entry.find_elements(*Locators.TDS)

        product_name, product_price = tds[1].text, int(tds[2].text)

        return product_name, product_price