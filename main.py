from selenium import webdriver

def get_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(90)
    
    return driver

if __name__ == '__main__':
    driver = get_driver()