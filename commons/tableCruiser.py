from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .tableFinder import TableFinder
from .screenshot import Screenshot
from .counter import Counter
from .printer import Printer


class TableCruiser:
    def __init__(self, driver):
        self.driver = driver
        self.tableFinder = TableFinder(driver)
        self.table = None
        self.table_rows = None

        self.printer = Printer()
        self.counter = Counter()

    def find_table(self):
        self.tableFinder.find_table()
        self.table = self.tableFinder.table

    def find_resized_table(self, table_size):
        self.tableFinder.find_resized_table(table_size)
        self.table = self.tableFinder.table

    def find_table_rows(self, expected_table_size):
        self.tableFinder.find_table_rows(expected_table_size)
        self.table_rows = self.tableFinder.table_rows

    def _damage_switch(self, case):
        # damage switch statement
        if case == "REAR END" or case == "FRONT END" or case == "MINOR DENT/SCRATCHES" or case == "UNDERCARRIAGE":
            return case
        else:
            return "MISC"

    def count_table_row_entries(self, value):
        if self.table_rows:
            models = {}
            damages = {}
            for row in self.table_rows:
                if value in row.text:
                    porsche_model = row.find_elements(By.TAG_NAME, "td")[5].text
                    self.counter.countEntries(porsche_model, models)
                    damage = row.find_elements(By.TAG_NAME, "td")[11].text
                    damage_type = self._damage_switch(damage)
                    self.counter.countEntries(damage_type, damages)
            print("\nModels:\n")
            self.printer.printEntries(models)
            print("\nDamages:\n")
            self.printer.printEntries(damages)

    def scan_for_value(self, value):
        try:
            value_found = False
            for row in self.table_rows:
                if value in row.text:
                    value_found = True
            if not value_found:
                raise ValueError(value + " not found")
        except ValueError:
            camera = Screenshot(self.driver)
            filename = value + "NotFound.png"
            camera.take(filename)
