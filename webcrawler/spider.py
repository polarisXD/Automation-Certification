from webcrawler.web import Web


class Spider:

    def __init__(self, driver, domain):
        self.web = Web(driver, domain)
        self.driver = driver
        self.domain = domain

    def crawl(self, url):
        self.web.get_links()
        self.web.traverse_web()
        print("Pages visited: " + str(len(self.web.visited)))
