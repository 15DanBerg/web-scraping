from core import Bot
from domain.book import Book

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from typing import List

class BookBot(Bot):
    def __init__(self, driver: Chrome):
        self.url = "https://books.toscrape.com/"
        self.__driver = driver
    
    def scrape(self, page_number: int = None) -> (int, List[Book]):
        if self.__driver.title == "":
            return 
    
    def has_more_pages(self) -> bool:
        if self.__driver.title == "":
            return True
        
        next_page_button_xpath = '//li[@class="next"]'
        if self.__driver.find_element(By.XPATH, next_page_button_xpath).is_displayed():
            return True

        return False
        
