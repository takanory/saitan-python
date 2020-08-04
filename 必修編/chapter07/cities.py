prompt = "\n行ったことのある街を教えてください："
prompt += "\n（終わったら '終了' と入力してください。） "

while True:
    city = input(prompt)

    if city == '終了':
        break
    else:
        print(f"{city.title()}に行くのって最高です!")
