import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commons.copartMainPage import MainPage

class Challenge7(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge7(self):
        # code for our test steps
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        self.main_page.fill_makes_models()
        self.main_page.check_makes_models_links()



if __name__ == '__main__':
    unittest.main();