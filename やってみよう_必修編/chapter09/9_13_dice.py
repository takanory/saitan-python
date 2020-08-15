from random import randint


class Die():
    """サイコロを表すクラス"""

    def __init__(self, sides=6):
        """サイコロを初期化する"""
        self.sides = sides

    def roll_die(self):
        """サイコロの出た目（1〜面の数）を返す"""
        return randint(1, self.sides)


# 6面のサイコロを作成し、10回転がした結果を出力する
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("6面サイコロを10回転がした結果")
print(results)

# 10面のサイコロを作成し、10回転がした結果を出力する
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10面サイコロを10回転が結果")
print(results)

# 20面のサイコロを作成し、10回転がした結果を出力する
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n20面サイコロを10回転が結果")
print(results)
