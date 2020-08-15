def describe_city(city, country='日本'):
    """都市について説明する"""
    msg = f"{city}は{country}にあります。"
    print(msg)


describe_city('京都')
describe_city('レイキャビク', 'アイスランド')
describe_city('札幌')
