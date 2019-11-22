import unittest
from selenium import webdriver
from fibonacci import Fibonacci
from numberSpeller import NumberSpeller


class Challenge4(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")
        self.fib = Fibonacci()
        self.numberSpeller = NumberSpeller()

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def test_challenge4(self):
        # code for our test steps
        fibonacci_number = self.fib.getFibonacciNumber(50)
        print(str(fibonacci_number) + " - " + self.numberSpeller.spellNumber(fibonacci_number))


if __name__ == '__main__':
    unittest.main();