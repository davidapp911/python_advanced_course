from selenium.webdriver.common.by import By


class Locators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-button")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART = (By.TAG_NAME, "button")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRSTNAME_FIELD = (By.ID, "first-name")
    LASTNAME_FIELD = (By.ID, "last-name")
    POSTALCODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETED_MESSAGE = (By.CLASS_NAME, "complete-header")