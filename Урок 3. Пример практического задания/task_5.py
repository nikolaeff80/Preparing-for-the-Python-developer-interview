# 5. Усовершенствовать первую функцию из предыдущего примера.
#
# Необходимо просканировать текстовый файл, созданный на предыдущем задании
# и реализовать создание и запись нового текстового файла
#
# В новый текстовый файл обеспечить запись строк вида:
#
# zmsebjvdgi zmsebjvdgi
# ychpwljtzn ychpwljtzn
# ...
#
# Т.е. извлекаются строки из первого текстового файла
# а в новый они записываются в виде, где вместо числа ставится строка
#
# Здесь необходимо использовать регулярные выражения.

import os
import random
import re
from functools import reduce

LINES_COUNT = STRING_SIZE = 10


def get_random_string():
    """Генератор набора символов"""
    return reduce(lambda string, char: string + char,
                  [chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])


def create_text_file(f_name):
    """Запись файла или его открытие"""
    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as f_descr:
            return f_descr

    with open(f_name, 'w', encoding='utf-8') as f_descr:
        numbers = [random.randint(0, 100) for _ in range(LINES_COUNT)]
        strings = [get_random_string() for _ in range(LINES_COUNT)]
        f_descr.writelines(['{} {}\n'.format(number, text)
                            for number, text in zip(numbers, strings)])
        return f_descr


def print_text_file(desc):
    """Выполнение замен"""
    # файл для извлечения текста
    f_in = open(desc.name, 'r')
    # файл для записи текста
    f_out = open("second_file.txt", 'w')

    for line in f_in:
        numb = re.search(r'\d*', line)
        string = re.search(r'\s\w*', line)
        line = line.replace(numb.group(0), string.group(0))
        f_out.write(line)

    f_in.close()
    f_out.close()

    with open("second_file.txt", encoding='utf-8') as descr:
        for elem in descr:
            print(elem)


DESCRIPTOR = create_text_file("first_file.txt")

print_text_file(DESCRIPTOR)
