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
    page.login(username, password) # logs into the website

    assert page.check_login_message(username) == True

@pytest.mark.parametrize("username, password", [("someuser2", "afkpc123")])
def test_shopping_cart(driver, username, password):
    page = HomePage(driver)

    page.navigate_to_homepage()  # navigates to demoblaze website
    page.login(username, password)  # logs into the website
    page.navigate_to_monitors_page() # navigates to monitors page
    page.click_highest_price_monitor() # selects on the monitor with the highest price