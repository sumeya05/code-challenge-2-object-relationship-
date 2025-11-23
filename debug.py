from customer import Customer
from coffee import Coffee

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Place orders
alice.create_order(latte, 5.0)
alice.create_order(espresso, 3.5)
bob.create_order(latte, 6.0)

# Test coffee methods
print(latte.num_orders())
print(latte.average_price())
print(espresso.customers())

# Test customer methods
print(alice.coffees())
print(Customer.most_aficionado(latte).name)
