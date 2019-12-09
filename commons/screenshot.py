class Screenshot:
    def __init__(self, driver):
        self.driver = driver

    def take(self, filename):
        self.driver.save_screenshot(filename)