from selenium import webdriver

drivers = {
    "chrome": webdriver.Chrome
}

class SeleniumKeywords:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.driver = None

    def open_browser(self, browser="chrome"):
        driver_class = drivers[browser]
        self.driver = driver_class()

    def go_to(self, url):
        self.driver.get(url)