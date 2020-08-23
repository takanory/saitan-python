print("終了するにはいつでも 'q' を入力してください。\n")

while True:
    try:
        x = input("\n何か数字を入力してください: ")
        if x == 'q':
            break

        x = int(x)

        y = input("別の数字を入力してください: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("すみません、数字でお願いします。")

    else:
        sum = x + y
        print(f"{x}と{y}の合計は{sum}です。")
