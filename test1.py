from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By  # Import By
import time
import config

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def login_test():
        
        driver.get(config.base_url)
        user_id= driver.find_element(By.XPATH , ("//input[@name='uid']"))
        user_id.send_keys(config.id)
        time.sleep(0)

        driver.find_element(By.XPATH , "//input[@name='password']").send_keys(config.Password)
        time.sleep(0)

        driver.find_element(By.XPATH , "//input[@name='btnLogin']").click()
        time.sleep(0)

       


        driver.close()





