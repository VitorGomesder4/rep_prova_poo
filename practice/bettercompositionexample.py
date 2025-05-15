class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Employee:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address  # Composition: an Employee HAS an Address

emp_address = Address("123 Main St", "Springfield", "IL", "62704")
emp = Employee("Alice", emp_address)

print(f"{emp.name} lives in {emp.address.city}, {emp.address.state}")