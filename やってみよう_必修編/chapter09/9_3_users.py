class User():
    """ユーザーのプロフィールを表すクラス"""

    def __init__(self, first_name, last_name, username, email, location):
        """ユーザーを初期化する"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """ユーザーの情報を出力する"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  ユーザー名: {self.username}")
        print(f"  メールアドレス: {self.email}")
        print(f"  場所: {self.location}")

    def greet_user(self):
        """ユーザー宛のあいさつメッセージを出力する"""
        print(f"\nおかえりなさい{self.username}！")


takanory = User('takanori', 'suzuki', 'takanory', 'takanory@example.com',
                'toshima-ku')
takanory.describe_user()
takanory.greet_user()

zenich = User('zenichiro', 'yasuda', 'zenich', 'zen@example.com', 'chofu')
zenich.describe_user()
zenich.greet_user()
