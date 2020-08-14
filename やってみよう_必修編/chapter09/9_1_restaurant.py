class Restaurant():
    """レストランを表すクラス"""

    def __init__(self, name, cuisine_type):
        """レストランを初期化する"""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """レストランについての情報を出力する"""
        msg = f"{self.name}は素晴らしい{self.cuisine_type}を提供します。"
        print(f"\n{msg}")

    def open_restaurant(self):
        """レストランが開店したことを知らせるメッセージを出力する"""
        msg = f"{self.name}が開店しました。ぜひご来店ください！"
        print(f"\n{msg}")


restaurant = Restaurant('malaychan', '東南アジア料理')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
