# Bicycle Rental System

CA1 project for the **Bicycle Rental System** assignment using Python and Object-Oriented Programming (OOP).

## Project description

This program manages a small collection of bicycles that can be rented and returned. It includes an abstract base class, inheritance, input validation, custom error handling and automated tests.

## Files

- `rental_item.py`: abstract `RentalItem` class.
- `bicycle.py`: `Bicycle` class that inherits from `RentalItem`.
- `main.py`: demonstration program with successful and failed cases.
- `test_bicycle.py`: automated tests using `pytest`.
- `.gitignore`: files and folders excluded from Git.

## How to run

```bash
python main.py
```

## How to run the tests

Install pytest if needed:

```bash
pip install pytest
```

Run the tests:

```bash
python -m pytest -v
```

## Features

- Abstract class `RentalItem`.
- Inheritance with `Bicycle(RentalItem)`.
- Validation for IDs, names, daily rates and rental days.
- Exceptions for invalid data and unavailable bicycles.
- Alternative constructor using `@classmethod` and `from_string()`.
- At least four bicycles in `main.py`.
- More than ten automated tests.
