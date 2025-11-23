import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_coffee_creation():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    with pytest.raises(ValueError):
        Coffee("ab")  # Too short


def test_coffee_orders_and_customers():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    latte = Coffee("Latte")

    o1 = c1.create_order(latte, 5.0)
    o2 = c2.create_order(latte, 6.0)

    assert o1 in latte.orders()
    assert o2 in latte.orders()
    assert c1 in latte.customers()
    assert c2 in latte.customers()


def test_num_orders_and_average_price():
    c = Customer("Alice")
    cappuccino = Coffee("Cappuccino")

    c.create_order(cappuccino, 4.0)
    c.create_order(cappuccino, 6.0)

    assert cappuccino.num_orders() == 2
    assert cappuccino.average_price() == 5.0
