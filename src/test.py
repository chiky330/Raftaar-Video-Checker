# Get all Selenium tools 
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# Get all datetime tools
from datetime import *
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com")
#driver.maximize_window()
sleep(2)

#accept cookies
#cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy"]'))).click()

# Insert your own login info for now

email=driver.find_element_by_id("email")
email.send_keys("INSERT USERNAME") 
password=driver.find_element_by_id("pass")
password.send_keys("GET PASSWORD")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(2)
driver.get("FACEBOOK GROUP OF YOUR CHOICE") # change group here
sleep(30)


