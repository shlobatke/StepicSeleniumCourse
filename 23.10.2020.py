from selenium import webdriver
import os
import time

try:
   with open("test.txt", "w") as file:
      content = file.write("automationbypython")
      path =os.getcwd() + '/' + file.name

   browser = webdriver.Chrome()
   browser.get("http://suninjuly.github.io/file_input.html")
   browser.find_element_by_name("firstname").send_keys("kak zhe ti menya zaebal")
   browser.find_element_by_name("lastname").send_keys("neuzheli,bleat")
   browser.find_element_by_name("email").send_keys("norm")
   browser.find_element_by_name("file").send_keys(path)
   browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

finally:
   time.sleep(10)
   browser.quit()

