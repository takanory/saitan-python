class AnonymousSurvey:
    """アンケートの質問に対する匿名の回答を集める"""

    def __init__(self, question):
        """質問を格納し、回答を格納する領域を用意する"""
        self.question = question
        self.responses = []

    def show_question(self):
        """アンケートの質問を表示する"""
        print(self.question)

    def store_response(self, new_response):
        """質問に対する回答を1件格納する"""
        self.responses.append(new_response)

    def show_results(self):
        """すべての回答を表示する"""
        print("アンケートの回答:")
        for response in self.responses:
            print(f"- {response}")
