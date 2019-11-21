import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge2(self):
        # code for our test steps
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        search = self.driver.find_element_by_id("input-search")
        search.send_keys("exotic")
        search.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source
        timeout = 10
        wait = WebDriverWait(self.driver, timeout)
        table = wait.until(EC.presence_of_element_located((By.ID, "serverSideDataTable"))).get_attribute("innerHTML")
        print(table)
        self.assertIn("PORSCHE", table)


if __name__ == '__main__':
    unittest.main();