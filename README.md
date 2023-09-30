# Restarunt-Menu-Managment-System-using-Pythin-and-MongoDB
Restaurant Menu System using Python and MongoDb Compass


Adding Menu Items (add_menu_item function): Allows restaurant staff to add new menu items to the database by providing the item's name, price, and category. The entered information is stored in the "menu" collection.

Displaying the Menu (display_menu function): Retrieves and displays all existing menu items from the "menu" collection in a user-friendly table format using the PrettyTable library, allowing customers and staff to view the available dishes.

Placing Orders (place_order function): Enables customers to place orders by entering their name and selecting menu items. The system calculates the total price based on the selected items and stores the order details, including the customer's name, ordered items, and total price, in the "orders" collection.

Listing All Orders (list_all_orders function): Provides staff with the ability to view all customer orders stored in the "orders" collection. It displays customer names, ordered items, and total prices, aiding in order tracking and management.

Updating Menu Items (update_menu_item function): Allows staff to update existing menu items by specifying the item's name and providing new details, including the name, price, and category. The function updates the corresponding entry in the "menu" collection, ensuring menu items remain accurate and up-to-date.

Main Menu Loop (main function): Serves as the program's control center, presenting a menu of options for users to interact with the system. Users can choose from various actions, such as adding menu items, displaying the menu, placing orders, listing all orders, updating menu items, and exiting the program.

These functionalities collectively provide a comprehensive restaurant menu management system, simplifying menu updates, automating order processing, and enhancing the overall dining experience for both customers and restaurant staff.
