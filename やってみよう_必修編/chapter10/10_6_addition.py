try:
    x = input("何か数字を入力してください: ")
    x = int(x)

    y = input("別の数字を入力してください: ")
    y = int(y)
except ValueError:
    print("すみません、数字でお願いします。")
else:
    sum = x + y
    print(f"{x}と{y}の合計は{sum}です。")
