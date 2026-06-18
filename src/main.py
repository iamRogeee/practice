import sys
import os
from pathlib import Path


def print_usage():
    """Вывод справки по использованию"""
    print("Использование: python main.py <путь_к_папке>")
    print("Пример: python main.py /home/user/documents")


def main():
    """Точка входа программы"""
    # Проверка аргументов командной строки
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    # Получение пути к папке
    folder_path = sys.argv[1]

    # Проверка существования папки
    if not os.path.exists(folder_path):
        print(f"Ошибка: Папка '{folder_path}' не существует")
        sys.exit(1)

    if not os.path.isdir(folder_path):
        print(f"Ошибка: '{folder_path}' не является папкой")
        sys.exit(1)

    print(f"Сканирование папки: {folder_path}")
    # Здесь будет основная логика


if __name__ == "__main__":
    main()