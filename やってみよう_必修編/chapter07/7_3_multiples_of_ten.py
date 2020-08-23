number = input("何か数を入力してください: ")
number = int(number)

if number % 10 == 0:
    print(f"{number}は10の倍数です。")
else:
    print(f"{number}は10の倍数ではありません。")
