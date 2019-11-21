import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge7(self):
        # code for our test steps
        self.driver.get("https://copart.com")
        self.assertIn("Copart", self.driver.title)
        makes_models = []
        for i in range(1, 5):
            column_xpath = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(i) + ']/ul/li/a'
            popular_column = self.driver.find_elements_by_xpath(column_xpath)
            assert popular_column
            assert len(popular_column) > 0
            items = []
            for item in popular_column:
                item_name = item.text
                item_link = item.get_attribute("href")
                items.append({item_name: item_link})
            makes_models.append(items)
        for col in makes_models:
            print(col)


if __name__ == '__main__':
    unittest.main();