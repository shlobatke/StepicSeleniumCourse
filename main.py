from selenium import webdriver
import time
driver = webdriver.Chrome("drivers/chromedriver.exe")
from selenium.webdriver.common.keys import  Keys
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout(6)
driver.get('https://google.com/')
driver.find_element_by_name("q").send_keys("nerd cats")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
# print("Заебок, все робит")
time.sleep(4)
driver.quit()