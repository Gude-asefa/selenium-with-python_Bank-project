from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By  # Import By
import time
import config

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class BankProject():
    def login_test(self):
        driver.get(config.base_url)
        user_id= driver.find_element(By.XPATH , ("//input[@name='uid']"))
        user_id.send_keys(config.id)
        time.sleep(1)

        driver.find_element(By.XPATH , "//input[@name='password']").send_keys(config.Password)
        time.sleep(1)

        driver.find_element(By.XPATH , "//input[@name='btnLogin']").click()
        time.sleep(2)


        driver.close()

demo=BankProject()
demo.login_test()





