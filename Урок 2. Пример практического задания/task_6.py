# 6. Проверить на практике возможности полиморфизма.
#
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
#
# Инициализировать классы необязательно.
#
# Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара,
# а вторая — его цены.
#
# Далее реализовать выполнение каждой из функции тремя способами.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        print(self.get_name())


class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        print(self.get_price())


F_OBJ = ItemDiscountReportOne('Epson', 5)
F_OBJ.get_info()

S_OBJ = ItemDiscountReportTwo('HP', 10)
S_OBJ.get_info()

for obj in (F_OBJ, S_OBJ):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(F_OBJ)
obj_handler(S_OBJ)
