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

products = [Product(price=900, number=2, vat=1.25), Product(price=100, number=1, vat=1.06)]

total_price = 0
for product in products:
	total_price = total_price + product.price_with_vat()
	print "total price in this loop", total_price

print "total", total_price