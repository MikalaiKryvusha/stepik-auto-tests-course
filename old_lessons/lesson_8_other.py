from selenium import webdriver
from selenium.webdriver.common.by import By
import time


if __name__ == '__main__':
    URL = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(URL)

    inputs = browser.find_elements(By.XPATH, "//input[@required='']")

    for input_field in inputs:
        input_field.send_keys("deez")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    actual = browser.find_element(By.TAG_NAME, "h1").text

    assert actual == "Congratulations! You have successfully registered!"

    time.sleep(30)
    browser.quit()