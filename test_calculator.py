import unittest

from calculator import add, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(8, 2), 10)

    def test_subtract(self):
        self.assertEqual(subtract(8, 2), 6)

    def test_multiply_positive(self):
        self.assertEqual(multiply(6, 4), 24)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-3, 2), -6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_divide_exact(self):
        self.assertEqual(divide(12, 3), 4)

    def test_divide_fraction(self):
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_zero(self):
        with self.assertRaisesRegex(ValueError, "^Cannot divide by zero$"):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
