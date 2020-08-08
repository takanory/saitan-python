party_size = input("今晩のディナーには何人参加しますか？ ")
party_size = int(party_size)

if party_size > 8:
    print("すみません、席につくまで少しお待ちください。")
else:
    print("テーブルの準備はできています。")
