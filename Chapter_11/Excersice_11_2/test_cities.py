import unittest
from Country_City import get_country_city

class test_city_country(unittest.TestCase):
    
    def test_country(self):
        formatted_city = get_country_city('chile','Santiago')
        self.assertEqual(formatted_city,"Santiago, Chile")

    def test_country_population(self):
        formatted_city = get_country_city('chile','Santiago',2000)
        self.assertEqual(formatted_city,"Santiago, Chile - Population 2000")

if __name__ == '__main__':
    unittest.main()