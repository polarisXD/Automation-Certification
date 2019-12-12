#help.sling.com run a search, validate there were results

import unittest
from selenium import webdriver
from sling.search import Search


class BonusChallenge2(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.search = Search(self.driver)

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_bonus_challenge2(self):
        # code for our test steps
        self.driver.get("https://help.sling.com")
        self.assertIn("Help Center", self.driver.title)
        self.search.search("Roku")
        self.search.validate()

if __name__ == '__main__':
    unittest.main();