#class & metod:

class Product(object):
	price = 0
	number = 0
	vat = 1.25

	def price_with_vat(self):
		return self.price * self.number * self.vat

robot = Product()
robot.price = 900
robot.number = 2

book = Product()
book.price = 100
book.number = 1
book.vat = 1.06

print robot.price_with_vat() + book.price_with_vat()