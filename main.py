from menu import Menu
from order import Order
from report import Report
from menu_manager import MenuManager

def main():
    menu_file = 'menu.csv'
    order_file = 'orders.csv'
    menu = Menu(menu_file)
    menu_manager = MenuManager(menu_file)

    while True:
        print("\nWelcome to the Coffee Eight Shop POS System")
        print("1. Take an order")
        print("2. Generate sales report")
        print("3. Edit menu")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            order = Order(menu)
            order.take_order()
            order.print_receipt()
            order.save_order(order_file)
        elif choice == '2':
            report = Report(order_file)
            report.generate()
        elif choice == '3':
            try:
                menu_manager.display_menu()
                print("\nMenu Management")
                print("1. Add item")
                print("2. Update item")
                print("3. Delete item")
                print("4. Go back")
                menu_choice = input("Enter your choice: ").strip()
                if menu_choice > '4':
                    raise Exception("Option item not found")
                elif menu_choice == '1':
                    menu_manager.add_item()
                elif menu_choice == '2':
                    menu_manager.update_item()
                elif menu_choice == '3':
                    menu_manager.delete_item()
                elif menu_choice == '4':
                    continue
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(e)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
