import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ElementUtils:
    @staticmethod
    def force_scroll(driver, web_element, position: str = 'center'):
        with allure.step('Прокрутить элемент в центр страницы'):
            driver.execute_script("arguments[0].scrollIntoView({block: arguments[1]})", web_element, position)

    @staticmethod
    def take_screenshot(driver):
        with allure.step('Сделать скриншот'):
            allure.attach(driver.get_screenshot_as_png(), name='ScreenShot', attachment_type=AttachmentType.PNG)

    @staticmethod
    def check_display_passed_elements(driver, elements):
        with allure.step('Проверить отображение переданных элементов'):
            counter = 0
            wait = WebDriverWait(driver, timeout=10)

            for i in elements:
                counter += 1
                try:
                    element = wait.until(expected_conditions.element_to_be_clickable(i))
                    assert element.is_displayed(), f'"Элемент" № {counter} не отобразился'
                except Exception:
                    ElementUtils.take_screenshot(driver)
