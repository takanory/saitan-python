import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """ボタンの属性を初期化する"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # ボタンの大きさと属性を設定する
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # ボタンの rect オブジェクトを生成し画面の中央に配置する
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # ボタンのメッセージは一度だけ準備する必要がある
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """msgを画像に変換しボタンの中央に配置する"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 空白のボタンを描画し、メッセージを描画する
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
