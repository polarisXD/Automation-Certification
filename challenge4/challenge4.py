import unittest
from selenium import webdriver
from challenge4.fibonacciSpelling import spellFibonacciNumber

class Challenge1(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        spellFibonacciNumber(22)

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge4(self):
        # code for our test steps
        print()


if __name__ == '__main__':
    unittest.main();