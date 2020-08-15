class User():
    """ユーザーのプロフィールを表すクラス"""

    def __init__(self, first_name, last_name, username, email, location):
        """ユーザーを初期化する"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """ユーザーの情報を出力する"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  ユーザー名: {self.username}")
        print(f"  メールアドレス: {self.email}")
        print(f"  場所: {self.location}")

    def greet_user(self):
        """ユーザー宛のあいさつメッセージを出力する"""
        print(f"\nおかえりなさい{self.username}！")

    def increment_login_attempts(self):
        """ログイン試行回数を1増やす"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ログイン試行回数を0にリセットする"""
        self.login_attempts = 0


takanory = User('takanori', 'suzuki', 'takanory', 'takanory@example.com',
                'toshima-ku')
takanory.describe_user()
takanory.greet_user()

print("\n3回ログインを試します...")
takanory.increment_login_attempts()
takanory.increment_login_attempts()
takanory.increment_login_attempts()
print(f"  ログイン試行回数: {takanory.login_attempts}")

print("ログイン試行回数をリセットします...")
takanory.reset_login_attempts()
print(f"  ログイン試行回数: {takanory.login_attempts}")
