import csv  # Importing the csv module for reading and writing CSV files
from menu_base import MenuBase  # Importing the MenuBase class from the menu_base module

class MenuManager(MenuBase):  # Defining the MenuManager class which inherits from MenuBase

    def save_menu(self):  # Defining the method to save the menu to a CSV file
        with open(self.filename, 'w', newline='') as file:  # Opening the CSV file in write mode
            writer = csv.writer(file)  # Creating a CSV writer object
            writer.writerow(['id', 'item', 'price'])  # Writing the header row
            for key, value in self.menu.items():  # Iterating over each item in the menu dictionary
                writer.writerow([key, value['item'], value['price']])  # Writing each item to the CSV file

    def add_item(self):  # Defining the method to add a new item to the menu
        new_id = str(len(self.menu) + 1)  # Generating a new ID for the item
        item_name = ""  # Initializing item_name variable
        item_price = 0  # Initializing item_price variable
        try:  # Starting a try-except block
            item_name = input("Enter the name of the new item: ").strip()  # Getting user input for the new item name
            if item_name == "":  # If the user leaves the item name blank
                raise Exception("Leaving item name blank returns to Option Menu")  # Raise an exception with a custom error message
        except Exception as e:  # Catching any exceptions
            print(e)  # Printing the exception message
        else:  # If no exception is raised
            while True:  # Starting a loop for getting the item price
                try:  # Starting a try-except block
                    item_price = float(input("Enter the price of the new item: ").strip())  # Getting user input for the new item price
                    break  # Exiting the loop if a valid price is entered
                except ValueError:  # Catching ValueError if the entered price is not a valid float
                    print("Please enter a numeric value")  # Printing an error message
            self.menu[new_id] = {'item': item_name, 'price': item_price}  # Adding the new item to the menu dictionary
            self.save_menu()  # Saving the updated menu to the CSV file
            self.display_menu()  # Displaying the updated menu
            print(f"Item {item_name} added successfully.")  # Printing a success message

    def update_item(self):  # Defining the method to update an existing item in the menu
        self.display_menu()  # Displaying the current menu
        item_id = input("Enter the item number to update: ").strip()  # Getting user input for the item number to update
        if item_id in self.menu:  # Checking if the entered item number exists in the menu
            item_name = input(f"Enter the new name for {self.menu[item_id]['item']} (or press enter to keep current): ").strip()  # Getting user input for the new item name
            item_price = input(f"Enter the new price for {self.menu[item_id]['item']} (or press enter to keep current): ").strip()  # Getting user input for the new item price
            if item_name:  # If a new item name is provided
                self.menu[item_id]['item'] = item_name  # Updating the item name in the menu dictionary
            if item_price:  # If a new item price is provided
                self.menu[item_id]['price'] = float(item_price)  # Updating the item price in the menu dictionary
            self.save_menu()  # Saving the updated menu to the CSV file
            self.display_menu()  # Displaying the updated menu
            print(f"Item {item_id} updated successfully.")  # Printing a success message
        else:  # If the entered item number does not exist in the menu
            print("Invalid item number.")  # Printing an error message

    def delete_item(self):  # Defining the method to delete an existing item from the menu
        self.display_menu()  # Displaying the current menu
        item_id = input("Enter the item number to delete: ").strip()  # Getting user input for the item number to delete
        if item_id in self.menu:  # Checking if the entered item number exists in the menu
            del self.menu[item_id]  # Deleting the item from the menu dictionary
            self.save_menu()  # Saving the updated menu to the CSV file
            self.display_menu()  # Displaying the updated menu
            print(f"Item {item_id} deleted successfully.")  # Printing a success message
        else:  # If the entered item number does not exist in the menu
            print("Invalid item number.")  # Printing an error message