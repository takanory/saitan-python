current_users = ['takanory', 'zenich', 'admin', 'shimizukawa', 'ken5']
new_users = ['soogie', 'Zenich', 'TAKANORY', 'NaoY', 'Kashew_nuts']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"すいません{new_user}、その名前はすでに使用されています。")
    else:
        print(f"よかった、{new_user}という名前は利用可能です。")
