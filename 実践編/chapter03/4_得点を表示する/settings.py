class Settings:
    """エイリアン侵略の全設定を格納するクラス"""

    def __init__(self):
        """ゲームの固定の設定値を初期化する"""
        # 画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 宇宙船の設定
        self.ship_limit = 3

        # 弾の設定
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # エイリアンの設定
        self.fleet_drop_speed = 10

        # ゲームのスピードアップする速さ
        self.speedup_scale = 1.1
        # エイリアンの点数が増加する量
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ゲーム中に変更される設定値を初期化する"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # 艦隊の移動方向を表し 1 は右、-1 は左に移動することを表す
        self.fleet_direction = 1

        # 点数
        self.alien_points = 50

    def increase_speed(self):
        """速度の設定値とエイリアンの点数を増やす"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
