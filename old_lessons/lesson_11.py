from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x1 = int(browser.find_element_by_css_selector("#num1").text)
    x2 = int(browser.find_element_by_css_selector("#num2").text)
    y = str(x1 + x2)
    value = "[value='{}']".format(y)
    browser.find_element_by_css_selector("#dropdown").click()
    browser.find_element_by_css_selector(value).click()

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


