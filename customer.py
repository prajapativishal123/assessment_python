import fruit_manager

def buy_fruit():
    """
    Allows customers to buy fruit.
    """
    fruit_stock = fruit_manager.load_fruit_stock()

    while True:
        print("\nFruit Market - Customer")
        print("1) View Fruit Stock")
        print("2) Buy Fruit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fruit_manager.view_fruit_stock(fruit_stock)
        elif choice == "2":
            buy_fruits(fruit_stock)
        else:
            print("Invalid choice. Please enter 1 or 2.")

        if input("Do you want to perform more operations? (y/n): ").lower() != 'y':
            break

    fruit_manager.save_fruit_stock(fruit_stock)

def buy_fruits(fruit_stock):
    """
    Processes customer fruit purchases.
    """
    fruit_manager.view_fruit_stock(fruit_stock)

    while True:
        fruit_name = input("Enter the name of the fruit you want to buy (or 'exit' to finish): ")
        if fruit_name.lower() == 'exit':
            break

        if fruit_name in fruit_stock:
            try:
                quantity = int(input(f"Enter the quantity (in kg) of {fruit_name} you want to buy: "))
                if quantity <= 0:
                    raise ValueError("Quantity must be positive.")
                if quantity <= fruit_stock[fruit_name]['qty']:
                    total_price = quantity * fruit_stock[fruit_name]['price']
                    print(f"Total price for {quantity} kg of {fruit_name}: ${total_price}")
                    if input("Confirm purchase? (y/n): ").lower() == 'y':
                        fruit_stock[fruit_name]['qty'] -= quantity
                        fruit_manager.log_transaction(f"Bought {quantity} kg of {fruit_name} for ${total_price}.")
                        print(f"Purchase successful! You bought {quantity} kg of {fruit_name}.")
                    else:
                        print("Purchase cancelled.")
                else:
                    print(f"We don't have enough {fruit_name} in stock. We have {fruit_stock[fruit_name]['qty']} kg.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print(f"Fruit '{fruit_name}' not found in stock.")
