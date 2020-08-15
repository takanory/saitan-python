def make_sandwich(*items):
    """指定された材料でサンドイッチを作る"""
    print("\nこれからサンドイッチを作ります。")
    for item in items:
        print(f"  ...{item}をサンドイッチに追加しました。")
    print("サンドイッチができました！")


make_sandwich('ベーコン', 'レタス', 'トマト')
make_sandwich('ツナ', 'マヨネーズ')
make_sandwich('ハム', 'チーズ', 'レタス', 'トマト', '玉子')
