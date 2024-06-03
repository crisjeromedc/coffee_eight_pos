import csv
from datetime import datetime

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.order = []

        self.total = 0.0

    def take_order(self):
        while True:
            print("\n--- Order Breakdown ---")
            self.display_order()
            print("-------------------")
            self.menu.display()
            choice = input("Enter the item number to order (or 'done' to finish): ").strip()
            if choice.lower() == 'done':
                break
            if choice in self.menu.menu:
                quantity = int(input(f"Enter quantity for {self.menu.menu[choice]['item']}: "))
                self.order.append({'item': self.menu.menu[choice]['item'], 'price': self.menu.menu[choice]['price'],
                                   'quantity': quantity})
                self.total += self.menu.menu[choice]['price'] * quantity
                print(f"Added {quantity} x {self.menu.menu[choice]['item']} to order. Current total: P{self.total:.2f}")
            else:
                print("Invalid choice. Please try again.")

    def display_order(self):
        for item in self.order:
            print(f"{item['quantity']} x {item['item']} - P{item['price'] * item['quantity']:.2f}")
        print(f"Total: P{self.total:.2f}")

    def print_receipt(self):
        print("\n--- Receipt ---")
        self.display_order()
        print("-------------------")
        print("Thank you for your purchase!")

    def save_order(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            for item in self.order:
                writer.writerow([item['item'], item['price'], item['quantity'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
