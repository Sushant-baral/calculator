import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Runs before every test — fresh calculator each time"""
        self.calc = Calculator()

    # --- ADDITION ---
    def test_add_positive(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- SUBTRACTION ---
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- MULTIPLICATION ---
    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # --- DIVISION ---
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(20, 4), 5.0)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # --- HISTORY ---
    def test_history_records(self):
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        self.assertEqual(len(self.calc.get_history()), 2)

    def test_history_empty_on_start(self):
        self.assertEqual(self.calc.get_history(), [])

    def test_history_correct_entry(self):
        self.calc.add(5, 5)
        self.assertIn("5 + 5 = 10", self.calc.get_history())


if __name__ == "__main__":
    unittest.main()