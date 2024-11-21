# Предметная область службы доставки
class Person:
    """Базовый класс для людей"""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Customer(Person):
    """Класс для клиентов службы доставки"""
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address

class Employee(Person):
    """Базовый класс для сотрудников службы доставки"""
    def __init__(self, name, phone, employee_id):
        super().__init__(name, phone)
        self.employee_id = employee_id

class DeliveryDriver(Employee):
    """Класс для водителей доставки"""
    def __init__(self, name, phone, employee_id, license_number, vehicle):
        super().__init__(name, phone, employee_id)
        self.license_number = license_number
        self.vehicle = vehicle 
        self.current_order = None 

    def assign_order(self, order):
        self.current_order = order

class Manager(Employee):
    """Класс для менеджеров"""
    def __init__(self, name, phone, employee_id, department):
        super().__init__(name, phone, employee_id)
        self.department = department

    def manage_warehouse(self, warehouse):
        print(f"{self.name} управляет складом на {warehouse.location}.")

class Order:
    """Класс для заказов"""
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer  
        self.items = items  
        self.status = "Pending"

    def update_status(self, status):
        self.status = status

class Item:
    """Класс для товаров"""
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

class Vehicle:
    """Класс для транспортных средств"""
    def __init__(self, vehicle_type, registration_number, max_load):
        self.vehicle_type = vehicle_type
        self.registration_number = registration_number
        self.max_load = max_load

class Warehouse:
    """Класс для складов."""
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.inventory = [] 

    def add_item(self, item):
        self.inventory.append(item)

class Payment:
    """Класс для обработки платежей."""
    def __init__(self, amount, payment_method, order):
        self.amount = amount
        self.payment_method = payment_method
        self.order = order  
        self.status = "Pending"

    def process_payment(self):
        self.status = "Completed"
