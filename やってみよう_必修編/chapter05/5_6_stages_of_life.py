age = 17

if age < 2:
    stage = "赤ちゃん"
elif age < 4:
    stage = "幼児"
elif age < 13:
    stage = "子ども"
elif age < 20:
    stage = "ティーンエイジャー"
elif age < 65:
    stage = "大人"
else:
    stage = "高齢者"

print(f"あなたは{stage}です！")
