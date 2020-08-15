"""ユーザを表すクラスの集まり"""


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


class Admin(User):
    """管理権限を持ったユーザーを表すクラス"""

    def __init__(self, first_name, last_name, username, email, location):
        """管理者ユーザーを初期化する"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

        # 空の権限で初期化する
        self.privileges = Privileges()


class Privileges():
    """管理者の権限を格納するクラス"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """管理者が持っている権限を出力する"""
        print("\n権限の一覧")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- このユーザーには権限がありません。")
