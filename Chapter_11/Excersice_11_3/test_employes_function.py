import unittest
from employes import employe

class TestEmployeSalaryRise(unittest.TestCase):

    def setUp(self):
        """Create a employee and test if the survey works"""
        firstName = "Rafael"
        lastName = "Jimenez"
        salary = 6000
        self.employe = employe(firstName,lastName,salary)

    #when we test integer, always cast into string
    def test_give_default_rise(self):
        self.employe.give_raise()
        self.assertIn("11000",str(self.employe.dataEmploye["ActualSalary"]))

    def test_give_custom_rise(self):
        self.employe.give_raise(2000)
        self.assertIn("8000",str(self.employe.dataEmploye["ActualSalary"]))
""
if __name__ == '__main__':
    unittest.main()