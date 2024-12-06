from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def evangadi_testing():
    driver.get("https://www.evangadi.com")
    print(driver.current_url)
    print(driver.title)
    driver.maximize_window()
    driver.minimize_window()
    driver.fullscreen_window()
    
    time.sleep(4)

    driver.find_element(By.CLASS_NAME ,"button-2").click()
    driver.back()
    driver.forward()
    time.sleep(5)
    driver.refresh()

    text= driver.find_element(By.CLASS_NAME ,"lnk-toggler").text
    print(text)

    driver.quit()

evangadi_testing()
