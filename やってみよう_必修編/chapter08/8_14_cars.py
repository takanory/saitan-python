def make_car(maker, model, **options):
    """自動車を表す辞書を作成する"""
    car_dict = {
        'maker': maker.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


subaru = make_car('スバル', 'レガシィ', color='ブルー', recorder=True)
print(subaru)

accord = make_car('honda', 'accord', year=1991, color='白',
                  headlights='popup')
print(accord)
