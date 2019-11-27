import unittest
from selenium import webdriver
from copartAPI import CopartAPI

class Challenge10(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.api = CopartAPI()

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge10(self):
        # code for our test steps
        #TODO: get csv
        csv_data = [[], [], []]
        try:
            for row in csv_data:
                data = self.api.search(row)
                assert row in data["data"]["results"]["content"]
        except ConnectionError:
            print("Response error")
            assert False


if __name__ == '__main__':
    unittest.main();