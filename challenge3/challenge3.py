import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge3(self):
        # code for our test steps
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        timeout = 10
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]/div/ul/li/a')))
        popular_items = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]/div[2]/div/ul/li/a')
        assert popular_items
        assert len(popular_items) > 0
        for item in popular_items:
            item_link = item.get_attribute("href")
            assert item_link
            print(item.text + " - " + item_link)


if __name__ == '__main__':
    unittest.main();