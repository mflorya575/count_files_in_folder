import os

def count_files(folder_path):
    file_count = 0

    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)

    return file_count

if __name__ == "__main__":
    folder_path = 'C:/vs_code/html'  # Замените на свой путь
    total_files = count_files(folder_path)
    print(f"Количество файлов в папке: {total_files}")
