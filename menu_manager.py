import csv
from menu_base import MenuBase
class MenuManager(MenuBase):
    def save_menu(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'item', 'price'])
            for key, value in self.menu.items():
                writer.writerow([key, value['item'], value['price']])

    def add_item(self):
        new_id = str(len(self.menu) + 1)
        item_name = ""
        item_price = 0
        try:
            item_name = input("Enter the name of the new item: ").strip()
            if item_name == "":
                raise Exception("Leaving item name blank returns to Option Menu")
        except Exception as e:
            print(e)
        else:
            # item_name = input("Enter the name of the new item: ").strip()
            while True:
                try:
                    item_price = float(input("Enter the price of the new item: ").strip())
                    break
                except ValueError:
                    print("Please enter a numeric value")
            self.menu[new_id] = {'item': item_name, 'price': item_price}
            self.save_menu()
            self.display_menu()
            print(f"Item {item_name} added successfully.")

    def update_item(self):
        self.display_menu()
        item_id = input("Enter the item number to update: ").strip()
        if item_id in self.menu:
            item_name = input(f"Enter the new name for {self.menu[item_id]['item']} (or press enter to keep current): ").strip()
            item_price = input(f"Enter the new price for {self.menu[item_id]['item']} (or press enter to keep current): ").strip()
            if item_name:
                self.menu[item_id]['item'] = item_name
            if item_price:
                self.menu[item_id]['price'] = float(item_price)
            self.save_menu()
            self.display_menu()
            print(f"Item {item_id} updated successfully.")
        else:
            print("Invalid item number.")

    def delete_item(self):
        self.display_menu()
        item_id = input("Enter the item number to delete: ").strip()
        if item_id in self.menu:
            del self.menu[item_id]
            self.save_menu()
            self.display_menu()
            print(f"Item {item_id} deleted successfully.")
        else:
            print("Invalid item number.")
