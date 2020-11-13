from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
    browser.find_element_by_css_selector("#book").click()
    button = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    inp = browser.find_element_by_css_selector("#input_value")
    inpV = int(inp.text)
    print(inpV)
    def calc(inpV):
        return str(math.log(abs(12 * math.sin(inpV))))
    y = calc(inpV)
    button.send_keys(y)
    browser.find_element_by_css_selector("#solve").click()


finally:
    time.sleep(10)
    # browser.quit()