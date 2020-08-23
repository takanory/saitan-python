filename = 'guest_book.txt'

print("終了するには '終了' と入力してください。")
while True:
    name = input("\nお名前は？ ")
    if name == '終了':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"こんにちは{name}さん。あなたはゲストブックに追加されました。")
