from bicycle import Bicycle


def main():
    bicycles = [
        Bicycle("B001", "City Bike", 10.00, "City"),
        Bicycle("B002", "Mountain Bike", 15.50, "Mountain"),
        Bicycle("B003", "Road Bike", 18.00, "Road"),
        Bicycle.from_string("B004, Electric Bike, 25.00", "Electric"),
    ]

    print("Bicycle Rental System")
    print("-" * 40)

    for bicycle in bicycles:
        print(bicycle)

    print("\nSuccessful rental examples")
    print("-" * 40)

    bicycles[0].rent()
    print(f"{bicycles[0].name} rented for 3 days: EUR{bicycles[0].calculate_rental_cost(3):.2f}")
    bicycles[0].return_item()
    print(f"{bicycles[0].name} returned successfully.")

    bicycles[1].rent()
    print(f"{bicycles[1].name} rented for 2 days: EUR{bicycles[1].calculate_rental_cost(2):.2f}")
    bicycles[1].return_item()

    print("\nError handling examples")
    print("-" * 40)

    try:
        Bicycle("", "Invalid Bike", 10)
    except ValueError as error:
        print(f"Validation error: {error}")

    try:
        bicycles[2].rent()
        bicycles[2].rent()
    except RuntimeError as error:
        print(f"Rental error: {error}")

    bicycles[2].return_item()


if __name__ == "__main__":
    main()
