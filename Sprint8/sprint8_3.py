import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("error")
    d = b**2-(4*a*c)
    if d > 0:
        x1 = round((-b + (d**0.5))/(2*a), 1)
        x2 = round((-b - (d**0.5))/(2*a), 1)
        return (x1, x2)
    elif d == 0:
        x1 = round(-b/(2*a), 1)
        return x1
    elif d < 0:
        return None


class QuadraticEquationTest(unittest.TestCase):

    def test_disc_positive(self):
        expected = (5.0, -0.3)
        actual=quadratic_equation(3, -14, -5)
        self.assertEqual(actual, expected)

    def test_disc_negative(self):
        expected = 3.0
        actual=quadratic_equation(3, -18, 27)
        self.assertEqual(actual, expected)    
    
    def test_disc_0(self):
        expected = None
        actual=quadratic_equation(2, 1, 67)
        self.assertEqual(actual, expected)

    def test_raises(self):
        self.assertRaises(Exception, quadratic_equation, 0, 0, 0)

if __name__ == '__main__':
    unittest.main()

#test1
# print(quadratic_equation(3, -14, -5))
# print(quadratic_equation(3, -18, 27))
# print(quadratic_equation(2, 1, 67))

#test2
# try:
#     quadratic_equation(0, 0, 0)
# except ValueError:
#     print('error')
