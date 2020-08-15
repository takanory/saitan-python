def show_messages(messages):
    """リストの中の各メッセージを出力する"""
    print("全メッセージを表示します。")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """各メッセージを出力し、sent_messagesに移動する"""
    print("\n全メッセージを送信します。")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["こんにちは", "元気ですか？", "ビール飲みたい"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\n最終的なリストの状態")
print(messages)
print(sent_messages)
