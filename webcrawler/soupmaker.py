from bs4 import BeautifulSoup


def make_soup(driver):
    source = driver.page_source
    soup = BeautifulSoup(source, features="html.parser")
    return soup
