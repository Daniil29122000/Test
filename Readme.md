# Speed Test

Скрипт для замера скорости скачивания по URL.

## Установка

pip install requests

## Запуск

python test.py <URL>

## Пример

python test.py https://upload.wikimedia.org/wikipedia/commons/f/ff/Pizigani_1367_Chart_10MB.jpg

## Что делает

- Принимает URL
- Делает 10 последовательных запросов к нему
- Считает среднее время запроса
- Считает объём скачанных данных
- Печатает среднюю скорость в МБ/сgey