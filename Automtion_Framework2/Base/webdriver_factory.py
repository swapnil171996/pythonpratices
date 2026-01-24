from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class WebdriverFactory:
    def __init__(self,browser,url=None,headless=False):
        self.browser=browser
        self.url=url
        self.headless=headless
    def get_driver_instance(self):
        driver=None
        if self.browser.lower()=='firefox':
            driver=webdriver.Firefox()
        elif self.browser.lower()=='edge':
            driver=webdriver.Edge()
        elif self.browser.lower()=='chrome':
            option=Options()
            if self.headless:

                option.add_argument('--headless')
            option.add_argument("--window-size=800,600")
            option.add_argument("--disable-popup-blocking")
            option.add_argument("--allow-running-insecure-content")
            option.add_argument("--ignore-certificate-errors")
            driver=webdriver.Chrome(options=option)
        if self.url is not None:
            driver.get(self.url)
        driver.maximize_window()
        return driver

