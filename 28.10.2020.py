from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    time.sleep(2)
    browser.find_element_by_xpath("//button[contains(text(),'I want to go on a magical journey!')]").click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)
    x =browser.find_element_by_css_selector("#input_value")
    # print(x)
    xx = int(x.text)
    print(xx)
    def calc(xx):
        return str(math.log(abs(12 * math.sin(int(xx)))))

    y = calc(xx)
    print(y)
    browser.find_element_by_xpath("//input[@id='answer']") .send_keys(y)
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

finally:
    time.sleep(10)
    # browser.quit()