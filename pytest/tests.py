import pytest
from home_page import HomePage
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [("someuser2", "afkpc123")])
def test_login(driver, username, password):
    page = HomePage(driver)

    page.navigate_to_homepage() # navigates to demoblaze website
    page.click_login_link()  # clicks on login link

    assert page.login_fields_presence() == True # checks that both fields are present

    page.submit_login_form(username, password)  # logs into the website

    assert page.check_login_message(username) == True # asserts that we got the welcome message

@pytest.mark.parametrize("username, password, product_name, product_price", [("someuser2", "afkpc123", "Apple monitor 24", 400)])
def test_shopping_cart(driver, username, password, product_name, product_price):
    page = HomePage(driver)

    page.navigate_to_homepage()  # navigates to demoblaze website
    page.click_login_link() # clicks on login link
    page.submit_login_form(username, password)  # logs into the website
    page.navigate_to_monitors_page() # navigates to monitors page
    name, price = page.click_highest_price_monitor() # selects on the monitor with the highest price

    assert name == product_name and price == product_price # here im supposed to assert that we got to the right page

    page.add_monitor_to_cart() # adds the monitor with the highest price to the cart
    name, price = page.navigate_to_cart() # navigates to cart page

    assert name == product_name and price == product_price # here im supposed to assert that the monitor was added to the cart