from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.demoblaze.com/")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.LOGIN_LINK)
        ).click()

        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(Locators.MODAL)
        )

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
            ec.element_to_be_clickable(Locators.MONITOR_LINK)
        ).click()

    def click_highest_price_monitor(self):
        monitors = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.MONITOR_ROW)
        )