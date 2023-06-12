import unittest
from Country_City import get_formatted_country_city

class Test_city_country(unittest.TestCase):

    def test_country(self):
        formatted_city = get_formatted_country_city("Santiago","Chile")
        self.assertEqual(formatted_city,"Santiago, Chile")

if __name__ == '__main__':
    unittest.main()