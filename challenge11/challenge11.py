import unittest
from selenium import webdriver
from webcrawler.spider import Spider

class Challenge11(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.spider = Spider(self.driver, "https://copart.com")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge11(self):
        # code for our test steps
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        self.spider.crawl(self.spider.domain)

if __name__ == '__main__':
    unittest.main();