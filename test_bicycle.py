import unittest

from bicycle import Bicycle
from rental_item import RentalItem


class TestBicycle(unittest.TestCase):

    def setUp(self):
        self.bicycle = Bicycle("B001", "Mountain Bike", 15.00, "Mountain")

    def test_create_bicycle_successfully(self):
        self.assertEqual(self.bicycle.item_id, "B001")
        self.assertEqual(self.bicycle.name, "Mountain Bike")
        self.assertEqual(self.bicycle.daily_rate, 15.00)
        self.assertTrue(self.bicycle.is_available)

    def test_invalid_daily_rate_raises_error(self):
        with self.assertRaises(ValueError):
            Bicycle("B002", "City Bike", -5)

    def test_zero_daily_rate_raises_error(self):
        with self.assertRaises(ValueError):
            Bicycle("B002", "City Bike", 0)

    def test_empty_model_raises_error(self):
        with self.assertRaises(ValueError):
            Bicycle("B002", "   ", 10)

    def test_rent_available_bicycle(self):
        result = self.bicycle.rent()
        self.assertFalse(self.bicycle.is_available)
        self.assertIn("rented successfully", result)

    def test_rent_already_rented_bicycle_raises_error(self):
        self.bicycle.rent()
        with self.assertRaises(ValueError):
            self.bicycle.rent()

    def test_return_rented_bicycle(self):
        self.bicycle.rent()
        result = self.bicycle.return_item()
        self.assertTrue(self.bicycle.is_available)
        self.assertIn("returned successfully", result)

    def test_return_available_bicycle_raises_error(self):
        with self.assertRaises(ValueError):
            self.bicycle.return_item()

    def test_calculate_rental_cost(self):
        self.assertEqual(self.bicycle.calculate_rental_cost(3), 45.00)

    def test_zero_days_raises_error(self):
        with self.assertRaises(ValueError):
            self.bicycle.calculate_rental_cost(0)

    def test_negative_days_raises_error(self):
        with self.assertRaises(ValueError):
            self.bicycle.calculate_rental_cost(-2)

    def test_non_integer_days_raises_error(self):
        with self.assertRaises(ValueError):
            self.bicycle.calculate_rental_cost(2.5)

    def test_from_string_creates_bicycle(self):
        bicycle = Bicycle.from_string("B010,Road Bike,20.00,Road")
        self.assertEqual(bicycle.item_id, "B010")
        self.assertEqual(bicycle.name, "Road Bike")
        self.assertEqual(bicycle.daily_rate, 20.00)
        self.assertEqual(bicycle.bicycle_type, "Road")

    def test_rental_item_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            RentalItem("R001", "Generic Item", 10)


if __name__ == "__main__":
    unittest.main()
