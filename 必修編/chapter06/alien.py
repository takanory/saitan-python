alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"最初のX座標: {alien_0['x_position']}")

# エイリアンは右に移動します。
# 現在のスピードによってエイリアンの移動距離を決定します。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 素早いエイリアン
    x_increment = 3

# 新しい位置は元の位置に移動距離を加算します。
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"新しいX座標: {alien_0['x_position']}")
