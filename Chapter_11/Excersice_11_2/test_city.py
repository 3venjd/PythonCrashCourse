import unittest

from city_functions import get_city_name

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_city = get_city_name('chile','santiago','5000000')
        self.assertEquals(formatted_city, 'Santiago, Chile - 5000000')

if __name__ == '__main__':
    unittest.main()
        