"""都市に関する情報を返す関数"""


def city_country(city, country, population=0):
    """'Santiago, Chile - 人口 5000000'のような文字列を返す"""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - 人口 {population}"
    return output_string
