odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

print("\nリストの最初の3つの要素です。")
for number in odd_numbers[:3]:
    print(number)

print("\nリストの中央の3つの要素です。")
for number in odd_numbers[3:6]:
    print(number)

print("\nリストの最後の3つの要素です。")
for number in odd_numbers[-3:]:
    print(number)
