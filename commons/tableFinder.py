from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TableFinder:
    def __init__(self, driver):
        self.driver = driver
        self.table = None
        self.table_rows = None

    def find_table(self):
        timeout = 10
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        self.table = self.driver.find_element_by_id("serverSideDataTable")
        assert self.table

    def find_resized_table(self, table_size):
        timeout = 10
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        options = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable_length"]/label/select/option')
        for option in options:
            if option.text == str(table_size):
                option.click()
        self.table = self.driver.find_element_by_id("serverSideDataTable")
        assert self.table

    def find_table_rows(self, expected_table_size):
        table_rows = self.table.find_elements_by_tag_name("tr")
        while len(table_rows) < expected_table_size:
            table_rows = self.table.find_elements_by_tag_name("tr")
        assert len(table_rows) >= expected_table_size
        self.table_rows = table_rows