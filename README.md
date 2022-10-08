# yandex-ui-tests
UI-автотесты для Yandex.ru...

#### Стек технологий:
  1. Python 3.10.7
  2. Pytest 7.1.3
  3. Allure-pytest 2.11.0
  4. Selenium 4.5.0
  5. ChromeDriver 106.0.5249.61

#### Для запуска тестов:
  1. Создать виртуальное окружение:  
    А. В PyCharm через раздел "**Interpreter Settings**"  
    Б. В терминале "**https://docs.python.org/3/library/venv.html**").  
  2. Установить необходимые библиотеки командой в терминале: pip install -r requirements.txt.  

#### Локальный запуск из IDE PyCharm:
  1. В меню "**Project Structure**" установить папку "**src**" как "**Sources Root**".
  2. В меню "**Select Run/Debug Configuration**" выбрать "**Add Configuration**" или "**Edit Configurations**".
  3. Создать новую конфигурацию: в диалоговом окне нажать кнопку "**Add New Configuration**" → "**Python tests**".
  4. Настроить команду запуска: "**Module name**": "**name_test_file_without_dot_py.test_name**".
  5. Параметр "**Working Directory**" должен указывать на папку "**src**".
  6. В поле "**Additional Arguments**" ввести аргументы запуска тестов.

#### Пример Additional Arguments для запуска теста:
```
--showlocals --alluredir=../logs -p no:cacheprovider
```

#### Как установить Allure на Windows 10:
  1. Перейти на страницу "**https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/**"  
  2. Скачать "**allure-commandline-2.19.0.zip**"  
  3. Распаковать архив в удобном для Вас месте на диске  
  4. Добавить путь до папки в "**Переменные среды**"  
    1) Открыть свойства ПК (кликнуть правой кнопкой мыши на Мой компьютер/Этот компьютер/ПК/PC)  
    2) В правом блоке перейти по ссылке "**Дополнительные параметры системы**"  
    3) В открывшемся окне нажать кнопку "**Переменные среды**"  
    4) В переменных средах пользователя сделать двойной клик по переменной "**Path**"  
    5) Добавить путь до папки "**allure-2.19.0\bin**"  
    6) При необходимости перезагрузить ПК.

#### Для создания отчета Allure, после выполнения теста:
  1. Открыть терминал в pycharm
  2. Ввести команду "**allure serve logs --host localhost**"
  3. Нажать "**ENTER**"!
