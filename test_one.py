import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import config
import util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Assuming util.read_data_from_excel returns a list of tuples [(userid, password), ...]
@pytest.mark.parametrize("userid, password", util.read_data_from_excel("C:\\Users\\sc0cp\\OneDrive\\Desktop\\TESTING\\data_sheet.xlsx", "Sheet1"))
def test_login(userid, password):
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get(config.base_url)
                
                # Locate and interact with input fields
        user_id = driver.find_element(By.XPATH, "//input[@name='uid']")
        user_id.send_keys(userid)
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        time.sleep(1)

                # Click login
        driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
        time.sleep(1)

        
        if (driver.current_url("https://www.demo.guru99.com/V4/manager/Managerhomepage.php")):
            welcome_message = driver.find_element(By.TAG_NAME, "marquee")
            assert welcome_message.is_displayed(), "Welcome message not displayed. Login might have failed."
        else: 
        
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

            assert alert.text == "user or password is not valid"

    finally:        
                

            # Quit the browser
        driver.quit()
