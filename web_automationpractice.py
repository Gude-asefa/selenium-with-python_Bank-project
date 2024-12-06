from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def evangadi_testing():
    ''' driver.get("https://www.evangadi.com")
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
    
    '''

    driver.get("https://www.ethiopianairlines.com/et")
    dropdown= driver.find_element(By.CSS_SELECTOR ,"div[class='card card-body'] div div[class='widget-input mt-2'] div[class='d-flex']").click()

    dd=Select(dropdown)



    driver.quit()

evangadi_testing()

