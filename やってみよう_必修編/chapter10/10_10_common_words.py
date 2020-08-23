def count_common_words(filename, word):
    """テキスト内の単語の出現回数を数える。"""
    # 注意: これは本当に単純な近似値です。実際の出現回数よりも大きな数が返されるでしょう。
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"単語'{word}'は{filename}内に約{word_count}回出現します。"
        print(msg)

filename = 'alice.txt'
count_common_words(filename, 'the')
