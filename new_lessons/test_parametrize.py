import time
import math
import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

class Test:

    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


    @pytest.mark.parametrize('url_test', links)
    def test_1(self, driver, url_test):

        link = f"{url_test}"

        driver.get(link)

        # test flow
        css_locator = "textarea.ember-text-area"
        input_field = self.wait_for_locator(driver, css_locator, timeout=20)
        input_field.send_keys(str(self.answer()))
        css_locator = "button.submit-submission"
        send_button = self.wait_for_locator(driver, css_locator, timeout=20)
        time.sleep(1)
        send_button.click()
        css_locator = "pre.smart-hints__hint"
        feed_back = self.wait_for_locator(driver, css_locator, timeout=20)
        feed_back_text = feed_back.text
        expecting_feed_back_text = "Correct!"

        if feed_back_text != expecting_feed_back_text:
            print(f"Needed text: {feed_back_text}\n")

        assert feed_back_text == expecting_feed_back_text, f"Expected feedback text is {expecting_feed_back_text}, but was found text {feed_back_text}"


    def answer(self):
        answer = math.log(int(time.time()))
        return answer

    def wait_for_locator(self, driver, locator, timeout):

        while True:
            if timeout == 0:
                raise Exception("Timeout!")

            try:
                element = driver.find_element_by_css_selector(locator)
                return element
            except:
                timeout -= 1
                time.sleep(1)
        pass


