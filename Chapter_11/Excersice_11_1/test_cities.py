import unittest

from city_functions import Country_City_Name

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_city = Country_City_Name('chile','santiago')
        self.assertEquals(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
        