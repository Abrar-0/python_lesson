class Employee:
    def __init__(self,name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        
    def get_name(self)-> str:
        return self.name
    
    def get_employee_id(self)-> str:
        return self.employee_id
    
    def get_position(self)-> str:
        return self.position
    
    def get_salary(self)-> str:
        return self.salary
    
    def set_salary(self, salary):
        self.salary = salary
        
class Manager(Employee):
    
    def __init__(self,name, employee_id, salary, department): 
        super().__init__(name, employee_id, "Manager", salary)
        self.department = department
    
    def get_department(self):
        return self.department

class EmployeeManagement:
    
    def __init__(self) -> None:
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for em in self.employees:
            if(em.get_employee_id() == employee_id):
                self.employees.remove(em)
                return True
        return False

    def list_employees(self):
        for em in self.employees:
            details = f'Employee ID: {em.get_employee_id()} Name: {em.get_name()} Salary: {em.get_salary()} Position: {em.get_position()}'
            if isinstance (em, Manager):
                details += f' Department: {em.get_department()}'
            print(details)
        if not self.employees:
            print("No employees found")

ems = EmployeeManagement()

# Adding employees
emp1 = Employee("John Doe", 1001, "Software Engineer", 60000)
emp2 = Manager("Jane Smith", 1002, 80000, "Engineering")
emp3 = Employee("John Daaae", 1003, "UX Engineer", 40000)

ems.add_employee(emp1)
ems.add_employee(emp2)

ems.list_employees()

# ems.remove_employee(1001)
ems.add_employee(emp3)

ems.list_employees()
