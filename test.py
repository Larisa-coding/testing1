import unittest
from main import add, subtract, multiply, divide, remainder

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 12)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertEqual(subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 6), 17)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(20, 5), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_remainder(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 4), 2)
        with self.assertRaises(ValueError):
            remainder(10, 0)

if __name__ == '__main__':
    unittest.main()
