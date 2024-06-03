import csv

class Report:
    def __init__(self, filename):
        self.filename = filename

    def generate(self):
        sales = {}
        try:
            with open(self.filename, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    item, price, quantity, _ = row
                    quantity = int(quantity)
                    price = float(price)
                    if item in sales:
                        sales[item]['quantity'] += quantity
                        sales[item]['total'] += price * quantity
                    else:
                        sales[item] = {'quantity': quantity, 'total': price * quantity}
            print("\n--- Sales Report ---")
            for item, data in sales.items():
                print(f"{item}: {data['quantity']} sold, Total: P{data['total']:.2f}")
        except FileNotFoundError:
            print("No sales data available.")
