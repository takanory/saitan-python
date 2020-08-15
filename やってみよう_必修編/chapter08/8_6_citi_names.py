def city_country(city, country):
    """'Santiago, Chile' のような文字列を返す"""
    return f"{city.title()}, {country.title()}"


city = city_country('santiago', 'chile')
print(city)

city = city_country('taipei', 'taiwan')
print(city)

city = city_country('kota kinabalu', 'malaysia')
print(city)
