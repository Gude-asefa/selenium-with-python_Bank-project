import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import config
import util


@pytest.mark.parametrize("userid, password", util.read_data_from_excel("C:\\Users\\sc0cp\\OneDrive\\Desktop\\TESTING\\data_sheet.xlsx", "Sheet1"))


def test_login(userid, password):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    

    driver.get(config.base_url)
   
    user_id = driver.find_element(By.XPATH, "//input[@name='uid']")
    user_id.send_keys(userid)
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@name='btnLogin']").click()
  

    try:

        if driver.current_url == config.manager_url:    
            success_message = driver.find_element(By.TAG_NAME, "marquee") 
            assert success_message.text == "Welcome To Manager's Page of Guru99 Bank"
            driver.get_screenshot_as_file(".\\report\\manager_page.png") 
        else:
            # Wait for the alert to be present
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            assert alert.text == "User or Password is not valid"
            alert.accept()  

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()