"""管理者ユーザーを表すクラスの集まり"""

from user2 import User


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
