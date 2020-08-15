guests = ["guido van rossum", "ewa jodlowska", "naomi ceder"]

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"\nすいません、{name}さんが夕食に参加できなくなりました。")

# Ewaさんの代わりにCoryさんを招待します
del guests[1]
guests.insert(1, 'cory althoff')

# 再度、招待メッセージを取得する
name = guests[0].title()
print(f"\n{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")
