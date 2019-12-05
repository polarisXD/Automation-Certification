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
        popular_makes_models = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]/div[2]/div/ul/li/a')
        popular_categories = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[3]/div/ul/li/a')
        assert popular_makes_models
        assert len(popular_makes_models) > 0
        print("Makes and models:")
        for make_model in popular_makes_models:
            make_model_link = make_model.get_attribute("href")
            assert make_model_link
            print(make_model.text + " - " + make_model_link)
        print("\nCategories")
        elements_left = len(popular_categories)
        while elements_left > 0:
            category = popular_categories[len(popular_categories) - elements_left]
            categories_link = category.get_attribute("href")
            assert categories_link
            print(category.text + " - " + categories_link)
            elements_left = elements_left - 1


if __name__ == '__main__':
    unittest.main();