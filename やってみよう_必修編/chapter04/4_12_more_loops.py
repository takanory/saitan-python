my_foods = ['ピザ', 'だんご', 'ケーキ']
friend_foods = my_foods[:]

my_foods.append('チョコレート')
friend_foods.append('アイスクリーム')

print("私の好きな食べ物")
for food in my_foods:
    print(f"- {food}")

print("\n友達が好きな食べ物")
for food in friend_foods:
    print(f"- {food}")
