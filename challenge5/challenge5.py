import unittest
from selenium import webdriver
from commons.search import Search
from commons.tableCruiser import TableCruiser



class Challenge5(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.search = Search(self.driver)
        self.tableCruiser = TableCruiser(self.driver)


    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge5(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.search.search("porsche")
        table_size = 100
        self.tableCruiser.find_resized_table(table_size)
        self.tableCruiser.find_table_rows(table_size)
        self.tableCruiser.count_table_row_entries("PORSCHE")


if __name__ == '__main__':
    unittest.main();