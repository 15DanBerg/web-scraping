from selenium.webdriver import Chrome
from domain.book import Book
from typing import List

class Bot():
    def __init__(self, driver: Chrome):
        self.__driver = driver
    
    def scrape(self, page_number: int = None) -> (int, List[Book]):
        raise NotImplementedError(
            "method scrape has not implemented on %s" % (self.__class__.__name__)
        )
    
    def has_more_pages(self) -> bool:
        raise NotImplementedError(
        "method get_next_page has not implemented on %s" % (self.__class__.__name__)
        )

