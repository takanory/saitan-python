def build_profile(first, last, **user_info):
    """ユーザーの全情報を格納した辞書を作成する"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('たかのり', '鈴木',
                             location='東京',
                             organization='PyCon JP Association',
                             company='BeProud')

print(user_profile)
