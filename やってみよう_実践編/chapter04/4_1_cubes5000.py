from matplotlib import pyplot as plt

# データを定義する
x_values = list(range(1, 5001))
cubes = [x**3 for x in x_values]

# プロットを作成する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, edgecolor='none', s=10)

# グラフのタイトルと軸ラベルを設定する
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# 軸のメモリラベルを設定する
ax.tick_params(axis='both', labelsize=14)

# グラフを表示する
# plt.savefig('4_1_cubes5000.png')
plt.show()
