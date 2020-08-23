import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("好きな数字は何ですか？ ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("ありがとうございます！ その数字を覚えておきます。")
else:
    print(f"あなたが好きな数字を知っています！それは{number}です。")
