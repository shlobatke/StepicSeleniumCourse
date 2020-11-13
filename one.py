from selenium import webdriver
import time


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # num = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # input0 = browser.find_element_by_link_text(num).click()
    time.sleep(2)
    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("ivanov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("ivan@mail.ru")
    button = browser.find_element_by_xpath('//button[contains(text(),"Submit")]').click()

    #     # Проверяем, что смогли зарегистрироваться
    #     # ждем загрузки страницы
    time.sleep(10)
    #
    #     # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_xpath("//h1[contains(text(),'Congratulations! You have successfully registered!')]")
         # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = 'Congratulations! You have successfully registered!'
    #
    #     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt
    #

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()