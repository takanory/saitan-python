favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}の好きなプログラミング言語は{language.title()}です。")

print("")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"{coder.title()}、投票してくれてありがとう！")
    else:
        print(f"{coder.title()}、好きなプログラミング言語はなんですか？")
