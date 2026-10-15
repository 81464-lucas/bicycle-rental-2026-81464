import pytest

from bicycle import Bicycle
from rental_item import RentalItem


def test_bicycle_is_subclass_of_rental_item():
    bicycle = Bicycle("B001", "City Bike", 10.00)
    assert isinstance(bicycle, RentalItem)


def test_bicycle_created_correctly():
    bicycle = Bicycle("B001", "City Bike", 10.00, "City")
    assert bicycle.item_id == "B001"
    assert bicycle.name == "City Bike"
    assert bicycle.daily_rate == 10.00
    assert bicycle.bicycle_type == "City"
    assert bicycle.is_available is True


def test_invalid_empty_id():
    with pytest.raises(ValueError):
        Bicycle("", "City Bike", 10.00)


def test_invalid_empty_name():
    with pytest.raises(ValueError):
        Bicycle("B002", "   ", 10.00)


def test_invalid_daily_rate():
    with pytest.raises(ValueError):
        Bicycle("B003", "Road Bike", 0)


def test_calculate_rental_cost():
    bicycle = Bicycle("B004", "Mountain Bike", 15.50)
    assert bicycle.calculate_rental_cost(4) == 62.00


def test_invalid_rental_days():
    bicycle = Bicycle("B005", "Road Bike", 18.00)
    with pytest.raises(ValueError):
        bicycle.calculate_rental_cost(0)


def test_rent_bicycle():
    bicycle = Bicycle("B006", "Electric Bike", 25.00)
    assert bicycle.rent() is True
    assert bicycle.is_available is False


def test_rent_unavailable_bicycle():
    bicycle = Bicycle("B007", "Electric Bike", 25.00)
    bicycle.rent()
    with pytest.raises(RuntimeError):
        bicycle.rent()


def test_return_bicycle():
    bicycle = Bicycle("B008", "City Bike", 10.00)
    bicycle.rent()
    assert bicycle.return_item() is True
    assert bicycle.is_available is True


def test_return_available_bicycle():
    bicycle = Bicycle("B009", "City Bike", 10.00)
    with pytest.raises(RuntimeError):
        bicycle.return_item()


def test_from_string():
    bicycle = Bicycle.from_string("B010, Folding Bike, 12.50", "Folding")
    assert bicycle.item_id == "B010"
    assert bicycle.name == "Folding Bike"
    assert bicycle.daily_rate == 12.50
    assert bicycle.bicycle_type == "Folding"


def test_from_string_invalid_format():
    with pytest.raises(ValueError):
        Bicycle.from_string("B011,Folding Bike")
