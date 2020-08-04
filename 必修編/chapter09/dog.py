class Dog:
    """イヌをモデル化したシンプルな実装例"""

    def __init__(self, name, age):
        """名前と年齢の属性を初期化する"""
        self.name = name
        self.age = age

    def sit(self):
        """イヌに「おすわり」の命令を実行する"""
        print(f"{self.name}はおすわりしている。")

    def roll_over(self):
        """イヌに「ごろーん」の命令を実行する"""
        print(f"{self.name}がごろーんした！")

my_dog = Dog('ウィリー', 6)
your_dog = Dog('ルーシー', 3)

print(f"私のイヌの名前は{my_dog.name}です。")
print(f"私のイヌは{my_dog.age}歳です。")
my_dog.sit()

print(f"\nあなたのイヌの名前は{your_dog.name}です。")
print(f"あなたのイヌは{your_dog.age}歳です。")
your_dog.sit()
