from selenium import webdriver

from core.bot.botbook import BookBot

def get_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(90)
    
    return driver

if __name__ == '__main__':
    driver = get_driver()
    bot = BookBot(driver)
    
    while(bot.has_more_pages):
        bot.scrape()