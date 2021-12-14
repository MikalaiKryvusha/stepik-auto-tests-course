from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc_func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_css_selector("button.btn")


    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )


    button.click()

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x_text = x_element.text
    print(x_text)
    y = str(calc_func(x_text))
    print(y)
    browser.find_element_by_css_selector("#answer.form-control").send_keys(y)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("#solve.btn").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
