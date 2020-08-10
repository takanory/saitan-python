rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'amazon': 'brazil',
    }

for river, country in rivers.items():
    print(f"{river.title()}は{country.title()}を流れている。")

print("\nこのデータセットには、以下の川が含まれています。")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nこのデータセットには、以下の国が含まれています。")
for country in rivers.values():
    print(f"- {country.title()}")
