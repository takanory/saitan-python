def make_album(artist, title, tracks=0):
    """アルバムに関する情報を含んだ辞書を作成する"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# 終了方法を通知する
print("'quit' と入力すると終了します。")

while True:
    title = input("\nアルバムの名前を教えてください： ")
    if title == 'quit':
        break

    artist = input("アーティストは誰ですか？ ")
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\n入力ありがとうございます！")
