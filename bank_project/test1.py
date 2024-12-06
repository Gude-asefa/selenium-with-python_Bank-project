from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By  # Import By
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# id :mngr603529
# Password :	pujEbEv
class BankProject():
    def login_test(self):
        driver.get("http://www.demo.guru99.com/V4/")
        user_id= driver.find_element(By.XPATH , ("//input[@name='uid']"))
        user_id.send_keys("mngr603529")
        time.sleep(1)

        driver.find_element(By.XPATH , "//input[@name='password']").send_keys("pujEbEv")
        time.sleep(1)

        driver.find_element(By.XPATH , "//input[@name='btnLogin']").click()
        time.sleep(2)


        driver.close()

demo=BankProject()
demo.login_test()





