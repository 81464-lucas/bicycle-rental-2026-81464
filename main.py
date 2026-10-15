from bicycle import Bicycle


def show_menu():
    print("\nBicycle Rental System")
    print("1. View bicycles")
    print("2. Rent a bicycle")
    print("3. Return a bicycle")
    print("4. Calculate rental cost")
    print("5. Exit")


def find_bicycle(bicycles, bicycle_id):
    for bicycle in bicycles:
        if bicycle.item_id.lower() == bicycle_id.lower():
            return bicycle
    return None


def main():
    bicycles = [
        Bicycle("B001", "Mountain Bike", 15.00, "Mountain"),
        Bicycle("B002", "City Bike", 10.00, "City"),
        Bicycle("B003", "Electric Bike", 25.00, "Electric"),
        Bicycle("B004", "Road Bike", 18.00, "Road"),
    ]

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAvailable bicycles:")
            for bicycle in bicycles:
                print(bicycle)

        elif choice == "2":
            bicycle_id = input("Enter bicycle ID: ").strip()
            bicycle = find_bicycle(bicycles, bicycle_id)

            if bicycle is None:
                print("Bicycle not found.")
                continue

            try:
                print(bicycle.rent())
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            bicycle_id = input("Enter bicycle ID: ").strip()
            bicycle = find_bicycle(bicycles, bicycle_id)

            if bicycle is None:
                print("Bicycle not found.")
                continue

            try:
                print(bicycle.return_item())
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "4":
            bicycle_id = input("Enter bicycle ID: ").strip()
            bicycle = find_bicycle(bicycles, bicycle_id)

            if bicycle is None:
                print("Bicycle not found.")
                continue

            try:
                days = int(input("Enter number of rental days: ").strip())
                cost = bicycle.calculate_rental_cost(days)
                print(f"Total rental cost: €{cost:.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")


if __name__ == "__main__":
    main()
