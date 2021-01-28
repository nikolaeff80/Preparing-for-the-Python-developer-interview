# 3. Усовершенствовать родительский класс таким образом,
# чтобы получить доступ к защищенным переменным.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Название товара: {self.get_name()}, цена: {self.get_price()}'


OBJ = ItemDiscountReport('Epson', 1000)
print(OBJ.get_parent_data())
