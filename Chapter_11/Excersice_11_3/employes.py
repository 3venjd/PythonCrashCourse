class employe:
    """Get the employee information"""

    def __init__(self, FirstName, LastName, AnnualSalary):
        self.dataEmploye = {"firstName": FirstName, "lastName" : LastName, "ActualSalary": AnnualSalary}

    #def strore_employee(self, employeeFirstName, employeLastName, employeActualSalary):


    def give_raise(self,riseSalary = 5000):
        self.dataEmploye["ActualSalary"] = self.dataEmploye["ActualSalary"] + riseSalary