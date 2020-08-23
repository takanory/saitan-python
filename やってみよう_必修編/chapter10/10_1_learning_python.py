filename = 'learning_python.txt'

print("--- ファイル全体を読み込む:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- ファイルの各行ををループ:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- 各行をリストに格納する:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
