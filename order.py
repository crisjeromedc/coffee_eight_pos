import csv  # Importing the csv module for reading and writing CSV files
from datetime import datetime  # Importing the datetime class from the datetime module

class Order:  # Defining the Order class

    def __init__(self, menu):  # Defining the constructor method
        self.menu = menu  # Initializing the menu attribute with the provided menu object
        self.order = []  # Initializing the order attribute as an empty list to store the ordered items
        self.total = 0.0  # Initializing the total attribute to store the total cost of the order

    def take_order(self):  # Defining the method to take the order
        while True:  # Starting an infinite loop
            print("\n--- Order Breakdown ---")  # Printing a header for the order breakdown
            self.display_order()  # Calling the display_order method to display the current order
            print("-------------------")  # Printing a separator
            self.menu.display()  # Displaying the menu using the display method of the menu object
            choice = input("Enter the item number to order (or 'done' to finish): ").strip()  # Getting user input for the item number to order
            if choice.lower() == 'done':  # If the user enters 'done'
                break  # Exiting the loop
            if choice in self.menu.menu:  # If the entered item number is valid
                quantity = int(input(f"Enter quantity for {self.menu.menu[choice]['item']}: "))  # Getting user input for the quantity
                self.order.append({'item': self.menu.menu[choice]['item'], 'price': self.menu.menu[choice]['price'],
                                   'quantity': quantity})  # Adding the ordered item to the order list
                self.total += self.menu.menu[choice]['price'] * quantity  # Updating the total cost of the order
                print(f"Added {quantity} x {self.menu.menu[choice]['item']} to order. Current total: P{self.total:.2f}")  # Printing a confirmation message
            else:  # If the entered item number is invalid
                print("Invalid choice. Please try again.")  # Printing an error message

    def display_order(self):  # Defining the method to display the current order
        for item in self.order:  # Iterating over each item in the order
            print(f"{item['quantity']} x {item['item']} - P{item['price'] * item['quantity']:.2f}")  # Printing the item quantity, name, and subtotal
        print(f"Total: P{self.total:.2f}")  # Printing the total cost of the order

    def print_receipt(self):  # Defining the method to print the receipt
        print("\n--- Receipt ---")  # Printing a header for the receipt
        self.display_order()  # Calling the display_order method to display the current order
        print("-------------------")  # Printing a separator
        print("Thank you for your purchase!")  # Printing a thank you message

    def save_order(self, filename):  # Defining the method to save the order to a CSV file
        with open(filename, 'a', newline='') as file:  # Opening the CSV file in append mode
            writer = csv.writer(file)  # Creating a CSV writer object
            for item in self.order:  # Iterating over each item in the order
                writer.writerow([item['item'], item['price'], item['quantity'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')])  # Writing the item details to the CSV file along with the current timestamp