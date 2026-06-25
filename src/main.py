import sys
import os

from scanner import scan_folder, print_files_info
from duplicates import find_duplicates, print_duplicates


def print_usage():
    """Вывод справки по использованию"""
    print("=" * 80)
    print("🔍 КОНСОЛЬНЫЙ ИНДЕКСАТОР ПАПОК (упрощенная версия)")
    print("=" * 80)
    print("\nИспользование:")
    print("  python main.py <путь_к_папке> [--backup <путь_к_бэкапу>]")
    print("\nПримеры:")
    print("  python main.py C:/Users/Егор/Documents")
    print("  python main.py C:/Users/Егор/Documents --backup D:/Backup")
    print("=" * 80)


def parse_args():
    """Разбор аргументов командной строки"""
    folder_path = None
    backup_path = None

    for i, arg in enumerate(sys.argv[1:]):
        if arg == '--backup' and i + 1 < len(sys.argv[1:]):
            backup_path = sys.argv[i + 2]
        elif not arg.startswith('--') and folder_path is None:
            folder_path = arg

    return folder_path, backup_path


def main():
    """Точка входа программы"""
    folder_path, backup_path = parse_args()

    # Проверка наличия пути к папке
    if folder_path is None:
        print_usage()
        sys.exit(1)

    # Проверка существования папки
    if not os.path.exists(folder_path):
        print(f"❌ Ошибка: Папка '{folder_path}' не существует")
        sys.exit(1)

    if not os.path.isdir(folder_path):
        print(f"❌ Ошибка: '{folder_path}' не является папкой")
        sys.exit(1)

    print(f"\n🔍 СКАНИРОВАНИЕ ПАПКИ: {folder_path}")
    print("=" * 80)

    # 1. Сканирование папки
    files_info, stats = scan_folder(folder_path)
    print_files_info(files_info, stats)

    # 2. Поиск дубликатов
    duplicates = find_duplicates(files_info)
    print_duplicates(duplicates)

    print("\n" + "=" * 80)
    print("✅ Сканирование завершено")
    print("=" * 80)


if __name__ == "__main__":
    main()