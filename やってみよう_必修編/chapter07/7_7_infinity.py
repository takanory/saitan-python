prompt = "何歳ですか？ "

active = True
while active:
    age = input(prompt)
    age = int(age)

    if age < 3:
        print("  チケット料金は無料です。")
    elif age < 13:
        print("  チケット料金は1000円です。")
    else:
        print("  チケット料金は1500円です。")
