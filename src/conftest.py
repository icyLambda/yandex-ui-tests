import pytest
import allure
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from variables import data as var


@pytest.fixture(scope='session')
def config():
    with open(var.CONFIG_PATH) as config_file:
        return json.load(config_file)


@pytest.fixture(scope='session')
def validate_browser(config):
    if 'browser' not in config:
        raise Exception('Отсутствует информация о браузере в файле config.json')
    if config['browser'] not in {'chrome'}:
        raise Exception(f"'{config['browser']}' не поддерживается браузер")
    return config['browser']


@pytest.fixture(scope='session')
def validate_wait_time(config):
    if 'wait_time' not in config:
        return 10
    return config['wait_time']


@pytest.fixture
def driver(validate_browser, validate_wait_time):
    if validate_browser == 'chrome':
        options = Options()
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(executable_path=var.CHROME_DRIVER_PATH, options=options)
        driver.set_window_size(width=1366, height=768)
    else:
        raise Exception(f"{config['browser']} не поддерживается браузер")

    driver.implicitly_wait(validate_wait_time)

    with allure.step('Запустить браузер'):
        yield driver

    with allure.step('Закрыть браузер'):
        driver.quit()
