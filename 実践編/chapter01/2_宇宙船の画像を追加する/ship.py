import pygame

class Ship:
    """宇宙船を管理するクラス"""

    def __init__(self, ai_game):
        """宇宙船を初期化し、開始時の位置を設定する"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 宇宙船の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 新しい宇宙船を画面下部の中央に配置する
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """宇宙船を現在位置に描画する"""
        self.screen.blit(self.image, self.rect)
