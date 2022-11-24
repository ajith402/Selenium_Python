from selenium import webdriver
import time

driver= webdriver.Chrome(executable_path="D://Programs//Python//SeleniumPython//chromedriver.exe")
# driver=webdriver.Firefox(executable_path="D://Programs//Python//SeleniumPython//geckodriver.exe")
# driver=webdriver.Edge(executable_path="D://Programs//Python//SeleniumPython//msedgedriver.exe")

driver.get("https://google.com/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.close()







