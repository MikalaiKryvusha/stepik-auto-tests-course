from selenium import webdriver
import time
import math
from selenium.webdriver.common.keys import Keys

def calc_func(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x_text = x_element.text
    y = str(calc_func(x_text))
    browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
    browser.find_element_by_css_selector("#answer.form-control").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


