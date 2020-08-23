filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # 余分な空行を取り除いてから「Python」を「C言語」に置き換える。
    line = line.rstrip()
    print(line.replace('Python', 'C言語'))
