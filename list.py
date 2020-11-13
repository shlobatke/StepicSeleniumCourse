from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

# link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    x =browser.find_element_by_xpath("//span[@id='num1']")
    print(x)

    X1 = int(x.text)
    # реобразую значение переменной в число
    # y = abs(12*math.sin(X1))
    y = browser.find_element_by_xpath("//span[@id='num2']")
    print(y)
    Y1 = int(y.text)
    print(y)

    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    z = str(X1 + Y1)
    print(z)


    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(z)  # ищем элемент с текстом "Python"

    # browser.find_element_by_id("answer").send_keys(y)
    # browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    # browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    browser.find_element_by_xpath("//button[contains(text(),'Submit')]").click()


finally:
    time.sleep(10)
    browser.quit()



