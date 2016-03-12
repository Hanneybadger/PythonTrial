def metodnamn(): print "hej"

metodnamn()

def metodnamn(message): print message

metodnamn(message="hej")

+class Product(object):
+	price = 0
+	number = 0
+	vat = 0
+
+robot = Product()
+robot.price = 900
+robot.number = 2
+robot.vat = 1.25
+
+book = Product()
+book.price = 100
+book.number = 1
+book.vat = 1.06
+
+print robot.price*robot.number*robot.vat+book.price*book.number*book.vat