from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    w1 = browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(2)
    btn = browser.find_element_by_tag_name("button")
    time.sleep(1)
    btn.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    x =browser.find_element_by_css_selector("#input_value")
    print(x)
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