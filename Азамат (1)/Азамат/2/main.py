import random
import os

# --- НАСТРОЙКА ПУТЕЙ ---
base_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(base_dir, "source_data", "input_lab4.txt")
output_file_path = os.path.join(base_dir, "output_results", "output_lab4.txt")


# --- ФУНКЦИЯ СОЗДАНИЯ ФАЙЛА (если его нет) ---
def create_test_files_if_not_exist():
    os.makedirs(os.path.dirname(input_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Тестовые данные: 8 чисел через пробел
    initial_data = "-5.5 3.2 10.1 -2.0 7.7 -8.5 4.4 1.1\n"

    if not os.path.exists(input_file_path):
        with open(input_file_path, "w", encoding="utf-8") as f:
            f.write(initial_data)
        print(f"Создан файл с тестовыми данными: {input_file_path}")


# --- ОСНОВНАЯ ЛОГИКА ---
def main():
    create_test_files_if_not_exist()

    # Чтение данных
    try:
        with open(input_file_path, "r", encoding="utf-8") as f_in:
            content = f_in.read().split()
            arr = [float(x) for x in content]
            if not arr:
                raise ValueError("Файл пуст.")
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file_path} не найден.")
        return
    except ValueError as e:
        print(f"Ошибка формата данных в файле: {e}")
        return

    n = len(arr)

    # Вычисления
    sum_pos = sum(x for x in arr if x > 0)

    idx_max = max(range(n), key=lambda i: abs(arr[i]))
    idx_min = min(range(n), key=lambda i: abs(arr[i]))
    start, end = min(idx_max, idx_min), max(idx_max, idx_min)
    sub_array = arr[start + 1: end]

    if len(sub_array) > 0:
        product = 1
        for x in sub_array:
            product *= x
        product_str = f"{round(product, 2)}"
    else:
        product_str = "нет элементов между max и min"

    sorted_arr = sorted(arr, reverse=True)

    # Запись результатов
    with open(output_file_path, "w", encoding="utf-8") as f_out:
        f_out.write("=" * 50 + "\n")
        f_out.write("Лабораторная работа №4 (Файловый ввод/вывод)\n")
        f_out.write("=" * 50 + "\n")

        f_out.write(f"Исходный массив ({n} элементов):\n")
        for i in range(0, n, 5):
            chunk = arr[i:i + 5]
            f_out.write("  " + "  ".join(f"{x:7.2f}" for x in chunk) + "\n")

        f_out.write("-" * 50 + "\n")
        f_out.write(f"1. Сумма положительных элементов: {round(sum_pos, 2)}\n")
        f_out.write(f"2. Произведение между max и min (по модулю): {product_str}\n")

        f_out.write("3. Массив, отсортированный по убыванию:\n")
        for i in range(0, n, 5):
            chunk = sorted_arr[i:i + 5]
            f_out.write("  " + "  ".join(f"{x:7.2f}" for x in chunk) + "\n")
        f_out.write("=" * 50 + "\n")

    print(f"Программа успешно выполнена. Результаты сохранены в {output_file_path}")


if __name__ == "__main__":
    main()
