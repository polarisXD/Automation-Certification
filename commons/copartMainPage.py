from .tableCruiser import TableCruiser

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.makes_models = []
        self.tableCruiser = TableCruiser(self.driver)

    def fill_makes_models(self):
        self.makes_models = []
        for i in range(1, 5):
            column_xpath = '//*[@id="tabTrending"]/div[1]/div[2]/div[' + str(i) + ']/ul/li/a'
            popular_column = self.driver.find_elements_by_xpath(column_xpath)
            assert popular_column
            assert len(popular_column) > 0
            items = []
            for item in popular_column:
                item_name = item.text
                item_link = item.get_attribute("href")
                items.append([item_name, item_link])
            self.makes_models.append(items)

    def check_makes_models_links(self):
        for col in self.makes_models:
            for model in col:
                model_name = model[0].lower().replace(" ", "-")
                link = model[1]
                self.driver.get(link)
                self.tableCruiser.find_table()
                search_results = self.driver.find_element_by_class_name("result-title")
                assert model_name in search_results.text