import json

def get_stored_username():
    """保存されたユーザー名があれば取得する。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """新たなユーザー名の入力を促す。"""
    username = input("あなたのお名前は？ ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """ユーザー名であいさつする。"""
    username = get_stored_username()
    if username:
        correct = input(f"あなたは{username}さんですか？ (y/n) ")
        if correct == 'y':
            print(f"おかえりなさい、{username}さん！")
        else:
            username = get_new_username()
            print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")
    else:
        username = get_new_username()
        print(f"戻ってきたときにも名前を覚えていますよ、{username}さん！")

greet_user()
