# 2. Инкапсулировать оба параметра (название и цену)
# товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы
# будет сгенерирована ошибка выполнения.



class ItemDiscount:
	def __init__(self, name, price):
		self.__name = name
		self.__price = price


class ItemDiscountReport(ItemDiscount):
	def get_parent_data(self):
		return f'Название товара: {self.name}, цена: {self.price}'


OBJ = ItemDiscountReport('Epson', 1000)
print(OBJ.get_parent_data())
