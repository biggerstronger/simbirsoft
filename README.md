***Тестовое задание для SimbirSoft***

Для запуска необходимо установить зависимости из файла ```requirements.txt```, раскатить selenium-hub и
selenium-firefox-node командой
```docker-compose up``` и запустить тесты с генерацией отчета
```pytest -k tests.py --alluredir reports && allure generate reports -o clear_reports --clean```
