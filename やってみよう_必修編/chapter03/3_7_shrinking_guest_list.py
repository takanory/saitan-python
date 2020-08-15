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

# 大きなテーブルを見つけたので、追加のゲストを招待する
print("\n大きなテーブルを見つけた！")
guests.insert(0, 'iqbal abdullah')
guests.insert(2, 'younggun kim')
guests.append('jung yu cheng')

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[3].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[4].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[5].title()
print(f"{name}さん、ぜひ夕食に来てください。")

# 大きいテーブルが夕食の時間に間に合いません！
print("\nごめんなさい、夕食に2名しか招待できません。")

name = guests.pop()
print(f"ごめんなさい、{name.title()}さんの席がありません。")

name = guests.pop()
print(f"ごめんなさい、{name.title()}さんの席がありません。")

name = guests.pop()
print(f"ごめんなさい、{name.title()}さんの席がありません。")

name = guests.pop()
print(f"ごめんなさい、{name.title()}さんの席がありません。")

# 残った2名に対して招待メッセージを出力する
name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

# リストを空にする
del guests[0]
del guests[0]

# リストが空であることを確認する
print(guests)
