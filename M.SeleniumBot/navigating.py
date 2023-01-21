from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#tuşları aktive ettik


driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("q")
time.sleep(1)
searchInput.send_keys("python")

searchInput.send_keys(Keys.ENTER) # enter a tıkladık
time.sleep(3)

kod = driver.page_source
print(kod)

#repos = driver.find_elements_by_css_selector(".repo-list-item h3 a")

#for element in repos:
    #print(element.text)


driver.close()