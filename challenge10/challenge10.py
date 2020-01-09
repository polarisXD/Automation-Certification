import unittest
from selenium import webdriver
from commons.copartAPI import CopartAPI
import pandas




class Challenge10(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.api = CopartAPI()

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def create_query(self, row):
        query = ""
        for col in row:
            if type(col) is not float:
                query = query + str(col) + " "
        return query

    def test_challenge10(self):
        # code for our test steps
        csv_data = pandas.read_excel("data.xlsx", dtype=str)
        data = csv_data.values
        try:
            for row in data:
                query = self.create_query(row)
                print("Query: " + query)
                data = self.api.search(query)
                print("Search results: " + str(data["data"]["results"]["totalElements"]))
        except ConnectionError:
            print("Response error")
            assert False


if __name__ == '__main__':
    unittest.main();