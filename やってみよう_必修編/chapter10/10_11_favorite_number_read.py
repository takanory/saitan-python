import json

with open('favorite_number.json') as f:
    number = json.load(f)

print(f"あなたが好きな数字を知っています！それは{number}です。")
