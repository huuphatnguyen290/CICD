# test_spending_tracker.py

import unittest
from spending_tracker import calculate_total, calculate_average, get_top_category, add_expense


class TestSpendingTracker(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"desc": "Lunch", "amount": 12.50, "category": "Food"},
            {"desc": "Bus fare", "amount": 3.00, "category": "Transport"},
            {"desc": "Dinner", "amount": 20.00, "category": "Food"},
        ]

    def test_calculate_total(self):
        self.assertAlmostEqual(calculate_total(self.expenses), 35.50, places=2)

    def test_calculate_total_empty(self):
        self.assertEqual(calculate_total([]), 0)

    def test_calculate_average(self):
        self.assertAlmostEqual(calculate_average(self.expenses), 11.83, places=2)

    def test_calculate_average_empty(self):
        self.assertEqual(calculate_average([]), 0)

    def test_get_top_category(self):
        self.assertEqual(get_top_category(self.expenses), "Food")

    def test_get_top_category_empty(self):
        self.assertIsNone(get_top_category([]))

    def test_add_expense_valid(self):
        add_expense(self.expenses, "Coffee", 5.00, "Food")
        self.assertEqual(len(self.expenses), 4)

    def test_add_expense_invalid_amount(self):
        with self.assertRaises(ValueError):
            add_expense(self.expenses, "Coffee", -5.00, "Food")

    def test_add_expense_empty_desc(self):
        with self.assertRaises(ValueError):
            add_expense(self.expenses, "", 5.00, "Food")


if __name__ == "__main__":
    unittest.main()