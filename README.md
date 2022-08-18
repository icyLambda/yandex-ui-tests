# yandex-ui-tests
UI-автотесты для Yandex.ru...

#### Стек технологий:
  1. Python 3.10.5
  2. Pytest 7.1.2
  3. Allure-pytest 2.9.45
  4. Selenium 4.4.2
  5. ChromeDriver 104.0.5112.79

#### Для запуска тестов:
  1. Создать виртуальное окружение:  
    А. В PyCharm через раздел "**Interpreter Settings**"  
    Б. В терминале "**https://docs.python.org/3/library/venv.html**").  
  2. Установить необходимые библиотеки командой в терминале: pip install -r requirements.txt.  

#### Локальный запуск из IDE PyCharm:
  1. В меню "**Project Structure**" установить папку "**src**" как "**Sources Root**".
  2. В меню "**Select Run/Debug Configuration**" выбрать "**Add Configuration**" или "**Edit Configurations**".
  3. Создать новую конфигурацию: в диалоговом окне нажать кнопку "**Add New Configuration**" → "**Python tests**".
  4. Настроить команду запуска: "**Module name**": "**test_news_block_on_yandex.test_news_block_on_yandex**".
  5. Параметр "**Working Directory**" должен указывать на папку "**src**".
  6. В поле "**Additional Arguments**" ввести аргументы запуска тестов.

#### Пример Additional Arguments для запуска теста:
```
--showlocals --alluredir=output -p no:cacheprovider
```

#### Для создания отчета Allure, после выполнения теста:
  1. Открыть терминал в pycharm
  2. Ввести команду "**allure serve src/output**"
  3. Нажать "**ENTER**"!
