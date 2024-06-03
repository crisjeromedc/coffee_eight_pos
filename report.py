import csv  # Importing the csv module for reading CSV files

class Report:  # Defining the Report class

    def __init__(self, filename):  # Defining the constructor method
        self.filename = filename  # Initializing the filename attribute with the provided filename

    def generate(self):  # Defining the method to generate the sales report
        sales = {}  # Creating an empty dictionary to store sales data
        try:  # Starting a try-except block
            with open(self.filename, newline='') as file:  # Opening the sales data file
                reader = csv.reader(file)  # Creating a CSV reader object
                for row in reader:  # Iterating over each row in the CSV file
                    item, price, quantity, _ = row  # Unpacking the row data
                    quantity = int(quantity)  # Converting quantity to an integer
                    price = float(price)  # Converting price to a float
                    if item in sales:  # If the item is already in the sales dictionary
                        sales[item]['quantity'] += quantity  # Incrementing the quantity sold
                        sales[item]['total'] += price * quantity  # Updating the total sales value
                    else:  # If the item is not in the sales dictionary
                        sales[item] = {'quantity': quantity, 'total': price * quantity}  # Adding the item to the sales dictionary
            print("\n--- Sales Report ---")  # Printing a header for the sales report
            for item, data in sales.items():  # Iterating over each item in the sales dictionary
                print(f"{item}: {data['quantity']} sold, Total: P{data['total']:.2f}")  # Printing the item sales data
        except FileNotFoundError:  # Catching FileNotFoundError if the sales data file is not found
            print("No sales data available.")  # Printing a message indicating no sales data is available