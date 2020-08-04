# 確認が必要なユーザーから始める
# 確認済みのユーザーを保持するための空のリストを用意する
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 未確認ユーザーがいなくなるまでユーザーの確認を進める
# 確認済みのユーザーは確認済みリストに移動する
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"確認中のユーザー: {current_user.title()}")
    confirmed_users.append(current_user)

# 確認済みのユーザーをすべて表示する
print("\n以下のユーザーは確認済みです。")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
