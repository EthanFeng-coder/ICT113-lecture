class Employee:
    def __init__(self, name, employee_id, employee_type, hourly_rate):
        self.name = name
        self.employee_id = employee_id
        self.employee_type = employee_type  # such as 'full-time', 'part-time', 'contractor'
        self.hourly_rate = hourly_rate

    def calculate_wage(self, hours_worked):
        # The calculation might differ based on the employee type
        if self.employee_type == 'full-time':
            return self.calculate_full_time_wage(hours_worked)
        elif self.employee_type == 'part-time':
            return self.calculate_part_time_wage(hours_worked)
        elif self.employee_type == 'contractor':
            return self.calculate_contractor_wage(hours_worked)
        else:
            raise ValueError("Invalid employee type")

    def calculate_full_time_wage(self, hours_worked):
        # Implement full-time wage calculation logic
        pass

    def calculate_part_time_wage(self, hours_worked):
        # Implement part-time wage calculation logic
        pass

    def calculate_contractor_wage(self, hours_worked):
        # Implement contractor wage calculation logic
        pass

    # Additional methods can be added here a