from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.keys import Keys

def calc_func(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 

    with open("../test.txt", "w") as file:
        content = file.write("automationbypython")
    
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, "../test.txt")
    print(file_path)


    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_field = browser.find_element_by_css_selector("input[name='firstname']")
    input_field.send_keys("Russia")
    input_field = browser.find_element_by_css_selector("input[name='lastname']")
    input_field.send_keys("Russia")
    input_field = browser.find_element_by_css_selector("input[name='email']")
    input_field.send_keys("Russia")

    input_field = browser.find_element_by_css_selector('[type="file"]')
    input_field.send_keys(file_path)

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


