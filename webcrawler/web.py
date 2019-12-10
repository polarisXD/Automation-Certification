from webcrawler.soupmaker import *

class Web:
    def __init__(self, driver, domain):
        self.unvisited = set()
        self.visited = []
        self.driver = driver
        self.domain = domain

    def get_links(self):
        soup = make_soup(self.driver)
        hrefs = soup.find_all('a', href=True)
        for href in hrefs:
            link = href.get("href")
            if "./" in link:
                new_link = self.domain + link[1:]
                if new_link not in self.visited:
                    self.unvisited.add(new_link)

    def traverse_web(self):
        while len(self.unvisited) > 0:
            visiting = self.unvisited.pop()
            print("Visiting: " + visiting)
            self.driver.get(visiting)
            self.visited.append(visiting)
