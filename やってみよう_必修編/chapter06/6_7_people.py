# 空のリストを作成する
people = []

# 人の辞書を作成してリストに追加する
person = {
    'first_name': 'たかのり',
    'last_name': '鈴木',
    'age': 49,
    'city': '東京',
    }
people.append(person)

person = {
    'first_name': 'せぶん',
    'last_name': '鈴木',
    'age': 2,
    'city': '東京',
    }
people.append(person)

person = {
    'first_name': 'にあ',
    'last_name': '鈴木',
    'age': 4,
    'city': '東京',
    }
people.append(person)

# 辞書の全情報を出力する
for person in people:
    name = f"{person['last_name']}{person['first_name']}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}は{city}に住んでおり、{age}才です。")
