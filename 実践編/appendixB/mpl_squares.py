import matplotlib.pyplot as plt
from matplotlib import rcParams

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
rcParams['font.family'] = 'IPAexGothic'
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# グラフのタイトルと軸のラベルを設定する
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("値", fontsize=14)
ax.set_ylabel("2乗した値", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis='both', labelsize=14)

plt.show()
