age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 2500
elif age < 65:
    price = 4000
elif age >= 65:
    price = 2000

print(f"入場料金は{price}円です。")
