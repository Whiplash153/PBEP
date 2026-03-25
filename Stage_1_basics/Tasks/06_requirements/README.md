Задача 6 — requirements.txt

Что сделал
- Сгенерировал файл requirements.txt через команду pip freeze > requirements.txt.
- В файл попали все установленные пакеты и их версии.
- Проверил, что файл существует и содержит список (requests, certifi, idna, urllib3, charset-normalizer).

Команды
- Создать файл:
pip freeze > requirements.txt
- Проверить:
ls -l requirements.txt
head -n 10 requirements.txt
- Установить зависимости в новом окружении:
pip install -r requirements.txt

Ожидаемый результат
- В проекте есть файл requirements.txt.
- В нём перечислены пакеты и их версии.
- При установке в новом окружении воспроизводится тот же набор библиотек.

Артефакты
- requirements.txt (в корне проекта)
- Tasks/06_requirements/README.md