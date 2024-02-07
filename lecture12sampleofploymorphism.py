class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def getName(self):
        return self.name

    def calcPay(self):
        return 0

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, annual_salary):
        super().__init__(emp_id, name)
        self.annual_salary = annual_salary

    def calcPay(self):
        # Assuming bi-weekly pay
        return self.annual_salary / 26

class CasualEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calcPay(self):
        return self.hourly_rate * self.hours_worked

# Polymorphic function
def calculate_pay(emp):
    print("Name: ", emp.getName())
    print("Pay: $", emp.calcPay())

def main():
    print("Wage Calculator")
    print("-------------------------")
    
    # Create instances of CasualEmployee and SalariedEmployee
    e1 = CasualEmployee('emp100', 'Umesh', 20, 40)
    e2 = SalariedEmployee('emp200', 'David', 124800)

    # Calculate pay using the polymorphic function
    calculate_pay(e1)
    print()
    calculate_pay(e2)

# Run the main function
main()