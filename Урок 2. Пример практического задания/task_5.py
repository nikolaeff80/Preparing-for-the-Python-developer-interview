# 5. Реализовать расчет цены товара со скидкой.
#
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
#
# Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка),
# и перегрузку метода str дочернего класса.
#
# В этом методе должна пересчитываться цена и возвращаться результат —
# цена товара со скидкой.
#
# Чтобы все работало корректно, не забудьте инициализировать дочерний
# и родительский классы
# (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
	def __init__(self, name, price):
		self.__name = name
		self.__price = price
	
	def get_name(self):
		return self.__name
	
	def get_price(self):
		return self.__price
	
	def set_price(self, price):
		self.__price = price


class ItemDiscountReport(ItemDiscount):
	def __init__(self, name, price, discount):
		super().__init__(name, price)
		self.discount = discount
	
	def get_parent_data(self):
		return f'Название товара: {self.get_name()}, цена: {self.get_price()}'
	
	def __str__(self):
		return f'Название товара: {self.get_name()}, ' \
			   f'цена со скидкой: {self.get_price() - self.discount}'


OBJ = ItemDiscountReport('Epson', 1000, 10)
print(OBJ)
