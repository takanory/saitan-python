import sys

import pygame

from settings import Settings

class AlienInvasion:
    """ゲームのアセットと動作を管理する全体的なクラス"""

    def __init__(self):
        """ゲームを初期化し、ゲームのリソースを作成する"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("エイリアン侵略")

    def run_game(self):
        """ゲームのメインループを開始する"""
        while True:
            # キーボードとマウスのイベントを監視する
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # ループを通過するたびに画面を再描画する
            self.screen.fill(self.settings.bg_color)

            # 最新の状態の画面を表示する
            pygame.display.flip()

if __name__ == '__main__':
    # ゲームのインスタンスを作成し、ゲームを実行する
    ai = AlienInvasion()
    ai.run_game()
