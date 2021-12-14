from selenium import webdriver
import time
import math


def calc_func(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)

    browser.switch_to_window(browser.window_handles[1])

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x_text = x_element.text
    y = str(calc_func(x_text))
    browser.find_element_by_css_selector("#answer.form-control").send_keys(y)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    print(browser.switch_to.alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

