# Задание 2.	Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):
#
#     Функция принимает имя каталога и распечатывает его содержимое
#     в виде «путь и имя файла», а также любые другие
#     файлы во вложенных каталогах.
#
#     Эта функция подобна os.walk. Использовать функцию os.walk
#     нельзя. Данная задача показывает ваше умение работать с
#     вложенными структурами.
#     заполните далее


import os


def print_directory_contents(dir_path):

    def get_directory_files(dir_path):
        struct = []
        for file_or_directory in os.listdir(dir_path):
            full_name = os.path.join(os.path.abspath(dir_path), file_or_directory)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(dir_path), file_or_directory))
            else:
                struct.extend(get_directory_files(full_name))
        return struct
    return get_directory_files(dir_path)


my_res = print_directory_contents('test_folder')
print(my_res)