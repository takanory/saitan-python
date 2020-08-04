number = input("何か数を入力してください。奇数か偶数かを判定します: ")
number = int(number)

if number % 2 == 0:
    print(f"\n数{number}は偶数です。")
else:
    print(f"\n数{number}は奇数です。")
