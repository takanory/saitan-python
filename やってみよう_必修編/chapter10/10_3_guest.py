name = input("お名前は？ ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
