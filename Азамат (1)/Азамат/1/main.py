import math
import os

# --- НАСТРОЙКА ПУТЕЙ ---
base_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(base_dir, "source_data", "input_lab1.txt")
output_file_path = os.path.join(base_dir, "output_results", "output_lab1.txt")

# --- ФУНКЦИЯ СОЗДАНИЯ ФАЙЛА (если его нет) ---
def create_test_files_if_not_exist():
    # 1. Создаем папки, если их нет
    os.makedirs(os.path.dirname(input_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # 2. Задаем тестовые данные (можете изменить под себя)
    initial_data = "45\n"  # Значение угла альфа

    # 3. Создаем файл, если его не существует
    if not os.path.exists(input_file_path):
        with open(input_file_path, "w", encoding="utf-8") as f:
            f.write(initial_data)
        print(f"Создан файл с тестовыми данными: {input_file_path}")


# --- ОСНОВНАЯ ЛОГИКА ---
def main():
    create_test_files_if_not_exist()  # Создаем файл, если надо

    # Чтение данных
    try:
        with open(input_file_path, "r", encoding="utf-8") as f_in:
            line = f_in.readline().strip()
            if not line:
                raise ValueError("Входной файл пуст.")
            alpha_deg = float(line)
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file_path} не найден.")
        return
    except ValueError as e:
        print(f"Ошибка формата данных в файле: {e}")
        return

    # Вычисления
    alpha = math.radians(alpha_deg)
    z1 = (
        math.cos(alpha)
        + math.sin(alpha)
        + math.cos(3 * alpha)
        + math.sin(3 * alpha)
    )
    z2 = 2 * math.sqrt(2) * math.cos(alpha) * math.sin(math.pi / 4 + 2 * alpha)
    is_match = math.isclose(z1, z2, abs_tol=1e-5)
    match_text = "Результаты совпадают!" if is_match else "Ошибка! Результаты не совпадают."

    # Запись результатов
    with open(output_file_path, "w", encoding="utf-8") as f_out:
        f_out.write("=" * 40 + "\n")
        f_out.write("Лабораторная работа №1 (Файловый ввод/вывод)\n")
        f_out.write("=" * 40 + "\n")
        f_out.write(f"Исходный угол альфа (град): {alpha_deg}\n")
        f_out.write("-" * 40 + "\n")
        f_out.write(f"Результат z1 = {z1:.6f}\n")
        f_out.write(f"Результат z2 = {z2:.6f}\n")
        f_out.write("-" * 40 + "\n")
        f_out.write(f"{match_text}\n")
        f_out.write("=" * 40 + "\n")

    print(f"Программа успешно выполнена. Результаты записаны в {output_file_path}")

if __name__ == "__main__":
    main()