prompt = "\n何をピザにトッピングしたいですか?"
prompt += "\n終わったら '終了' と入力してください。）: "

while True:
    topping = input(prompt)
    if topping != '終了':
        print(f"  あなたのピザに{topping}をトッピングします。")
    else:
        break
