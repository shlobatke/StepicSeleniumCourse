from selenium import webdriver
import time
import math

# link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    x =browser.find_element_by_xpath("//span[@id='input_value']")
    X1 = int(x.text)
    # реобразую значение переменной в число
    print(X1)
    # y = abs(12*math.sin(X1))

    def calc(X1):
        return str(math.log(abs(12 * math.sin(int(X1)))))
    y = calc(X1)
    print(y)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView();",answer )
    answer.click()
    time.sleep(1)
    answer.send_keys(y)
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()


finally:
    time.sleep(10)
    # browser.quit()

