from abc import ABC, abstractmethod


class Product(ABC):
    """AbstractProduct - the base interface of products."""

    @abstractmethod
    def cook(self):
        pass

class FettuccineAlfredo(Product):
    """Concrete Product for Italian restaurant - 
    "Fettuccine Alfredo"."""

    name="Fettuccine Alfredo"
    def cook(self):
        print(f"Italian main course prepared: {self.name}")
        
class Tiramisu(Product):
    """Concrete Product for Italian restaurant - 
    "Tiramisu"."""

    name="Tiramisu"
    def cook(self):
        print(f"Italian dessert prepared: {self.name}")

class DuckALOrange(Product):
    """Concrete Product for French restaurant - 
    "Duck À L'Orange"."""

    name="Duck À L'Orange"
    def cook(self):
        print(f"French main course prepared: {self.name}")

class CremeBrulee(Product):
    """Concrete Product for French restaurant - 
    "Crème brûlée"."""

    name="Crème brûlée"
    def cook(self):
        print(f"French dessert prepared: {self.name}")

class Factory(ABC):
    """The Abstract Factory interface declares a set of 
    methods that return different abstract products."""

    @abstractmethod
    def get_dish(type_of_meal):
        pass

class ItalianDishesFactory(Factory):
    """Concrete Factory for Italian restaurant."""

    def get_dish(type_of_meal):
        if type_of_meal=="main":
            return FettuccineAlfredo()
        if type_of_meal=="dessert":
            return Tiramisu()

class FrenchDishesFactory(Factory):
    """Concrete Factory for French restaurant."""

    def get_dish(type_of_meal):
        if type_of_meal=="main":
            return DuckALOrange()
        if type_of_meal=="dessert":
            return CremeBrulee()

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory=="italian":
            return ItalianDishesFactory
        if type_of_factory=="french":
            return FrenchDishesFactory


#test1
fp=FactoryProducer()
fac=fp.get_factory("italian")
main_dish=fac.get_dish("main")
main_dish.cook()

#test2
dessert=fac.get_dish("dessert")
dessert.cook()

#test3
fac1=fp.get_factory("french")
main_dish=fac1.get_dish("main")
main_dish.cook()

#test4
dessert=fac1.get_dish("dessert")
dessert.cook()
