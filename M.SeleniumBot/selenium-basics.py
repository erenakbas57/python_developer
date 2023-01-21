from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
print(driver.title)

url1 = "https://github.com/erenakbas57"
driver.get(url1)

time.sleep(2)
driver.back()
# driver.forward()

time.sleep(2)
driver.close()