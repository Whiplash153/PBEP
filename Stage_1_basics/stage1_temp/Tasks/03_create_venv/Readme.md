
Виртуальное окружение (venv)  

Что сделано
- Создано окружение командой: python3.12 -m venv .venv  
- Активировано: source .venv/bin/activate  
- Проверена версия Python и путь: python --version, which python
- Обновлён pip и установлен пакет requests  

Артефакты
- .venv/ — папка окружения
- requirements.txt — список зависимостей
- hello.py — тестовый скрипт
- .gitignore — исключает venv и служебные файлы  

Как проверить 
1. Активировать окружение: source .venv/bin/activate
2. Запустить скрипт: python hello.py  
3. В выводе должны быть строки:
- Hello from venv!
- Версия Python (3.12.x)
- Версия requests
