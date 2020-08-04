def get_formatted_name(first, last, middle=''):
    """フォーマットされたフルネームを返す"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
