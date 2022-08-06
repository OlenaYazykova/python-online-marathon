class Washing:
    """The Subsystem class fo washing."""
 
    def wash(self):
        print("Washing...")
 
class Rinsing:
    """The Subsystem class fo rinsing."""
 
    def rinse(self):
        print("Rinsing...")
 
class Spinning:
    """The Subsystem class fo spinning."""
 
    def spin(self):
        print("Spinning...")
 
class WashingMachine:
    """The Facade class."""
 
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.startWashing()
 
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


#test1
WashingMachine=WashingMachine()
#test2
WashingMachine.startWashing()
