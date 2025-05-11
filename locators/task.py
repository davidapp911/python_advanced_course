import HomePage
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def test_case_one():
    # options setup needed if script triggers cloudflare
    op = Options()
    op.add_argument("user-data-dir=/Users/davidp/Library/Application Support/Google/Chrome/Default")
    page = HomePage.HomePage(webdriver.Chrome(options=op))

    page.navigate_to_url("https://www.epam.com")  # navigate to home page

    page.click_careers_link()  # click on careers

    page.input_keyword("Python")  # fill in keywords into the keyword field on careers website

    page.select_all_locations()  # set location option to all locations

    page.select_remote()  # clicks on checkbox for the remote option

    page.find_open_positions()  # perform job search by clicking on find button

    page.open_latest_job() # clicks on the latest job position to see the details

    sleep(10)