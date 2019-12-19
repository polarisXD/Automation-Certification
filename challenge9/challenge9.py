import unittest
from selenium import webdriver
from commons.copartAPI import CopartAPI

class Challenge9(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.api = CopartAPI()

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge9(self):
        # code for our test steps
        try:
            data = self.api.search("toyota camry")
        except ConnectionError:
            print("Response error")
            assert False
        content_element = data["data"]["results"]["content"][0]
        assert content_element
        assert type(content_element) is dict
        assert type(content_element["lotNumberStr"]) is str
        assert type(content_element["ln"]) is int
        assert type(content_element["mkn"]) is str
        for key in content_element.keys():
            print(key + ":" + str(content_element[key]) + " data type: " + str(type(content_element[key])))


if __name__ == '__main__':
    unittest.main();