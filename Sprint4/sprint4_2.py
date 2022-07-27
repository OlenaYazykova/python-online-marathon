class Pizza:
    order_number=0

    def __init__(self, ingredients):
        self.ingredients=ingredients
        Pizza.order_number+=1
        self.order_number= Pizza.order_number
    
    @classmethod
    def hawaiian(cls):
        ingredients=['ham', 'pineapple']
        return cls(ingredients)

    @classmethod
    def meat_festival(cls):
        ingredients=['beef','meatball','bacon']
        return cls(ingredients)

    @classmethod
    def garden_feast(cls):
        ingredients=['spinach','olives','mushroom']
        return cls(ingredients)


p1=Pizza(["bacon","parmesan","ham"])
print(p1.ingredients)

p2=Pizza.garden_feast()
print(p2.ingredients)

p3 = Pizza.hawaiian()
print(p3.ingredients)

p4 = Pizza.meat_festival()
print(p4.ingredients)
	
p5 = Pizza(["pepperoni", "bacon"])
print(p5.ingredients)

my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])
print(my_pizza.ingredients)
	
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)
