class Settings:
    """エイリアン侵略の全設定を格納するクラス"""

    def __init__(self):
        """ゲームの初期設定"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 宇宙船の設定
        self.ship_speed = 1.5
