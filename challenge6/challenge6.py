import unittest
from selenium import webdriver
from commons.search import Search
from commons.tableCruiser import TableCruiser

class Challenge6(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.search = Search(self.driver)
        self.tableCruiser = TableCruiser(self.driver)

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge6(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.search.search("nissan")
        self.tableCruiser.find_table()
        self.tableCruiser.find_table_rows(expected_table_size=1)
        self.tableCruiser.scan_for_value("skyline")



if __name__ == '__main__':
    unittest.main();