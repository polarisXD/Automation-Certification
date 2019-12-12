# sling.com, under sling orange, print out alt text

import unittest
from selenium import webdriver


class BonusChallenge1(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_bonus_challenge1(self):
        # code for our test steps
        self.driver.get("https://sling.com")
        self.assertIn("Sling TV", self.driver.title)
        orange_channels = self.driver.find_elements_by_xpath('//*[@id="channelList"]/li/img')
        for channel in orange_channels:
            print(channel.get_attribute("alt"))


if __name__ == '__main__':
    unittest.main();