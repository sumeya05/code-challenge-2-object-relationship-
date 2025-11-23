import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_order_creation_and_properties():
    c = Customer("Alice")
    latte = Coffee("Latte")

    order = Order(c, latte, 5.0)
    assert order.customer == c
    assert order.coffee == latte
    assert order.price == 5.0

    with pytest.raises(ValueError):
        Order(c, latte, 0.5)  # Price too low

    with pytest.raises(ValueError):
        Order(c, latte, 11.0)  # Price too high
