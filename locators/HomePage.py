from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_careers_link(self):
        self.driver.find_element(By.LINK_TEXT, "Careers").click()

    def input_keyword(self, keyword):
        self.driver.find_element(By.CSS_SELECTOR, "input[type=text][placeholder='Keyword']").send_keys(keyword)

    def accept_cookies(self):
        accept_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )

        accept_button.click()

    def select_all_locations(self):
        self.driver.find_element(By.CLASS_NAME, "select2-selection__arrow").click()
        self.driver.find_element(By.XPATH, "//li[@title='All Locations']").click()

    def select_remote(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "label[for='id-93414a92-598f-316d-b965-9eb0dfefa42d-remote']"))
        )

        checkbox.click()

    def find_open_positions(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    def sort_by_date(self):
        sorter = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "label[for='sort-time']"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behaviour: 'smooth', block:'center'});", sorter)

        sorter.click()

    def open_latest_job(self):
        # get the ul list of job items
        job_ul = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CLASS_NAME, "search-result__list"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behaviour: 'smooth', block:'center'});", job_ul)

        job_li = job_ul.find_elements(By.TAG_NAME, "li")

        job_link = WebDriverWait(job_li[0], 10).until(
            ec.presence_of_element_located((By.TAG_NAME, "a"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", job_link)

        # job_link.click()