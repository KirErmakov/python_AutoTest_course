from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//*[@type="submit"]').click()
    # Переход на новую вкладку браузера
    browser.switch_to.window(browser.window_handles[1])
    number = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(number)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()


