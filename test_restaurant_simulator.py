import pytest
from restaurant_simulator import show_menu, menu, add_order, delete_order, show_orders, pay_order, orders, revenue


@pytest.fixture(autouse=True)
def reset_orders():
    orders.clear()
    global revenue
    revenue = 0


def test_show_menu():
    assert show_menu(menu) == (
        "+----------+---------+\n"
        "| item     | price   |\n"
        "+==========+=========+\n"
        "| Pizza    | 10€     |\n"
        "+----------+---------+\n"
        "| Burger   | 7€      |\n"
        "+----------+---------+\n"
        "| Pasta    | 8€      |\n"
        "+----------+---------+\n"
        "| Salad    | 5€      |\n"
        "+----------+---------+\n"
        "| Icecream | 5€      |\n"
        "+----------+---------+"
    )


def test_add_order():
    assert add_order("1", ["Pizza", "Salad", "Pizza"]) == "Order for table 1 has been added"
    assert add_order("1", ["Pizza", "Salad", "Pizza"]) == "There is already an order for table 1"
    assert add_order("2", ["Pizza", "Salad", "Pizza"]) == "Order for table 2 has been added"
    assert add_order("", ["Pizza"]) == "No order added"
    assert add_order("6", []) == "No items were added to the order. The order has not been created"


def test_delete_order():
    add_order("1", ["Pizza"])
    assert delete_order("1") == "Order for table 1 has been deleted"
    assert delete_order("1") == "No order found for table 1"
    assert delete_order("") == "No order deleted"


def test_show_orders():

    assert show_orders() == "There are no orders"

    add_order("hello world", ["Icecream"])
    assert show_orders() == (
        "*** ORDERS ***\n"
        "--------------------\n"
        "Table id: hello world\n"
        "Icecream: 1\n"
        "Paid: No\n"
        "--------------------"
    )

    add_order("123", ["Salad"])
    assert show_orders() == (
        "*** ORDERS ***\n"
        "--------------------\n"
        "Table id: hello world\n"
        "Icecream: 1\n"
        "Paid: No\n"
        "--------------------\n"
        "Table id: 123\n"
        "Salad: 1\n"
        "Paid: No\n"
        "--------------------"
    )


def test_pay_order():

    add_order("hello world", ["Icecream"])
    assert pay_order(
        "hello world", confirmation="y") == "The order for table hello world has been marked as paid. Total: 5€"

    add_order("1", ["Icecream", "Salad", "Salad"])
    assert pay_order(
        "1", confirmation="y") == "The order for table 1 has been marked as paid. Total: 15€"
    assert pay_order("1") == "The order for table 1 has already been paid"

    add_order("2", ["Salad", "Salad"])
    assert pay_order("2", confirmation="n") == "Payment canceled"

    assert pay_order("3") == "No orders found for table 3"
