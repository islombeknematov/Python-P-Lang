class Item:
	def calc_total_price(self, x, y):
		return x * y



item1 = Item()
item1.name = 'Acer'
item1.price = 200
item1.quantity = 3
print(item1.calc_total_price(item1.price, item1.quantity))


item2 = Item()
item2.name = 'hp'
item2.price = 150
item2.quantity = 5
print(item2.calc_total_price(item2.price, item2.quantity))


11:58