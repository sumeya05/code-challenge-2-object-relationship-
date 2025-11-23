from order import Order


class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name  # Will call the setter
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError(
                "Customer name must be a string between 1 and 15 characters."
            )
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_totals = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_totals[order.customer] = (
                    customer_totals.get(order.customer, 0) + order.price
                )
        if not customer_totals:
            return None
        return max(customer_totals, key=customer_totals.get)
