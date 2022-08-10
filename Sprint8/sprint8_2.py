import unittest


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):

    def test_int_positive(self):
        expected = 5.0
        actual=divide(10, 2)
        self.assertEqual(actual, expected)

    def test_int_negative(self):
        expected = -5.0
        actual=divide(-10, 2)
        self.assertEqual(actual, expected)    
    
    def test_float(self):
        expected = 0.5
        actual=divide(2, 4)
        self.assertEqual(actual, expected)

    def test_float_period(self):
        expected = 0.3333333333
        actual=divide(1, 3)
        self.assertAlmostEqual(actual, expected, 10)

    def test_raises(self):
        self.assertRaises(Exception, divide, 3, 0)


if __name__ == '__main__':
    unittest.main()
