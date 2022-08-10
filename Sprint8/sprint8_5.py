import unittest


class Worker:
    def __init__(self, name, salary=0.0):
        if salary<0:
            raise ValueError("Error! The value of salary is negative!")
        self.name=name
        self.salary=salary

    def get_tax_value(self):
        tax = 0.0
        tax_range=[(0, 0), (1000, 0.1), (3000, 0.15), (5000, 0.21), (10000, 0.3), (20000, 0.4), (50000, 0.47)]
        for i in range(1, len(tax_range)):
            if i==len(tax_range)-1:
                tax += (self.salary-tax_range[i][0])*tax_range[i][1]
            if self.salary > tax_range[i][0]:
                tax += (tax_range[i][0]-tax_range[i-1][0])*tax_range[i-1][1]
            else:
                tax += (self.salary-tax_range[i-1][0])*tax_range[i-1][1]
                break
        return tax


class WorkerTest(unittest.TestCase):
    valid_test_data = [
        (('worker1', 1001), 0.1),
        (('worker2', 5500), 605.0),
        (('worker3', 60000), 21250.0),
        (('worker3'), 0.0)
        ]

    def setUp(self):
            self.check_valid_data=[]
            for data in WorkerTest.valid_test_data:
                if isinstance(data[0], tuple) == True:
                    self.check_valid_data.append([Worker(*data[0]).get_tax_value(), data[1]])
                else:
                    self.check_valid_data.append([Worker(data[0]).get_tax_value(), data[1]])

    def test_valid_data(self):
        for data in self.check_valid_data:
            with self.subTest():
                self.assertAlmostEqual(data[0], data[1], 1)
    
    @unittest.expectedFailure
    def test_expected(self):
        raise ValueError("Error! The value of salary is negative!")

    def tearDown(self):
        self.check_valid_data = None


if __name__ == '__main__':
    unittest.main()

#test1
# worker = Worker("Natasha", 1001)
# print(worker.get_tax_value())

#test2
# worker = Worker("Vika", 100000)
# print(worker.get_tax_value())

#test3
# worker = Worker("Petia", 1000)
# print(worker.get_tax_value())

#test4	
# worker = Worker("Vasia")
# print(worker.get_tax_value())
