from name_function import get_formatted_name

print("'q' を入力すると終了します。")
while True:
    first = input("\n名を入力してください: ")
    if first == 'q':
        break
    last = input("姓を入力してください: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tフォーマットされた名前: {formatted_name}.")
