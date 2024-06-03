from menu import Menu  # Importing the Menu class from the menu module
from order import Order  # Importing the Order class from the order module
from report import Report  # Importing the Report class from the report module
from menu_manager import MenuManager  # Importing the MenuManager class from the menu_manager module

def main():  # Defining the main function
    menu_file = 'menu.csv'  # Assigning the filename 'menu.csv' to the menu_file variable
    order_file = 'orders.csv'  # Assigning the filename 'orders.csv' to the order_file variable
    menu = Menu(menu_file)  # Creating an instance of the Menu class with the menu_file as a parameter
    menu_manager = MenuManager(menu_file)  # Creating an instance of the MenuManager class with the menu_file as a parameter

    while True:  # Starting an infinite loop
        print("\nWelcome to the Coffee Eight Shop POS System")  # Printing a welcome message
        print("1. Take an order")  # Printing an option to take an order
        print("2. Generate sales report")  # Printing an option to generate a sales report
        print("3. Edit menu")  # Printing an option to edit the menu
        print("4. Exit")  # Printing an option to exit the program
        choice = input("Enter your choice: ").strip()  # Getting user input for their choice and stripping any leading or trailing whitespace

        if choice == '1':  # If the user chooses option 1
            order = Order(menu)  # Creating an instance of the Order class with the menu as a parameter
            order.take_order()  # Calling the take_order method of the Order instance
            order.print_receipt()  # Calling the print_receipt method of the Order instance
            order.save_order(order_file)  # Calling the save_order method of the Order instance with the order_file as a parameter
        elif choice == '2':  # If the user chooses option 2
            report = Report(order_file)  # Creating an instance of the Report class with the order_file as a parameter
            report.generate()  # Calling the generate method of the Report instance
        elif choice == '3':  # If the user chooses option 3
            try:  # Starting a try-except block
                menu_manager.display_menu()  # Calling the display_menu method of the MenuManager instance
                print("\nMenu Management")  # Printing a menu management header
                print("1. Add item")  # Printing an option to add an item to the menu
                print("2. Update item")  # Printing an option to update an item in the menu
                print("3. Delete item")  # Printing an option to delete an item from the menu
                print("4. Go back")  # Printing an option to go back to the main menu
                menu_choice = input("Enter your choice: ").strip()  # Getting user input for their choice and stripping any leading or trailing whitespace
                if menu_choice > '4':  # If the user's choice is greater than '4'
                    raise Exception("Option item not found")  # Raise an exception with a custom error message
                elif menu_choice == '1':  # If the user chooses option 1
                    menu_manager.add_item()  # Calling the add_item method of the MenuManager instance
                elif menu_choice == '2':  # If the user chooses option 2
                    menu_manager.update_item()  # Calling the update_item method of the MenuManager instance
                elif menu_choice == '3':  # If the user chooses option 3
                    menu_manager.delete_item()  # Calling the delete_item method of the MenuManager instance
                elif menu_choice == '4':  # If the user chooses option 4
                    continue  # Continue to the next iteration of the loop
                else:  # If the user enters an invalid choice
                    print("Invalid choice. Please try again.")  # Print an error message
            except Exception as e:  # Catching any exceptions
                print(e)  # Printing the exception message
        elif choice == '4':  # If the user chooses option 4
            print("Exiting...")  # Print an exiting message
            break  # Break out of the loop and exit the program
        else:  # If the user enters an invalid choice
            print("Invalid choice. Please try again.")  # Print an error message

if __name__ == "__main__":  # If the script is executed as the main program
    main()  # Call the main function