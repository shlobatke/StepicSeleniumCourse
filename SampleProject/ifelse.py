from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    input0 = browser.find_element_by_link_text(num).click()

    input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# from selenium import webdriver
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num = str(math.ceil(math.pow(math.pi, math.e)*10000))
#     print(num)
#
#     input1 = browser.find_element_by_link_text(num).click()
#
#
#
# finally:
#     time.sleep(30)
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла