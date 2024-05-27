from core import Bot
from domain.book import Book

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from typing import List

class BookBot(Bot):
    def __init__(self, driver: Chrome):
        self.url = "https://books.toscrape.com/"
        self.__driver = driver
    
    
    def scrape(self, page_number: int = None) -> (int, List[Book]):
        if self.__driver.title == "":
            self.__get_first_page(page_number)
        
        properties = []
        
        self.__get_next_page()

        return properties
    

    def has_more_pages(self) -> bool:
        if self.__driver.title == "":
            return True
        
        next_page_button_xpath = '//li[@class="next"]'
        if self.__driver.find_element(By.XPATH, next_page_button_xpath).is_displayed():
            return True

        return False
        
        
    def __get_first_page(self, page_number):
        if page_number is None:
            self.__driver.get(self.url)
        else:
            self.__driver.get("%s?pagina=%s" % (self.url, page_number))
      
            
    def __get_next_page(self):
        next_page_button_xpath = '//li[@class="next"]/a'
    
        try:
            next_btn_elem = self.__driver.find_element(By.XPATH, next_page_button_xpath)
            if next_btn_elem.is_displayed():
                next_btn_elem.click()
        except NoSuchElementException:
            return None
        
        
        
