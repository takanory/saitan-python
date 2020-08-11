favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'takanory': ['barcelona', 'billund', 'taipei'],
    'zenich': ['san francisco', 'amsterdam', 'campbell river'],
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}が好きな場所は以下です。")
    for place in places:
        print(f"- {place.title()}")
