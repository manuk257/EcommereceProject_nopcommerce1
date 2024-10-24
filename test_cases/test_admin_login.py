import undetected_chromedriver as uc
import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


# Launch browser with undetected-chromedriver
def test_Admin_Login():
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login")


# Perform login steps
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys("admin")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(30)
    print(driver.title)
