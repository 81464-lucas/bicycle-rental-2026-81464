from abc import ABC, abstractmethod


class RentalItem(ABC):
    """Abstract base class for items that can be rented."""

    def __init__(self, item_id, name, daily_rate):
        self.item_id = self._validate_text(item_id, "Item ID")
        self.name = self._validate_text(name, "Name")
        self.daily_rate = self._validate_price(daily_rate)
        self.is_available = True

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string.")
        return value.strip()

    @staticmethod
    def _validate_price(value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Daily rate must be a number.")
        if value <= 0:
            raise ValueError("Daily rate must be greater than zero.")
        return float(value)

    @abstractmethod
    def calculate_rental_cost(self, days):
        """Calculate the total rental cost."""
        pass

    @abstractmethod
    def rent(self):
        """Rent the item."""
        pass

    @abstractmethod
    def return_item(self):
        """Return the item."""
        pass

    @classmethod
    def from_string(cls, data):
        """Create a rental item from a comma-separated string."""
        parts = data.strip().split(",")

        if len(parts) != 3:
            raise ValueError("Data must contain item ID, name and daily rate.")

        item_id, name, daily_rate = parts
        return cls(item_id.strip(), name.strip(), float(daily_rate.strip()))

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return (
            f"{self.__class__.__name__}("
            f"ID: {self.item_id}, Name: {self.name}, "
            f"Daily rate: €{self.daily_rate:.2f}, Status: {status})"
        )
