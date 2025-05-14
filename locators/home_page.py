from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators import Locators
from time import sleep


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_careers_link(self):
        self.driver.find_element(*Locators.CAREERS_LINK).click()

    def input_keyword(self, keyword):
        self.driver.find_element(*Locators.KEYWORDS_INPUT).send_keys(keyword)

    def select_all_locations(self):
        self.driver.find_element(*Locators.LOCATION_ARROW).click()
        self.driver.find_element(*Locators.SELECT_ALL_LOCATIONS).click()

    def select_remote(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.REMOTE_CHECKBOX)
        )

        checkbox.click()

    def find_open_positions(self):
        self.driver.find_element(*Locators.FIND_BUTTON).click()

    def open_latest_job(self):
        job_ul = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.JOB_LIST_WRAPPER)
        )

        job_list = WebDriverWait(job_ul, 10).until(
            ec.presence_of_all_elements_located(Locators.JOB_LIST)
        )

        link_div = job_list[0].find_element(*Locators.JOB_APPLY_LINK_WRAPPER)

        apply_link = link_div.find_element(*Locators.LINK_TAG)

        apply_link.click()

    def keyword_in_page(self, keyword):
        body = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.PAGE_BODY)
        )
        sleep(1)
        return True if keyword in body.text else False

    def click_search_icon(self):
        self.driver.find_element(*Locators.SEARCH_ICON).click()
        sleep(1)

    def input_search_keyword(self, keyword):
        search_input = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(Locators.SEARCH_INPUT)
        )

        search_input.send_keys(keyword)
        sleep(1)

    def click_find_button(self):
        find_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(Locators.SEARCH_FIND_BUTTON)
        )

        find_button.click()