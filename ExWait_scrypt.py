from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    # Ожидаем изменения цены до указанного значения
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    submit_button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    number = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(number)
    browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(5)
    browser.quit()

