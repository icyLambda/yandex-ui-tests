import time
import allure

from selenium.webdriver.common.by import By
from variables.data import BASE_URL
from locators import locators_selectors as ls
from library.element_utils import ElementUtils


class YandexPage:
    URL = BASE_URL

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузить страницу Yandex.Ru')
    def load_yandex_page(self):
        self.driver.get(YandexPage.URL)

    @allure.step('Проверить загрузку страницы Yandex.Ru')
    def check_page_loading_yandex(self):
        title = self.driver.title
        ElementUtils.take_screenshot(driver=self.driver)
        assert title == "Яндекс", 'Страница не соответствует ожидаемой'

    @allure.step('Проверить отображение блока новостей на странице')
    def check_display_news_block(self):
        with allure.step('Проверить наличие блока новостей в коде страницы'):
            news_block = self.driver.find_element(By.CSS_SELECTOR, ls.news_block_css)
            assert news_block, 'Блок новостей не найден на странице'
        ElementUtils.force_scroll(driver=self.driver, web_element=news_block)
        ElementUtils.take_screenshot(driver=self.driver)
        with allure.step('Проверить видимость блока новостей на странице'):
            news_block_is_displayed = self.driver.find_element(By.CSS_SELECTOR, ls.news_block_css).is_displayed()
            assert news_block_is_displayed, 'Блок новостей не отобразился'

    @allure.step('Проверить отображение ссылки на раздел главных новостей')
    def check_displaying_link_to_main_news(self):
        main_news_link = self.driver.find_element(By.CSS_SELECTOR, ls.main_news_css).is_displayed()
        assert main_news_link, 'Ссылка на раздел главных новостей не отобразилась'

    @allure.step('Проверить отображение ссылки на раздел региональных новостей')
    def check_displaying_link_to_regional_news(self):
        regional_news_link = self.driver.find_element(By.CSS_SELECTOR, ls.regional_news_css).is_displayed()
        assert regional_news_link, 'Ссылка на раздел региональных новостей не отобразилась'

    @allure.step('Проверить отображение 5 ссылок на новости')
    def check_displaying_five_link_to_news(self) -> int:
        with allure.step('Проверить наличие пяти ссылок на новости в коде новостного блока'):
            news_links = self.driver.find_elements(By.CSS_SELECTOR, ls.other_news_item_css)
            assert len(news_links) == 5, 'В блоке новостей найдено не 5 ссылок на новости'
        ElementUtils.check_display_passed_elements(driver=self.driver, elements=news_links)
        return len(news_links)

    @allure.step('Проверить отображение ссылки "Показать еще"')
    def check_displaying_link_to_show_more(self):
        with allure.step('Проверить наличие ссылки "Показать еще" в коде новостного блока'):
            show_more_link = self.driver.find_element(By.XPATH, ls.show_more_xpath)
        with allure.step('Проверить отображение ссылки "Показать еще"'):
            show_more_link.is_displayed()
            assert show_more_link, 'Ссылка "Показать еще" не отобразилась'
        return show_more_link

    @allure.step('Проверить работоспособность ссылки "Показать еще"')
    def check_functionality_show_more(self, initial_count_links, show_more_element):
        for index in range(2):
            with allure.step('Кликнуть по ссылке'):
                show_more_element.click()
            ElementUtils.force_scroll(driver=self.driver, web_element=show_more_element)
            with allure.step('Получить новую информацию о кол-ве ссылок'):
                news_links = self.driver.find_elements(By.CSS_SELECTOR, ls.other_news_item_css)
                all_count_news_links = len(news_links)
            ElementUtils.check_display_passed_elements(driver=self.driver, elements=news_links)
            ElementUtils.take_screenshot(driver=self.driver)

            with allure.step('Проверить увеличение кол-ва новостных ссылок'):
                if index == 0:
                    assert all_count_news_links >= initial_count_links + 5, 'Клик по ссылке не сработал.'
                else:
                    assert all_count_news_links >= initial_count_links + 10, 'Клик по ссылке не сработал.'

    @allure.step('Проверить отображение ссылки "Свернуть"')
    def check_displaying_link_to_collapse(self):
        with allure.step('Проверить наличие ссылки "Свернуть" в коде новостного блока'):
            collapse_link = self.driver.find_element(By.XPATH, ls.collapse_xpath)
        with allure.step('Проверить отображение ссылки "Свернуть"'):
            collapse_link.is_displayed()
            assert collapse_link, 'Ссылка "Свернуть" не отобразилась'

    @allure.step('Проверить работоспособность ссылки "Свернуть"')
    def check_functionality_collapse(self, initial_count_links):
        with allure.step('Проверить наличие ссылки "Свернуть" в коде новостного блока'):
            collapse_link = self.driver.find_element(By.XPATH, ls.collapse_xpath)
        with allure.step('Кликнуть по ссылке "Свернуть" в коде новостного блока'):
            collapse_link.click()
        with allure.step('Проверить скрытие ссылки "Свернуть"'):
            time.sleep(1.0)
            collapse_count = len(self.driver.find_elements(By.XPATH, ls.collapse_xpath))
            assert collapse_count == 0, 'Ссылка "Свернуть" не скрылась'
        with allure.step('Получить новую информацию о кол-ве ссылок'):
            news_links = self.driver.find_elements(By.CSS_SELECTOR, ls.other_news_item_css)
            all_count_news_links = len(news_links)
        ElementUtils.check_display_passed_elements(driver=self.driver, elements=news_links)
        ElementUtils.take_screenshot(driver=self.driver)
        with allure.step('Проверить уменьшение кол-ва новостных ссылок'):
            assert all_count_news_links == initial_count_links, 'Клик по ссылке не сработал.'
