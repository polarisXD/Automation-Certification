import unittest
import logging
from selenium import webdriver
from commons.copartAPI import CopartAPI


class Challenge8(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.api = CopartAPI()
        logging.basicConfig(filename="copartapi.log",level=logging.INFO)

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge8(self):
        # code for our test steps
        try:
            data = self.api.search("toyota camry")
            logging.info("Response from toyota comary query:")
            logging.info(data)
            searches = ["nissan skyline", "porsche 911", "ford 150", "ferrari", "tesla model s", "mazda 3", "mazda 6",
                        "pontiac solstice", "chevy camaro", "infinity g35", "subaru outback"]
            for search in searches:
                data = self.api.search(search)
                logging.info("Elements in " + search + " search results: " + str(data["data"]["results"]["totalElements"]))
        except ConnectionError:
            print("Response error")
            assert False




if __name__ == '__main__':
    unittest.main();