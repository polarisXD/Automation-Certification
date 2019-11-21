import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge6(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge6(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        search = self.driver.find_element_by_id("input-search")
        search.send_keys("nissan")
        search.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source
        timeout = 10
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIsNotNone(table, "Unable to load table data")
        table_rows = table.find_elements_by_tag_name("tr")
        while len(table_rows) <= 1:
            table_rows = table.find_elements_by_tag_name("tr")
        try:
            skyline_found = False
            for row in table_rows:
                if "skyline" in row.text:
                    skyline_found = True
            if not skyline_found:
                raise ValueError("Skyline not found")
        except ValueError:
            self.driver.save_screenshot("screenshot.png")


if __name__ == '__main__':
    unittest.main();