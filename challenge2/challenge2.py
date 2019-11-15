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
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIsNotNone(table, "Unable to load table data")
        table_rows = table.find_elements_by_tag_name("tr")
        while len(table_rows) <= 1:
            table_rows = table.find_elements_by_tag_name("tr")
        porsche_present = False
        checked = 0
        for row in table_rows:
            checked += 1
            if "PORSCHE" in row.text:
                porsche_present = True
                break
        print("Items checked: " + str(checked))
        print("Total items: " + str(len(table_rows)))
        self.assertTrue(porsche_present, "Could not locate PORSCHE in results.")


if __name__ == '__main__':
    unittest.main();