import pickle


class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"


def serialize_employee(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)


def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee = pickle.load(file)
    return employee


emp1 = Employee("E001", "Joe Mama", "2023-01-01", 50000)
serialize_employee(emp1, "employee.dat")

deserialized_emp = deserialize_employee("employee.dat")
print(deserialized_emp)
