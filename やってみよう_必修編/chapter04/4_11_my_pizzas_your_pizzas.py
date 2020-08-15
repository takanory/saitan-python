favorite_pizzas = ['マルゲリータ', 'クアトロ・フォルマッジ', 'マリナーラ']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('ビスマルク')
friend_pizzas.append('ペスカトーレ')

print("私が好きなピザ")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\n友達が好きなピザ")
for pizza in friend_pizzas:
    print(f"- {pizza}")
