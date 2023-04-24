from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    number = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(number)
    submit_button = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()
    browser.find_element(By.XPATH, '//*[@for="robotsRule"]').click()
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
