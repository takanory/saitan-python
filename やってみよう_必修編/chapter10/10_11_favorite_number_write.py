import json

number = input("好きな数字は何ですか？ ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("ありがとうございます！ その数字を覚えておきます。")
