from abc import ABC, abstractmethod


class RentalItem(ABC):
    def __init__(self, item_id, name, daily_rate):
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("item_id must be a non-empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string.")
        if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
            raise ValueError("daily_rate must be a positive number.")

        self.item_id = item_id.strip()
        self.name = name.strip()
        self.daily_rate = float(daily_rate)
        self.is_available = True

    @classmethod
    def from_string(cls, data):
        if not isinstance(data, str):
            raise TypeError("data must be a string.")

        parts = [part.strip() for part in data.split(",")]
        if len(parts) != 3:
            raise ValueError("data must have the format: id,name,daily_rate")

        item_id, name, daily_rate = parts
        try:
            daily_rate = float(daily_rate)
        except ValueError as error:
            raise ValueError("daily_rate must be a number.") from error

        return cls(item_id, name, daily_rate)

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def return_item(self):
        pass
