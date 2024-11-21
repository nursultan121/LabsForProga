# Предметная область службы доставки
class Person:
    """Базовый класс для людей."""
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Customer(Person):
    """Класс для клиентов службы доставки (наследует Person)."""
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address
