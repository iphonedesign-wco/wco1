import unittest

from demo_app.calculator import add, is_even


class CalculatorTests(unittest.TestCase):
    def test_add_returns_expected_sum(self) -> None:
        self.assertEqual(add(20, 22), 42)

    def test_is_even_detects_even_numbers(self) -> None:
        self.assertTrue(is_even(42))

    def test_is_even_detects_odd_numbers(self) -> None:
        self.assertFalse(is_even(41))


if __name__ == "__main__":
    unittest.main()
