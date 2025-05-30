from selenium import webdriver
import pytest
from home_page import HomePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("keyword", ["Python", "Java"])
def test_case_one(driver, keyword):
    page = HomePage(driver)

    page.navigate_to_url("https://www.epam.com")  # navigate to home page
    page.click_careers_link()  # click on careers
    page.input_keyword(keyword)  # fill in keywords into the keyword field on careers website
    page.select_all_locations()  # set location option to all locations
    page.select_remote()  # clicks on checkbox for the remote option
    page.find_open_positions()  # perform job search by clicking on find button
    page.open_latest_job() # clicks on the latest job position to see the details

    assert page.keyword_in_page(keyword) == True #Validate that the programming language mentioned in the step above is on a page

@pytest.mark.parametrize("keyword", ["BLOCKCHAIN", "CLOUD", "Automation"])
def test_case_two(driver, keyword):
    page = HomePage(driver)

    page.navigate_to_url("https://www.epam.com") #navigate to home page
    page.click_search_icon() # click on magnifier icon
    page.input_search_keyword(keyword) # search the keyword on the page
    page.click_find_button() # clicks on find button

    assert page.keyword_in_page(keyword) == True