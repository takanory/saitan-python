# 空白を含んだ文字列からメソッドを使用して空白を取り除く
name = "\tTakanori Suzuki\n"

print("そのまま出力")
print(name)

print("\nlstrip()を使用")
print(name.lstrip())  # 左側の空白を取り除く

print("\nrstrip()を使用")
print(name.rstrip())  # 右側の空白を取り除く

print("\nstrip()を使用")
print(name.strip())  # 左右の空白を取り除く
