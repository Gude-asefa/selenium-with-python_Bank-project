

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the Evangadi website
driver.get("https://www.evangadi.com")

# Print the title of the page
print(driver.title)

# Close the driver
driver.quit()