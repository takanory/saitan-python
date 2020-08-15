glossary = {
    'string': '一連の文字。',
    'comment': 'プログラム内のメモで、Pythonインタープリタは無視する。',
    'list': '特定の順番のアイテムの集まり。',
    'loop': 'アイテムの集まりを1つずつ処理すること。',
    'dictionary': "キーと値のペアの集まり。",
    }

word = 'string'
print(f"{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
