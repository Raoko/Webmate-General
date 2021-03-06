from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import subprocess
import time

class webmate():

    def __init__(self, URL=None):
        self.URL = URL

    def loadDriver(self, PHANTOM=False):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("--disable-popup-blocking")
        if PHANTOM == True:
            self.chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.get(self.URL)

    def formInput(self, ID=None, XPATH=None, NAME=None, KEY=None, pressEnter=False):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            elem = self.driver.find_element_by_xpath(XPATH)
        elif ID:
            elem = self.driver.find_element_by_id(ID)
        elif NAME:
            elem = self.driver.find_element_by_name(NAME)
        elem.send_keys(KEY)
        if pressEnter == True:
            time.sleep(1)
            elem.send_keys(Keys.RETURN)

    def buttonClick(self, ID=None, XPATH=None, NAME=None):
        time.sleep(0.1)
        self.driver.implicitly_wait(10)
        if XPATH:
            self.driver.find_element_by_xpath(XPATH).click()
        elif ID:
            self.driver.find_element_by_id(ID).click()
        elif NAME:
            self.driver.find_element_by_name(NAME).click()

    def kill(self, arg, times=1):
        for i in range(times):
            subprocess.call(["taskkill", "/f", "/IM", arg])
        
if __name__ == "__main__":
    pass
