from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
browser.find_element_by_id("button")
# browser.implicitly_wait(5)
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
# browser.quit()