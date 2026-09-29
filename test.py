import requests   # библиотека для HTTP-запросов (нужно установить: pip install requests)
import time       # встроенная библиотека для замера времени
import sys        # встроенная библиотека для аргументов командной строки

def measure_speed(url, count=10):
    """
    Замеряет скорость скачивания по указанному URL.
    url   - адрес картинки
    count - количество запросов (по заданию 10)
    """
    total_time = 0      # суммарное время всех запросов
    total_bytes = 0     # суммарный объём скачанных данных

    print(f"Замеряю скорость для: {url}\n")

    for i in range(count):
        start = time.time()             # время ДО запроса
        response = requests.get(url)    # делаем запрос, ждём ответа
        data = response.content         # получаем тело ответа (байты)
        end = time.time()               # время ПОСЛЕ запроса

        elapsed = end - start           # время одного запроса
        total_time += elapsed
        total_bytes += len(data)        # len(байтов) = размер в байтах

        print(f"Запрос {i+1}: {elapsed:.3f} сек, {len(data)} байт")

    # Средние значения
    avg_time = total_time / count
    avg_speed_mb = (total_bytes / (1024 * 1024)) / total_time

    print("\n" + "=" * 40)
    print(f"Среднее время запроса: {avg_time:.4f} сек")
    print(f"Всего скачано:         {total_bytes / (1024 * 1024):.2f} МБ")
    print(f"Средняя скорость:      {avg_speed_mb:.2f} МБ/с")
    print("=" * 40)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python speed_test.py <URL>")
        sys.exit(1)
    test_url = sys.argv[1]
    measure_speed(test_url)