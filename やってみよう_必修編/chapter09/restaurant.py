"""レストランを表すクラス"""


class Restaurant():
    """レストランを表すクラス"""

    def __init__(self, name, cuisine_type):
        """レストランを初期化する"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """レストランについての情報を出力する"""
        msg = f"{self.name}は素晴らしい{self.cuisine_type}を提供します。"
        print(f"\n{msg}")

    def open_restaurant(self):
        """レストランが開店したことを知らせるメッセージを出力する"""
        msg = f"{self.name}が開店しました。ぜひご来店ください！"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """料理を提供したお客さんの数を設定する"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """料理を提供したお客さんの数を増やす"""
        self.number_served += additional_served
