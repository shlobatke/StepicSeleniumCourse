from selenium import webdriver
import time
import math

# link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x =browser.find_element_by_xpath("//img[@id='treasure']").get_attribute("valuex")
    print(x)

    # X1 = int(x.text)
    # реобразую значение переменной в число
    # print(X1)
    # y = abs(12*math.sin(X1))

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(y)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()


finally:
    time.sleep(10)
    browser.quit()



