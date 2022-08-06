class Goods:
    """Сlass defines the interface for price and discount"""
  
    def __init__(self, price, discount_strategy=None): 
        self.price=price
        self.discount_strategy=discount_strategy
    
    def price_after_discount(self):
        if self.discount_strategy:
            discount=self.discount_strategy(self)
        else:
            discount = 0
        return self.price-discount
    
    def __str__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"
          
def on_sale_discount(order):
    """Function defines 50% discount"""
    return order.price * 0.50

def twenty_percent_discount(order):
    """Function defines 20% discount"""
    return order.price * 0.20


#test1	
print(Goods(20000))
#test2
print(Goods(20000, discount_strategy = twenty_percent_discount))
#test3	
print(Goods(20000, discount_strategy = on_sale_discount))
