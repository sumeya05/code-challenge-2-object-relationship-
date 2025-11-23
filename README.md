### ☕ Coffee Shop Domain Model

### Python OOP • Object Relationships Code Challenge

### 📌 Overview

This project is a Python application that models a Coffee Shop using Object-Oriented Programming and object relationships.

### The domain consists of three main entities:

Customer

Coffee

Order

### The relationships modeled are:

A Customer can have many Orders

A Coffee can have many Orders

An Order belongs to one Customer and one Coffee

Customer ↔ Coffee is many-to-many through Order

This project demonstrates object relationships, validation, aggregate methods, and clean Python design following best practices.

### 📁 Project Structure

coffee_shop/
│── customer.py
│── coffee.py
│── order.py
│── debug.py
│── README.md
│
└── tests/ # (Optional Bonus)
├── test_customer.py
├── test_coffee.py
└── test_order.py

### 🛠️ Setup Instructions

1. Create Project Directory
   mkdir coffee_shop
   cd coffee_shop

2. Set Up Virtual Environment
   pipenv install
   pipenv shell

3. (Optional) Install Pytest
   pipenv install pytest

📦 Classes & Responsibilities

### 1. Customer Class

Initializes with:

name → string (1–15 chars)

Methods:

orders() → list of Order instances

coffees() → unique list of Coffee objects

create_order(coffee, price) → creates new Order

most_aficionado(coffee) → class method returning biggest spender on that coffee

### 2. Coffee Class

Initializes with:

name → string (≥ 3 characters)

Methods:

orders() → all orders for that coffee

customers() → unique list of customers

num_orders() → count of orders

average_price() → average price paid

### 3. Order Class

Initializes with:

customer → Customer instance

coffee → Coffee instance

price → float (1.0–10.0)

Validates:

correct types

valid price

Represents the belongs-to relationship

### 🔍 Validations (Exception Handling)

Each class includes strict input validation:

Customer name must be:

string

1–15 characters

Coffee name must be:

string

at least 3 characters

Order price:

float or int

between 1.0 and 10.0

Customer & Coffee in Order must be correct class types

Invalid data raises Exception.

### ▶️ Running Debug Script

Test everything manually:

python debug.py

Example functionality tested:

Creating customers

Creating coffees

Creating orders

Relationship methods

Aggregate methods

Aficionado calculation
