import unittest

from city_functions2 import city_country


class CitiesTestCase(unittest.TestCase):
    """city_functions2.pyをテストする"""

    def test_city_country(self):
        """シンプルな都市名と国名の組が動作するか確認する"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    def test_city_country_population(self):
        """人口を含んでも動作するかを確認する"""
        santiago_chile = city_country('santiago', 'chile',
                                      population=5_000_000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - 人口 5000000')


if __name__ == '__main__':
    unittest.main()
