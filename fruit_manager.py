import json
import logging
import os

STOCK_FILE = 'data/stock.json'
LOG_FILE = 'logs/transactions.log'

# Ensure the directory for the log file exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_transaction(transaction):
    logging.info(transaction)

def load_fruit_stock():
    try:
        with open(STOCK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_fruit_stock(fruit_stock):
    os.makedirs(os.path.dirname(STOCK_FILE), exist_ok=True)  # Ensure directory for stock file exists
    with open(STOCK_FILE, 'w') as file:
        json.dump(fruit_stock, file)

def manage_fruit():
    """
    Manages the fruit stock.
    """
    fruit_stock = load_fruit_stock()

    while True:
        print("\nFruit Market Manager")
        print("1) Add Fruit Stock")
        print("2) View Fruit Stock")
        print("3) Update Fruit Stock")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_fruit_stock(fruit_stock)
        elif choice == "2":
            view_fruit_stock(fruit_stock)
        elif choice == "3":
            update_fruit_stock(fruit_stock)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        if input("Do you want to perform more operations? (y/n): ").lower() != 'y':
            break

    save_fruit_stock(fruit_stock)

def add_fruit_stock(fruit_stock):
    """
    Adds fruit to the stock.
    """
    try:
        fruit_name = input("Enter fruit Name: ")
        quantity = int(input("Enter qty (in kg): "))
        price = int(input("Enter price: "))

        if quantity < 0 or price < 0:
            raise ValueError("Quantity and price must be positive.")

        fruit_stock[fruit_name] = {'qty': quantity, 'price': price}
        log_transaction(f"Added {quantity} kg of {fruit_name} at ${price}/kg to stock.")
        print(f"Fruit '{fruit_name}' added to stock.")
    except ValueError as e:
        print(f"Error: {e}")

def view_fruit_stock(fruit_stock):
    """
    Displays the current fruit stock.
    """
    print("\nView All Stocks:")
    if fruit_stock:
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: {details['qty']} kg at ${details['price']}/kg")
    else:
        print("No stock available.")

def update_fruit_stock(fruit_stock):
    """
    Updates the fruit stock.
    """
    try:
        fruit_name = input("Enter fruit Name: ")
        if fruit_name in fruit_stock:
            quantity = int(input("Enter new qty (in kg): "))
            price = int(input("Enter new price: "))

            if quantity < 0 or price < 0:
                raise ValueError("Quantity and price must be positive.")

            fruit_stock[fruit_name] = {'qty': quantity, 'price': price}
            log_transaction(f"Updated {fruit_name} to {quantity} kg at ${price}/kg in stock.")
            print(f"Fruit '{fruit_name}' stock updated.")
        else:
            print(f"Fruit '{fruit_name}' not found in stock.")
    except ValueError as e:
        print(f"Error: {e}")
