from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.example.com/")

print(driver.title)

time.sleep(15)

driver.quit()