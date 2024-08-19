# Restaurant Simulator


#### Video Demo: [Click here](https://youtu.be/8C6IFYBsvjU)


## Description:


Welcome to the **Restaurant Simulator**, a Python-based project designed to simulate management in a restaurant. This project was developed as part of the **CS50P course from Harvard**, focusing on Python programming. It provides a virtual environment where users can perform typical restaurant management tasks, such as adding orders, deleting them, marking them as paid, and viewing total revenue.


## Getting Started

To get started with the **Restaurant Simulator**, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/giannibytes/cs50p-restaurant-simulator.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd cs50p-restaurant-simulator
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Program**:
    ```bash
    python restaurant_simulator.py
    ```

5. **Follow On-Screen Instructions**:
    - The program will prompt you with options and instructions to manage the restaurant simulator.



## Features


- **View Orders**: Show a detailed list of current orders containing their table ID, ordered items, and their payment status.
- **Add Order**: Create new orders for specific tables by selecting items from the predefined menu.
- **Delete Order**: Remove existing orders.
- **Pay Order**: Mark orders as paid to update the total revenue.
- **View Total Revenue**: Show the total revenue accumulated.


## How to Use


1. **View Orders**:
    - Choose option `1` from the menu to view all current orders.
    - Each order contains the table ID, the items ordered, and the payment status.

2. **Add Order**:
    - Choose option `2` to add a new order.
    - Enter the ID of the table where the order will be added.
    - Follow the instructions to add menu items until finished.

3. **Delete Order**:
    - Choose option `3` to delete an existing order.
    - Enter the table ID of the order you want to delete.

4. **Pay Order**:
    - Choose option `4` to mark an existing order as paid.
    - Enter the table ID of the order you want to mark as paid.
    - Confirm payment when prompted (`y` for yes, `n` for no).

5. **View Total Revenue**:
    - Choose option `5` to view total revenue earned until now.

6. **Exit**:
    - Choose option `6` to exit the program.


## Usage Notes


- Be sure to follow the instructions and provide valid information when necessary.
- The program will guide you through every step with instructions and requests.


## Technical Details


The program uses the `tabulate` library for better menu display and employs data structures such as lists and dictionaries to manage orders and menus efficiently. Each function of the program is designed to be intuitive and easy to use.


## Contributions


- If you wish to contribute to this project, feel free to clone the repository and submit pull requests with improvements or fixes.
- Open new issues to discuss features, report bugs, or suggest improvements.
