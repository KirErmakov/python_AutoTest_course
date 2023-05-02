from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    time.sleep(15)  # sleep(30) - слишком долго
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Such element not found"


