filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\n読込中のファイル: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  すみません、ファイルが見つかりませんでした。")
