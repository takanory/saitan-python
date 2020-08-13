def make_album(artist, title, tracks=0):
    """アルバムに関する情報を含んだ辞書を作成する"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


album = make_album('steve reich', 'music for 18 musicians')
print(album)

album = make_album('大阪市音楽団', '宇宙の音楽')
print(album)

album = make_album('queen', 'a night at the opera', tracks=12)
print(album)
