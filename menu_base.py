import csv

class MenuBase:
    def __init__(self, filename):
        self.filename = filename
        self.menu = self.load_menu()

    def load_menu(self):
        menu = {}
        with open(self.filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                menu[row[0]] = {'item': row[1], 'price': float(row[2])}
        return menu

    def display_menu(self):
        print("\n--- Coffee Menu ---")
        for key, value in self.menu.items():
            print(f"{key}. {value['item']} - P{value['price']:.2f}")