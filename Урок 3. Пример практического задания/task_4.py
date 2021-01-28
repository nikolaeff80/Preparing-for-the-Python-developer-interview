# 4. Написать программу, в которой реализовать две функции.
#
# В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
#
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
# Например:
# [91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
# и
# ['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
# 'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']
#
#
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение.
# Например:
# 91 zmsebjvdgi
#
# 42 ychpwljtzn
#
# ...
#
# Первая функция должна возвращать ссылку на файловый дескриптор
#
#
# После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
# Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.


import os
import random
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


def print_text_file(f_descr):
    """Вывод содержимого файла"""
    with open(f_descr.name, 'r', encoding='utf-8') as descriptor:
        for line in descriptor:
            print(line)


DESCRIPTOR = create_text_file("first_file.txt")

print_text_file(DESCRIPTOR)
