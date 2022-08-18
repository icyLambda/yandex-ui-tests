import allure
from pages.yandex import YandexPage


@allure.feature('Тестирование страницы Yandex.Ru')
@allure.story('Проверка наличия блока новостей на странице Yandex.Ru')
@allure.severity('blocker')
def test_news_block_on_yandex(driver):
    search_page = YandexPage(driver)
    search_page.load_yandex_page()
    search_page.check_page_loading_yandex()

    search_page.check_display_news_block()
    search_page.check_displaying_link_to_main_news()
    search_page.check_displaying_link_to_regional_news()

    initial_count_links = search_page.check_displaying_five_link_to_news()

    show_more_element = search_page.check_displaying_link_to_show_more()
    search_page.check_functionality_show_more(initial_count_links, show_more_element)

    search_page.check_displaying_link_to_collapse()
    search_page.check_functionality_collapse(initial_count_links)

    search_page.check_displaying_link_to_show_more()
