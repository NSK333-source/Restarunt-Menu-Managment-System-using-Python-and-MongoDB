import pymongo
from prettytable import PrettyTable

# Initialize MongoDB client and database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Restaurant_Menu_DB"]
menu_collection = db["menu"]
order_collection = db["orders"]

# Function to add a menu item
def add_menu_item():
    item_name = input("Enter menu item name: ")

    item_price = float(input("Enter menu item price: "))
    item_category = input("Enter menu item category: ")
    menu_item = {"name": item_name, "price": item_price, "category": item_category}
    menu_collection.insert_one(menu_item)
    print("Menu item added successfully.")

# Function to display the menu
def display_menu():
    print("\nRestaurant Menu:")
    menu_items = menu_collection.find()

    # Create a table for displaying the menu
    table = PrettyTable()
    table.field_names = ["Item Name", "Category", "Price (Rs.)"]

    for item in menu_items:
        item_name = item.get('name', 'N/A')
        item_category = item.get('category', 'N/A')
        item_price = item.get('price', 0.00)

        table.add_row([item_name, item_category, f"Rs. {item_price}"])

    print(table)

# Function to place an order
def place_order():
    customer_name = input("Enter your name: ")
    display_menu()
    order_items = input("Enter menu items: ").split(',')

    total_price = 0.00
    for item_name in order_items:
        item = menu_collection.find_one({"name": item_name.strip()})
        if item:
            total_price += item["price"]

    order = {"customer_name": customer_name, "order_items": order_items, "total_price": total_price}
    order_collection.insert_one(order)
    print("Order placed successfully.")
    print("BILL: Rs." + str(total_price))

# Function to list all orders
def list_all_orders():
    orders = order_collection.find()
    print("\nAll Orders:")
    for order in orders:
        print(
            f"Customer: {order['customer_name']}, Items: {', '.join(order['order_items'])}, Total Price: Rs.{order['total_price']}")

# Function to update a menu item
def update_menu_item():
    item_name = input("Enter the name of the menu item to update: ")
    new_name = input("Enter the new name for the menu item: ")
    new_price = float(input("Enter the new price for the menu item: "))
    new_category = input("Enter the new category for the menu item: ")
    menu_collection.update_one({"name": item_name}, {"$set": {"name": new_name, "price": new_price, "category": new_category}})
    print("Menu item updated successfully.")

def main():
    while True:
        print("\nRestaurant Menu Management System")
        print("1. Add Menu Item")
        print("2. Display Menu")
        print("3. Place Order")
        print("4. List All Orders")
        print("5. Update Menu Item")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_menu_item()
        elif choice == "2":
            display_menu()
        elif choice == "3":
            place_order()
        elif choice == "4":
            list_all_orders()
        elif choice == "5":
            update_menu_item()
        elif choice == "6":
            print("THANK YOU FOR VISITING,HAVE A GREAT DAY")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
