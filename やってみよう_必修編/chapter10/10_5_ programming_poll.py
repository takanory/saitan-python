filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nプログラミングが好きな理由は何ですか？ ")
    responses.append(response)

    continue_poll = input("誰か他に回答する人はいますか？ (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
