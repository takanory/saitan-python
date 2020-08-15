favorite_numbers = {
    'たかのり': [42, 17],
    'ぜんいち': [42, 39, 56],
    'かしゅー': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}の好きな数字は以下です。")
    for number in numbers:
        print(f"  {number}")
