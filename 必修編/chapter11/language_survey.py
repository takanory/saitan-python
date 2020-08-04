from survey import AnonymousSurvey

# 質問文を定義し、アンケート調査を作成する
question = "最初に勉強した言語は何ですか？"
my_survey = AnonymousSurvey(question)

# 質問を表示し、質問に対する回答を保存する
my_survey.show_question()
print("'q' を入力すると終了します\n")
while True:
    response = input("言語: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# アンケート調査の結果を表示する
print("\nアンケート調査にご協力ありがとうございます！")
my_survey.show_results()
