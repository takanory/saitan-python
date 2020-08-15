def make_shirt(size, message):
    """作成するTシャツの情報を出力する"""
    print(f"\n{size}サイズのTシャツを作ります。")
    print(f'プリントするメッセージは「{message}」です。')


make_shirt('M', '大好きPython!')
make_shirt(message="Spam, Ham, Eggs", size='G-L')
