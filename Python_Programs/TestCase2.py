from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


driver=webdriver.Edge(EdgeChromiumDriverManager().install())


driver.get("https://google.com")

print(driver.title)
time.sleep(10)

driver.close()