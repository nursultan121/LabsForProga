# Предметная область службы доставки
from classes import *
import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

class InvalidIDException(Exception):
    pass

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении в JSON-файл: {e}")

def save_to_xml(data, filename):
    try:
        root = ET.Element('data')
        for item in data:
            item_element = ET.SubElement(root, item['type'])
            for key, value in item['attributes'].items():
                attribute_element = ET.SubElement(item_element, key)
                attribute_element.text = str(value)
        xml_string = ET.tostring(root, encoding='utf-8')
        pretty_xml = parseString(xml_string).toprettyxml(indent="  ")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
    except IOError as e:
        print(f"Ошибка при сохранении в XML-файл: {e}")

def validate_id(identifier):
    if identifier == "-1":
        raise InvalidIDException("ID не может быть равен -1.")

def create_customer():
    try:
        name = input("Введите имя клиента: ")
        phone = input("Введите телефон клиента: ")
        address = input("Введите адрес клиента: ")
        return Customer(name, phone, address)
    except Exception as e:
        print(f"Ошибка при создании клиента: {e}")

def create_employee():
    try:
        name = input("Введите имя сотрудника: ")
        phone = input("Введите телефон сотрудника: ")
        employee_id = input("Введите ID сотрудника: ")
        validate_id(employee_id)
        return Employee(name, phone, employee_id)
    except InvalidIDException as e:
        print(f"Неверный ID: {e}")
    except Exception as e:
        print(f"Ошибка при создании сотрудника: {e}")

def create_driver():
    try:
        name = input("Введите имя водителя: ")
        phone = input("Введите телефон водителя: ")
        employee_id = input("Введите ID сотрудника: ")
        validate_id(employee_id)
        license_number = input("Введите номер лицензии водителя: ")
        vehicle_type = input("Введите тип транспортного средства: ")
        registration_number = input("Введите регистрационный номер ТС: ")
        max_load = float(input("Введите максимальную грузоподъемность ТС: "))
        vehicle = Vehicle(vehicle_type, registration_number, max_load)
        return DeliveryDriver(name, phone, employee_id, license_number, vehicle)
    except InvalidIDException as e:
        print(f"Неверный ID: {e}")
    except ValueError as e:
        print(f"Ошибка ввода числового значения: {e}")
    except Exception as e:
        print(f"Ошибка при создании водителя: {e}")

def create_order():
    try:
        order_id = input("Введите ID заказа: ")
        validate_id(order_id)
        customer_name = input("Введите имя клиента для заказа: ")
        customer_phone = input("Введите телефон клиента: ")
        customer_address = input("Введите адрес клиента: ")
        customer = Customer(customer_name, customer_phone, customer_address)
        num_items = int(input("Введите количество товаров в заказе: "))
        items = []
        for _ in range(num_items):
            item_name = input("Введите название товара: ")
            item_weight = float(input("Введите вес товара: "))
            item_price = float(input("Введите цену товара: "))
            items.append(Item(item_name, item_weight, item_price))
        return Order(order_id, customer, items)
    except InvalidIDException as e:
        print(f"Неверный ID: {e}")
    except ValueError as e:
        print(f"Ошибка ввода числового значения: {e}")
    except Exception as e:
        print(f"Ошибка при создании заказа: {e}")

def main():
    data = []
    while True:
        print("\nМеню:")
        print("1. Добавить клиента")
        print("2. Добавить сотрудника")
        print("3. Добавить водителя доставки")
        print("4. Добавить заказ")
        print("5. Сохранить данные в JSON")
        print("6. Сохранить данные в XML")
        print("0. Выход")
        try:
            choice = input("Выберите действие: ")
            if choice == "1":
                customer = create_customer()
                if customer:
                    data.append({"type": "Customer", "attributes": vars(customer)})
            elif choice == "2":
                employee = create_employee()
                if employee:
                    data.append({"type": "Employee", "attributes": vars(employee)})
            elif choice == "3":
                driver = create_driver()
                if driver:
                    driver_data = vars(driver)
                    driver_data['vehicle'] = vars(driver.vehicle)
                    data.append({"type": "DeliveryDriver", "attributes": driver_data})
            elif choice == "4":
                order = create_order()
                if order:
                    order_data = vars(order)
                    order_data['customer'] = vars(order.customer)
                    order_data['items'] = [vars(item) for item in order.items]
                    data.append({"type": "Order", "attributes": order_data})
            elif choice == "5":
                save_to_json(data, 'data.json')
                print("Данные сохранены в JSON-файл.")
            elif choice == "6":
                save_to_xml(data, 'data.xml')
                print("Данные сохранены в XML-файл.")
            elif choice == "0":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()