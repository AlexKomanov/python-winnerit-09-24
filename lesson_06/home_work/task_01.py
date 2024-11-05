class Person:
    def __init__(self, name):
        self.name = name  # Regular property in parent class

    def get_name(self):
        return self.name


class Employee(Person):
    def __init__(self, name, salary, role):
        super().__init__(name)
        self.__salary = salary  # Private property
        self.__role = role  # Private property

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        if not value:
            raise ValueError("Role cannot be empty")
        self.__role = value


# Usage example:

# Creating an Employee object
employee = Employee("John Smith", 5000, "Software Developer")

# Using property from parent class
print(f"Employee name: {employee.get_name()}")

# Using properties
print(f"Salary: ${employee.salary}")
print(f"Role: {employee.role}")

# Changing values using setters
employee.salary = 5500
employee.role = "Senior Developer"

print(f"\nAfter promotion:")
print(f"New salary: ${employee.salary}")
print(f"New role: {employee.role}")

# Example of validation
try:
    employee.salary = -1000  # This will raise an error
except ValueError as e:
    print(f"\nValidation error: {e}")


