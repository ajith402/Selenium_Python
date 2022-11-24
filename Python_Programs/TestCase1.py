from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import      time


# driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Firefox(GeckoDriverManager().install())

driver.get("https://google.com")

driver.maximize_window()

print(driver.title)

time.sleep(10)
driver.close()