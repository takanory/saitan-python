# エイリアンを格納する空のリストを作成する
aliens = []

# 30匹のエイリアンを生成する
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 最初の5匹のエイリアンの情報を出力する
for alien in aliens[:5]:
    print(alien)
print("...")

# 生成されたエイリアンの数を出力する
print(f"全エイリアンの数: {len(aliens)}")
