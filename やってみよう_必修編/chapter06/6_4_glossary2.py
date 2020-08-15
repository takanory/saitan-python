glossary = {
    'string': '一連の文字。',
    'comment': 'プログラム内のメモで、Pythonインタープリタは無視する。',
    'list': '特定の順番のアイテムの集まり。',
    'loop': 'アイテムの集まりを1つずつ処理すること。',
    'dictionary': "キーと値のペアの集まり。",
    'key': '辞書のキーと値のペアの最初の項目。',
    'value': '辞書のキーと関連付けられた項目。',
    'int': '整数の数値。',
    'float': '小数点がある数値。',
    'and': '両方の条件がTrueの場合にTrueとなり、それ以外はFalseとなる。',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
