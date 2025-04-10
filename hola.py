from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f = logging.Formatter("[%(levelname)s] - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(f)
logger.addHandler(ch)

options = Options()
options.add_argument("--headless")

try:
    driver = webdriver.Firefox(options=options)
    
    driver.get("https://www.saucedemo.com/")

    logger.debug(f"{driver.title}")

    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    logging_btn = driver.find_element(By.ID, "login-button")

    user_name.send_keys("standard_user")
    password.send_keys("secret_sauce")
    logging_btn.click()

    logger.debug(f"{driver.current_url}")

    backpack = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    print(driver.title)


except Exception as e:
    print("FAILED:", str(e))
finally:
    if 'driver' in locals():
        driver.quit()
