# CSV_processing
# Описание:
Этот проект предоставляет утилиту командной строки для обработки CSV-файлов.
Возможности:
• Фильтрация строк по условию (>, <, >=, <=, =)
• Простые агрегатные функции (min, max, sum, avg, count)
• Комбинация фильтрации и агрегации
• Поддержка любых CSV с заголовком в первой строке

Структура репозитория:
• main.py — главный исполняемый скрипт
• csv_processor — модуль с функциями загрузки, фильтрации, агрегации
• requirements.txt — список зависимостей (здесь обычно только стандартная библиотека)
• tests/ — автоматические тесты (pytest)
• README.txt — этот файл

Требования:
• Python 3.6 или новее
• (Опционально) virtualenv или venv

Установка:

Клонируйте репозиторий или скачайте архив: git clone https://github.com/ProkhorSav/CSV_processing
Создайте и активируйте виртуальное окружение (рекомендуется): python3 -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate.bat (Windows)
Установите зависимости: pip install -r requirements.txt
Использование Синтаксис: python main.py <путь_к_csv> [--where "<условие>"] [--aggregate "<функция>=<столбец>"]

Параметры: • <путь_к_csv> — файл CSV с заголовком
• --where — условие фильтрации, например "price>500", "brand=apple"
• --aggregate — агрегатная функция:
min, max, sum, avg, count
Формат: функция=имя_столбца, например "max=rating"

Примеры:

Фильтрация по цене больше 500: python main.py products.csv --where "price>500"

Средняя цена всех товаров: python main.py products.csv --aggregate "avg=price"

Максимальный рейтинг среди товаров Xiaomi: python main.py products.csv --where "brand=xiaomi" --aggregate "max=rating"

Подсчёт количества товаров Samsung: python main.py products.csv --where "brand=samsung" --aggregate "count=brand"

Тесты:

Установите pytest: pip install pytest pytest-cov
Запустите тесты: pytest --cov=csv_processor tests/

Автор: Савенков Прохор Сергеевич
