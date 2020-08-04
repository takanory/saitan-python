def get_formatted_name(first_name, last_name):
    """フォーマットされたフルネームを返す"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# これは無限ループです！
while True:
    print("\nあなたの名前を教えてください。")
    print("（'q' を入力すると終了します）")

    l_name = input("姓を入力してください: ")
    if l_name == 'q':
        break

    f_name = input("名を入力してください: ")
    if f_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nこんにちは{formatted_name}！")
