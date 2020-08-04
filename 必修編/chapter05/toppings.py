available_toppings = ['マッシュルーム', 'オリーブ', 'ピーマン',
                      'ペパロニ', 'パイナップル', 'エクストラチーズ']

requested_toppings = ['マッシュルーム', 'フライドポテト', 'エクストラチーズ']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"ピザに{requested_topping}を追加します。")
    else:
        print(f"申し訳ありません、{requested_topping}はありません。")

print("\nピザができました！")
