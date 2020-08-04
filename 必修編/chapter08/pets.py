def describe_pet(pet_name, animal_type='イヌ'):
    """ペットについての情報を出力する。"""
    print(f"\n私は{animal_type}を飼っています。")
    print(f"{animal_type}の名前は{pet_name.title()}です。")

describe_pet(pet_name='ウィリー')
