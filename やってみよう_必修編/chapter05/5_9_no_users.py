usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("こんにちはadmin、状況のレポートを見ますか？")
        else:
            print(f"こんにちは{username}、またログインしてくれてありがとう。")
else:
    print("ユーザー募集中です！")
