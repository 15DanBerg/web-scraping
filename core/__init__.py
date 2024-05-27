from selenium.webdriver import Chrome

class Bot():
    def __init__(self, driver: Chrome):
        self.__driver = driver
    
    def scrape(self, page_number: int = None) -> (int, List[Property]):
        raise NotImplementedError(
            "method scrape has not implemented on %s" % (self.__class__.__name__)
        )
    
    def has_more_pages(self) -> bool:
        raise NotImplementedError(
        "method get_next_page has not implemented on %s" % (self.__class__.__name__)
        )

