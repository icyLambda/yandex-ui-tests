# CSS Селекторы
news_block_css = 'body #zen-row-0'
main_news_css = 'a#news_tab_news'
regional_news_css = 'a#news_tab_region'
other_news_item_css = '[data-blockname="topnews"] ol.news__list a.news__item'

# XPATH Локаторы
main_news_xpath = '//*[contains(@class, "card-news__active-")]//a[contains(@class, "news-story__link-")]'
regional_news_xpath = '//a[contains(@href, "dzen.ru/news/region")]'
other_news_item_xpath = '//*[contains(@class, "card-news__active-")]//a[contains(@class, "news-story__link-")]'
show_more_xpath = '//*[contains(@class, "card-news__active-")]//*[contains(text(), "Показать ещё")]'
collapse_xpath = '//*[contains(@class, "card-news__active-")]//*[contains(text(), "Свернуть")]'
