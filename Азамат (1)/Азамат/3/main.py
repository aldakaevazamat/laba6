import os

# --- НАСТРОЙКА ПУТЕЙ ---
base_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(base_dir, "source_data", "input_lab5.txt")
output_file_path = os.path.join(base_dir, "output_results", "output_lab5.txt")


# --- ФУНКЦИЯ СОЗДАНИЯ ФАЙЛА (если его нет) ---
def create_test_files_if_not_exist():
    os.makedirs(os.path.dirname(input_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Тестовые данные: размерность (3 4) и сама матрица
    initial_data = (
        "3 4\n"
        "-5 3 2 -1\n"
        "4 -2 0 5\n"
        "1 6 -3 2\n"
    )

    if not os.path.exists(input_file_path):
        with open(input_file_path, "w", encoding="utf-8") as f:
            f.write(initial_data)
        print(f"Создан файл с тестовыми данными: {input_file_path}")


# --- ФУНКЦИИ ОБРАБОТКИ ---
def count_cols_no_zeros(m):
    return sum(0 not in [m[i][j] for i in range(len(m))] for j in range(len(m[0])))


def get_char(row):
    return sum(x for x in row if x > 0 and x % 2 == 0)


# --- ОСНОВНАЯ ЛОГИКА ---
def main():
    create_test_files_if_not_exist()

    # Чтение данных
    try:
        with open(input_file_path, "r", encoding="utf-8") as f_in:
            header = f_in.readline().strip().split()
            if len(header) < 2:
                raise ValueError("В первой строке файла должны быть размеры (строки столбцы).")
            r, c = int(header[0]), int(header[1])

            matrix = []
            for line in f_in:
                if line.strip() == "":
                    continue
                row = [int(x) for x in line.split()]
                if len(row) != c:
                    raise ValueError(f"Количество элементов в строке не соответствует заявленному ({c}).")
                matrix.append(row)

            if len(matrix) != r:
                raise ValueError("Количество строк в файле не соответствует заявленному.")

    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file_path} не найден.")
        return
    except ValueError as e:
        print(f"Ошибка формата данных: {e}")
        return

    # Обработка
    cols_no_zeros = count_cols_no_zeros(matrix)
    matrix.sort(key=get_char)

    # Запись результатов
    with open(output_file_path, "w", encoding="utf-8") as f_out:
        f_out.write("=" * 60 + "\n")
        f_out.write("Лабораторная работа №5 (Файловый ввод/вывод)\n")
        f_out.write("=" * 60 + "\n")
        f_out.write("-" * 60 + "\n")
        f_out.write(f"1. Столбцов без нулей: {cols_no_zeros}\n")
        f_out.write("-" * 60 + "\n")
        f_out.write("2. Отсортированная матрица (по сумме полож. четных):\n")

        for row in matrix:
            row_str = " ".join(f"{x:4d}" for x in row)
            char_val = get_char(row)
            f_out.write(f"[ {row_str} ]  -> сумма: {char_val}\n")

        f_out.write("=" * 60 + "\n")

    print(f"Программа успешно выполнена. Результаты сохранены в {output_file_path}")


if __name__ == "__main__":
    main()