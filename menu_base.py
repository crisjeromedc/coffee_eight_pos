import csv  # Importing the csv module for reading CSV files

class MenuBase:  # Defining the MenuBase class

    def __init__(self, filename):  # Defining the constructor method
        self.filename = filename  # Initializing the filename attribute with the provided filename
        self.menu = self.load_menu()  # Initializing the menu attribute by calling the load_menu method

    def load_menu(self):  # Defining the method to load the menu from a CSV file
        menu = {}  # Creating an empty dictionary to store the menu items
        with open(self.filename, newline='') as file:  # Opening the CSV file
            reader = csv.reader(file)  # Creating a CSV reader object
            next(reader)  # Skipping the header row
            for row in reader:  # Iterating over each row in the CSV file
                menu[row[0]] = {'item': row[1], 'price': float(row[2])}  # Adding each menu item to the dictionary
        return menu  # Returning the loaded menu dictionary

    def display_menu(self):  # Defining the method to display the menu
        print("\n--- Coffee Menu ---")  # Printing a header for the menu
        for key, value in self.menu.items():  # Iterating over each item in the menu dictionary
            print(f"{key}. {value['item']} - P{value['price']:.2f}")  # Printing the item number, item name, and price