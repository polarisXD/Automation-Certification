from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search(self, term):
        search = self.driver.find_element_by_id("input-search")
        search.send_keys(term)
        search.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source
