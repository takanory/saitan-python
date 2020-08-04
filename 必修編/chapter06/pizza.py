# ピザの注文に関する情報を格納する
pizza = {
    'crust': 'レギュラー',
    'toppings': ['マッシュルーム', 'エクストラチーズ'],
    }

# 注文の要約
print(f"あなたが注文したのは{pizza['crust']}生地のピザで、"
    "トッピングは以下のとおりです。")

for topping in pizza['toppings']:
    print("\t" + topping)
