import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_creation():
    c = Customer("Alice")
    assert c.name == "Alice"
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long


def test_customer_orders_and_coffees():
    c = Customer("Bob")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")

    order1 = c.create_order(latte, 5.0)
    order2 = c.create_order(espresso, 3.0)

    assert order1 in c.orders()
    assert order2 in c.orders()
    assert latte in c.coffees()
    assert espresso in c.coffees()


def test_most_aficionado():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    mocha = Coffee("Mocha")

    c1.create_order(mocha, 4.0)
    c1.create_order(mocha, 2.0)
    c2.create_order(mocha, 7.0)

    assert Customer.most_aficionado(mocha) == c2

    new_coffee = Coffee("Americano")
    assert Customer.most_aficionado(new_coffee) is None
