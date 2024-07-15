import fruit_manager
import customer

def main():
    """
    Main function for the Fruit Store console application.
    """
    while True:
        print("WELCOME TO FRUIT MARKET")
        print("1) Manager")
        print("2) Customer")
        role = input("Select your Role: ")

        if role == "1":
            fruit_manager.manage_fruit()
        elif role == "2":
            customer.buy_fruit()
        else:
            print("Invalid choice. Please enter 1 or 2.")

        if input("Do you want to perform more operations? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
