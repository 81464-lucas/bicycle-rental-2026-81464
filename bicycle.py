from rental_item import RentalItem


class Bicycle(RentalItem):
    """Represents a bicycle that can be rented."""

    def __init__(self, bicycle_id, model, daily_rate, bicycle_type="Standard"):
        super().__init__(bicycle_id, model, daily_rate)
        self.bicycle_type = self._validate_text(bicycle_type, "Bicycle type")

    def calculate_rental_cost(self, days):
        days = self._validate_days(days)
        return self.daily_rate * days

    def rent(self):
        if not self.is_available:
            raise ValueError(f"Bicycle {self.item_id} is already rented.")

        self.is_available = False
        return f"Bicycle {self.item_id} has been rented successfully."

    def return_item(self):
        if self.is_available:
            raise ValueError(f"Bicycle {self.item_id} is not currently rented.")

        self.is_available = True
        return f"Bicycle {self.item_id} has been returned successfully."

    @staticmethod
    def _validate_days(days):
        if not isinstance(days, int) or isinstance(days, bool):
            raise ValueError("Rental days must be a whole number.")
        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")
        return days

    @classmethod
    def from_string(cls, data):
        """Create a bicycle from a comma-separated string.

        Expected format: ID,Model,DailyRate,Type
        """
        parts = data.strip().split(",")

        if len(parts) != 4:
            raise ValueError(
                "Data must contain bicycle ID, model, daily rate and type."
            )

        bicycle_id, model, daily_rate, bicycle_type = parts
        return cls(
            bicycle_id.strip(),
            model.strip(),
            float(daily_rate.strip()),
            bicycle_type.strip(),
        )

    def __str__(self):
        return super().__str__() + f", Type: {self.bicycle_type}"
