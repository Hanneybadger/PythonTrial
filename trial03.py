#class & metod:

class Product(object):
	price = 0
	number = 0
	vat = 0

	def __init__(self, price, number, vat):
		self.price = price
		self.number = number
		self.vat = vat

	def price_with_vat(self):
		return self.price*self.number*self.vat

robot = Product(price=900, number=2, vat=1.25)

book = Product(price=100, number=1, vat=1.06)

print robot.price_with_vat() + book.price_with_vat()