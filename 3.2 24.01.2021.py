from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_one(self):
        if __name__ == "__main__":
            unittest.main()

# link = 'http://suninjuly.github.io/math.html'


    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration1.html')

    time.sleep(2)
    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("ivanov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("ivan@mail.ru")
    button = browser.find_element_by_xpath('//button[contains(text(),"Submit")]').click()


    time.sleep(10)

    welcome_text_elt = browser.find_element_by_xpath("//h1[contains(text(),'Congratulations! You have successfully registered!')]")

    welcome_text = 'Congratulations! You have successfully registered!'

    assert "Congratulations! You have successfully registered!" == welcome_text_elt

    if __name__ == "__main__":
        test_one()
        print ("norm")
    browser.quit()