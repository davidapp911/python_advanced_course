from selenium.webdriver.common.by import By


class Locators:
    LOGIN_LINK = (By.ID, "login2")
    MODAL = (By.ID, "logInModal")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    LOGIN_MESSAGE = (By.ID, "nameofuser")
    MONITORS_LINK = (By.LINK_TEXT, "Monitors")
    MONITOR_LINK = (By.CLASS_NAME, "hrefch")
    MONITOR_ROW = (By.ID, "tbodyid")
    MONITOR_CARD = (By.CLASS_NAME, "card")
    MONITOR_PRICE = (By.TAG_NAME, "h5")
    CART_BUTTON = (By.LINK_TEXT, "Add to cart")
    CART_LINK = (By.LINK_TEXT, "Cart")
    CART_ENTRY = (By.CLASS_NAME, "success")
    TDS = (By.TAG_NAME, "td")