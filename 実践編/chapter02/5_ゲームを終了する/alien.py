import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """艦隊の中の1匹のエイリアンを表すクラス"""

    def __init__(self, ai_game):
        """エイリアンを初期化し、開始時の位置を設定する"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # エイリアンの画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 新しいエイリアンを画面の左上の近くに配置する
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # エイリアンの実際の位置を格納する
        self.x = float(self.rect.x)

    def check_edges(self):
        """エイリアンが画面の端に達した場合は True を返す"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """エイリアンを右または左に移動する"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
