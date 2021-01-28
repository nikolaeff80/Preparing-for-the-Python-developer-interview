"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""

import random


def gen_func(start, finish):
    """Генератор случайных чисел"""
    new_lst = []
    new_dict = {}
    for _ in range(10):
        print(finish - start)
        print(random.random())
        print(start)
        rnd = int((finish - start) * random.random() + start)
        new_lst.append(rnd)
        new_dict.update({f'elem_{rnd}': rnd})

    return new_lst, new_dict


print(gen_func(7, 26))
