from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#introducing a class called Cowin
class Cowin_url:

#url initializing in the constructor
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

#booting into the url
    def booting_function(self):
        try:
            self.driver.get(self.url)
            #time.sleep(5)
            return True
        except:
            Print ("Error on this web URL")
            return False

#create two windows for FAQ and Partner
    def create_FAQ_and_partner(self):
        if self.booting_function() == True:
            self.driver.maximize_window()

            wait = WebDriverWait(self.driver,10)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a'))).click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a'))).click()
            time.sleep(5)

        else:
            return False

# Fetching IDs of windows
    def fetch_ids(self):
        if self.booting_function() == True:
            window_handles = self.driver.window_handles
            for handles in window_handles:
                print(handles)

#closing the windowns one by one
    def closing_windows(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.close()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    url= "https://www.cowin.gov.in/"
    result = Cowin_url(url)
    result.booting_function()
    result.create_FAQ_and_partner()
    result.fetch_ids()
    result.closing_windows()