import unittest

class TriangleNotValidArgumentException(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        return self.data

class TriangleNotExistException(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        return self.data

class Triangle:
    def __init__(self, data):
        self.check_data(data)
        self.a = data[0]
        self.b = data[1]
        self.c = data[2]
    
    def check_data(self, data):
        if isinstance(data, tuple) == True and len(data) == 3:
            for item in data:
                if isinstance(item, int) != True:
                    raise TriangleNotValidArgumentException("Not valid arguments")
        else:
            raise TriangleNotValidArgumentException("Not valid arguments")
            
        if not (data[0]<data[1]+data[2] and data[1]<data[0]+data[2] and data[2]<data[0]+data[1]):
            raise TriangleNotExistException("Can`t create triangle with this arguments")       

    def get_area(self):
        p = (self.a + self.b + self.c)/2
        area = ((p)*(p - self.a)*(p - self.b)*(p - self.c))**0.5
        return area

class TriangleTest(unittest.TestCase):
    valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
            ]
    not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
            ]
    not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
            ]

    def setUp(self):
        self.check_valid_data=[]
        for data in TriangleTest.valid_test_data:
            self.check_valid_data.append([Triangle(data[0]).get_area(), data[1]])

    def test_valid_data(self):
        for data in self.check_valid_data:
            with self.subTest():
                self.assertAlmostEqual(data[0], data[1], 1)

    def test_raises_not_exist(self):
        for data in self.not_valid_triangle:
            with self.subTest():
                with self.assertRaises(TriangleNotExistException):
                    Triangle(data)

    def test_raises_invalid_arg(self):
        for data in self.not_valid_arguments:
            with self.subTest():
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(data)

    def tearDown(self):
        self.check_valid_data = None


if __name__ == '__main__':
    unittest.main()

#test1
# valid_test_data = [
#     (3, 4, 5),
#     (26, 25, 3),
#     (30, 29, 5),
#     (87, 55, 34),
#     (120, 109, 13),
#     (123, 122, 5)
#     ]  
# for data in valid_test_data:
#     print(Triangle(data).get_area())

#test2	
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     10
# ]
# for data in not_valid_arguments:
#     try:
#         Triangle(data)
#     except TriangleNotValidArgumentException as e:
#         print(e)

#test3
# not_valid_triangle = [
#     (1, 2, 3),
#     (1, 1, 2),
#     (7, 7, 15),
#     (100, 7, 90),
#     (17, 18, 35),
#     (127, 17, 33),
#     (145, 166, 700),
#     (1000, 2000, 1),
#     (717, 17, 7),
#     (0, 7, 7),
#     (-7, 7, 7)
# ]
# for data in not_valid_triangle:
#     try:
#         Triangle(data)
#     except TriangleNotExistException as e:
#         print(e)
