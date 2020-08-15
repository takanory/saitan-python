import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """city_functions.pyをテストする"""

    def test_city_country(self):
        """シンプルな都市名と国名の組が動作するか確認する"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
