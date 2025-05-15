import pytest
from home_page import HomePage
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password, expected", [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "error"),
    ("problem_user", "secret_sauce", "success"),
    ("performance_glitch_user", "secret_sauce", "success"),
    ("error_user", "secret_sauce", "success"),
    ("visual_user", "secret_sauce", "success"),
])
def test_login(driver, username, password, expected):
    page = HomePage(driver)
    page.navigate_to_url("https://www.saucedemo.com/") # navigates to the website
    page.user_login(username, password) # logs into website

    if expected == "success":
        assert page.check_title() == "Products" # checks that we arrived at the proper page
    elif expected == "error":
        assert page.error_message() == True # asserts if the error message is displayed

@pytest.mark.parametrize("username,password, n_items, expected_total", [
    ("standard_user", "secret_sauce", 1, 32.39),
    ("standard_user", "secret_sauce", 2, 43.18),
    ("standard_user", "secret_sauce", 3, 60.45),
])
def test_shopping_cart(driver, username, password, n_items, expected_total):
    page = HomePage(driver)
    page.navigate_to_url("https://www.saucedemo.com/")  # navigates to the website
    page.user_login(username, password)  # logs into website

    cart = page.add_item_to_cart(n_items) # adds n items to the cart

    page.navigate_to_cart()

    assert page.items_in_cart(cart) == True # Check the right items were added to the cart

    page.navigate_to_checkout()

    assert page.cart_total() == expected_total # Checks that the total displayed at the page matches the expected total

    assert page.complete_purchase() == True # Checks that the completed purchase message is displayed