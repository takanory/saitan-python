from user import Admin

takanory = Admin('takanori', 'suzuki', 'takanory', 'takanory@example.com',
                 'toshima-ku')
takanory.describe_user()

takanory_privileges = [
    "投稿を追加する",
    "投稿を削除する",
    "ユーザーを利用禁止にする",
    ]
takanory.privileges.privileges = takanory_privileges
takanory.privileges.show_privileges()
