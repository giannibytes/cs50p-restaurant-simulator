### RESTAURANT SIMULATOR ###


from tabulate import tabulate


# Order class to save table id and order details
class Order:
    def __init__(self, table_id, order_details):
        self.table_id = table_id
        self.order_details = order_details
        self.paid = False


# Menu items with their prices
menu = [
    {"item": "Pizza", "price": "10€"},
    {"item": "Burger", "price": "7€"},
    {"item": "Pasta", "price": "8€"},
    {"item": "Salad", "price": "5€"},
    {"item": "Icecream", "price": "5€"}
]

# Create a diccionary with the items and their prices in integer format
menu_items = {item["item"]: int(item["price"].replace("€", "")) for item in menu}

# Total revenue
revenue = 0

# List to store the orders
orders = []


# Show the menu with tabulate
def show_menu(menu):
    return tabulate(menu, headers="keys", tablefmt="grid")


# Add an order for a table
def add_order(table_id, order_items):

    if table_id == "":
        return "No order added"
    # Check if there is already an order for the given table
    for order in orders:
        if order.table_id == table_id:
            return f"There is already an order for table {table_id}"

    # Count quantities of each item in the order
    order_details = {}
    for item in order_items:
        if item in order_details:
            order_details[item] += 1
        else:
            order_details[item] = 1
    # If there are items in the order, create an order and add it to the order list
    if order_details:
        new_order = Order(table_id, order_details)
        orders.append(new_order)
        return f"Order for table {table_id} has been added"
    else:
        return "No items were added to the order. The order has not been created"


# Delete an order from a table
def delete_order(table_id):
    if table_id == "":
        return "No order deleted"

    # Find and delete the given table
    for order in orders:
        if order.table_id == table_id:
            orders.remove(order)
            return f"Order for table {table_id} has been deleted"

    else:
        return f"No order found for table {table_id}"


# Show all orders with their table id, order details and payment status listed
def show_orders():
    if not orders:
        return "There are no orders"

    orders_list = []
    for order in orders:
        order_info = f"Table id: {order.table_id}\n"
        for item, quantity in order.order_details.items():
            order_info += f"{item}: {quantity}\n"
        order_info += f"Paid: {'Yes' if order.paid else 'No'}\n"
        order_info += "-" * 20
        orders_list.append(order_info)
    return "*** ORDERS ***\n" + "-" * 20 + "\n" + "\n".join(orders_list)


# Mark an order as paid and update revenue
def pay_order(table_id, confirmation="n"):
    global revenue
    if table_id == "":
        return "No order was paid"

    for order in orders:
        if order.table_id == table_id:
            if order.paid:
                return f"The order for table {table_id} has already been paid"
            else:
                order_total = 0
                for item, quantity in order.order_details.items():
                    order_total += menu_items[item] * quantity
                print(f"Total to pay for the table {table_id}: {order_total}€")
                if confirmation == "y":
                    order.paid = True
                    revenue += order_total
                    return f"The order for table {table_id} has been marked as paid. Total: {order_total}€"

                else:
                    return "Payment canceled"
    else:
        return f"No orders found for table {table_id}"


# Print the options menu and ask the user to choose an option
def main():
    while True:
        print("\nChoose an option:")
        print("1. View orders")
        print("2. Add order")
        print("3. Delete order")
        print("4. Pay order")
        print("5. View total revenue")
        print("6. Exit")

        choice = input("Option: ").strip()
        print("")

        if choice == "1":
            print(show_orders())
            input("Press any key to continue...")

        elif choice == "2":
            print(show_menu(menu))
            table_id = input("Enter table id: ").strip()
            order_items = []
            if table_id:
                while True:
                    item = input(
                        "What would you like to eat? (leave blank to stop): ").strip().capitalize()
                    if not item:
                        break

                    if item not in menu_items:
                        print(f"{item} is not on the menu")
                        continue
                    order_items.append(item)

            print(add_order(table_id, order_items))
            input("Press any key to continue...")

        elif choice == "3":
            if not orders:
                print("There are no orders")
                input("Press any key to continue...")
                continue

            print(show_orders())
            table_id = input("Enter the table id of the order to delete: ").strip()
            print(delete_order(table_id))
            input("Press any key to continue...")

        elif choice == "4":
            if not orders:
                print("There are no orders")
                input("Press any key to continue...")
                continue

            print(show_orders())
            table_id = input(
                "Enter the table id of the order you want to mark as paid: ").strip()
            confirmation = input("Confirm payment (y/n): ").strip().lower()
            print(pay_order(table_id, confirmation))
            input("Press any key to continue...")

        elif choice == "5":

            print(f"TOTAL REVENUE: {revenue}€")
            input("Press any key to continue...")

        elif choice == "6":
            break
        else:
            print("Invalid input. Please choose a valid option")


if __name__ == "__main__":
    main()
