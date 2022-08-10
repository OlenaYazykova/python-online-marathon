import unittest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self, products):
        self.products=products

    def get_total_price(self):
        total_price = 0
        for item in self.products:
            if item.count<5:
                discount = 0
            elif item.count<7:
                discount = 0.05
            elif item.count<10:
                discount = 0.1 
            elif item.count<20:
                discount=0.2
            elif item.count==20:
                discount=0.3
            elif item.count>20:
                discount=0.5
            total_price += (item.price-item.price*discount)*item.count
        return total_price


class CartTest(unittest.TestCase):

    def test_discout(self):
        products = (Product('prod_1', 100, 3), 
            Product('prod_2', 200, 5), 
            Product('prod_3', 300, 6), 
            Product('prod_4', 400, 7), 
            Product('prod_5', 500, 8), 
            Product('prod_6', 600, 10), 
            Product('prod_7', 700, 15),
            Product('prod_8', 800, 20),
            Product('prod_9', 900, 25),)
        cart=Cart(products)
        expected = 44730.0
        actual=cart.get_total_price()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()


#test1
# products = (Product('p1',10,4),
# Product('p2',100,5),
# Product('p3',200,6),
# Product('p4',300,7),
# Product('p5',400,9),
# Product('p6',500,10),
# Product('p7',1000,20))
# cart = Cart(products)
# print(cart.get_total_price())
