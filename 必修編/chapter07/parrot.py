prompt = "\n何か書いてください。繰り返してお返事します。"
prompt += "\nプログラムを止めるには '終了' と入力してください。 "

active = True
while active:
    message = input(prompt)

    if message == '終了':
        active = False
    else:
        print(message)
