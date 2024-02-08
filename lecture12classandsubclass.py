class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    # Common method for display
    def display_information(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_monthly_pay(self):
        return self.annual_salary / 12

class CasualEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def record_hours(self, hours):
        self.hours_worked += hours
