from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search:
    def __init__(self, driver):
        self.driver = driver

    def search(self, term):
        search = self.driver.find_element_by_id("support-search-input")
        search.send_keys(term)
        search.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source

    def validate(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-head")))
        search_results = self.driver.find_elements_by_xpath('//ul[@class="search-results-list"]/section/div/a')
        assert search_results
        print("Results found: " + str(len(search_results)))
        if len(search_results) == 0:
            assert False
