import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """employeeモジュールをテストする"""

    def setUp(self):
        """テスト用の従業員を作成する"""
        self.takanory = Employee('takanori', 'suzuki', 6_500_000)

    def test_give_default_raise(self):
        """デフォルト金額での昇給が正しく動作することを確認する"""
        self.takanory.give_raise()
        self.assertEqual(self.takanory.salary, 7_000_000)

    def test_give_custom_raise(self):
        """指定した金額での昇給が正しく動作することを確認する"""
        self.takanory.give_raise(1_000_000)
        self.assertEqual(self.takanory.salary, 7_500_000)


if __name__ == '__main__':
    unittest.main()
