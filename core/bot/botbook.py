from selenium.webdriver import Chrome
from core import Bot


class BookBot(Bot):
    def __init__(self, driver: Chrome):
        self.url = "https://books.toscrape.com/"
        self.__driver = driver
    
    def scrape(self, page_number: int = None) -> (int, List[Property]):
        if self.__driver.title == "":
            return None
    
    def has_more_pages(self) -> bool:
        self
    