from rental_item import RentalItem


class Bicycle(RentalItem):
    def __init__(self, item_id, name, daily_rate, bicycle_type="Standard"):
        super().__init__(item_id, name, daily_rate)

        if not isinstance(bicycle_type, str) or not bicycle_type.strip():
            raise ValueError("bicycle_type must be a non-empty string.")

        self.bicycle_type = bicycle_type.strip()

    @classmethod
    def from_string(cls, data, bicycle_type="Standard"):
        bicycle = super().from_string(data)
        return cls(
            bicycle.item_id,
            bicycle.name,
            bicycle.daily_rate,
            bicycle_type,
        )

    def calculate_rental_cost(self, days):
        if not isinstance(days, int) or days <= 0:
            raise ValueError("days must be a positive whole number.")
        return self.daily_rate * days

    def rent(self):
        if not self.is_available:
            raise RuntimeError(f"Bicycle {self.item_id} is not available.")
        self.is_available = False
        return True

    def return_item(self):
        if self.is_available:
            raise RuntimeError(f"Bicycle {self.item_id} was not rented.")
        self.is_available = True
        return True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"{self.item_id}: {self.name} ({self.bicycle_type}) - EUR{self.daily_rate:.2f}/day - {status}"
