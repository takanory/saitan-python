# ペットの情報を格納する空のリストを作成する
pets = []

# ペットの情報を作成してリストに追加する
pet = {
    'animal type': 'フェレット',
    'name': 'せぶん',
    'owner': 'takanory',
    'eats': 'ferret food',
    }
pets.append(pet)

pet = {
    'animal type': 'うさぎ',
    'name': 'ちゃまる',
    'owner': 'selina',
    'eats': 'grass',
    }
pets.append(pet)

# 各ペットの情報を出力する
for pet in pets:
    print(f"\n{pet['name']}についての情報です。")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
