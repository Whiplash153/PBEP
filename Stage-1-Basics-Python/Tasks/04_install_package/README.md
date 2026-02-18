Задача 4 — Установить пакет через pip

Что сделал  
- Обновил pip в активном виртуальном окружении (venv).
- Установил пакет requests.
- Проверил установку через pip list.
- Написал тестовый скрипт test_requests.py и получил Status code: 200 и JSON-ответ.

Команды
- Обновление pip.
- Установка пакета requests.
- Проверка установки (pip list).
- Запуск тестового скрипта.

Ожидаемый вывод
- В pip list есть requests и его зависимости (urllib3, idna, certifi, charset-normalizer).
- Тестовый скрипт выводит:
- Status code: 200
- JSON-ответ от сервера.

Артефакты
- Папка Tasks/04_install_package/
- Файл test_requests.py
- README.md (этот файл)
- Обновлённый requirements.txt с зафиксированными зависимостями.