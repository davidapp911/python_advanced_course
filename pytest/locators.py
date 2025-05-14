from selenium.webdriver.common.by import By


class Locators:
    LOGIN_LINK = (By.ID, "login2")
    MODAL = (By.ID, "logInModal")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGIN_MESSAGE = (By.ID, "nameofuser")
    MONITOR_LINK = (By.LINK_TEXT, "Monitors")
    MONITOR_ROW = (By.ID, "tbodyid")
    MONITOR_CARD = (By.XPATH, "//div[contains(@class, 'card') and contains(@class, 'h100')]")