from selenium.webdriver.common.by import By


class Locators:
    CAREERS_LINK = (By.LINK_TEXT, "Careers")
    KEYWORDS_INPUT = (By.CSS_SELECTOR, "input[type=text][placeholder='Keyword']")
    LOCATION_ARROW = (By.CLASS_NAME, "select2-selection__arrow")
    SELECT_ALL_LOCATIONS = (By.XPATH, "//li[@title='All Locations']")
    REMOTE_CHECKBOX = (By.CSS_SELECTOR, "label[for='id-93414a92-598f-316d-b965-9eb0dfefa42d-remote']")
    FIND_BUTTON = (By.XPATH, "//button[contains(text(), 'Find')]")
    JOB_LIST_WRAPPER = (By.CLASS_NAME, "search-result__list")
    JOB_LIST = (By.TAG_NAME, "li")
    JOB_APPLY_LINK_WRAPPER = (By.CLASS_NAME, "search-result__item-controls")
    LINK_TAG = (By.TAG_NAME, "a")
    PAGE_BODY = (By.TAG_NAME, "body")
    SEARCH_ICON = (By.XPATH, "//button[contains(@class, 'header-search__button')]")
    SEARCH_INPUT = (By.XPATH, "//div[@class='search-results__input-holder']/descendant::input")
    SEARCH_FIND_BUTTON = (By.XPATH, "//button[contains(@class, 'custom-button') and contains(@class, 'uppercase-text')]")