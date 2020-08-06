import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ゲームのアセットと動作を管理する全体的なクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを作成する"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("エイリアン侵略")

        self.ship = Ship(self)

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """キーボードとマウスのイベントに対応する"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """画面上の画像を更新し、新しい画面に切り替える"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = AlienInvasion()
    ai.run_game()
