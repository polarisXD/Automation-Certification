import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge1(unittest.TestCase):

    def setUp(self):
        # code to startup webdriver
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        # code to close webdriver
        self.driver.close()

    def countEntries(self, entry, dictionary):
        if entry not in dictionary.keys():
            dictionary[entry] = 1
        elif entry in dictionary.keys():
            count = dictionary[entry]
            dictionary[entry] = count + 1
        else:
            print(entry + " not handled")

    def printEntries(self, dictionary):
        for key in dictionary.keys():
            print(key + ": " + str(dictionary[key]))

    def switch(self, case):
        # damage switch statement
        if case == "REAR END" or case == "FRONT END" or case == "MINOR DENT/SCRATCHES" or case == "UNDERCARRIAGE":
            return case
        else:
            return "MISC"

    def test_challenge5(self):
        # code for our test steps
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        search = self.driver.find_element_by_id("input-search")
        search.send_keys("porsche")
        search.send_keys(Keys.RETURN)
        assert "No results found" not in self.driver.page_source
        timeout = 10
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, "serverSideDataTable")))
        options = self.driver.find_elements_by_xpath('//*[@id="serverSideDataTable_length"]/label/select/option')
        for option in options:
            if option.text == "100":
                option.click()
        table = self.driver.find_element_by_id("serverSideDataTable")
        self.assertIsNotNone(table, "Unable to load table data")
        table_rows = table.find_elements_by_tag_name("tr")
        while len(table_rows) <= 21:
            table_rows = table.find_elements_by_tag_name("tr")
        models = {}
        damages = {}
        for row in table_rows:
            if "PORSCHE" in row.text:
                porsche_model = row.find_elements(By.TAG_NAME, "td")[5].text
                self.countEntries(porsche_model, models)
                damage = row.find_elements(By.TAG_NAME, "td")[11].text
                damage_type = self.switch(damage)
                self.countEntries(damage_type, damages)
        print("\nModels:\n")
        self.printEntries(models)
        print("\nDamages:\n")
        self.printEntries(damages)


if __name__ == '__main__':
    unittest.main();