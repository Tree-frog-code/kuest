import pygame

# 色の定義
BLACK = (0, 0, 0)
BLUE = (19, 19, 220)


class App:
    def __init__(self):
        # 初期化
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))  # ウィンドウサイズの指定
        pygame.display.set_caption("Pygame Test")

    def mainloop(self):
        while True:
            # 背景色の指定。RGBだと思う
            pygame.screen.fill((255, 63, 10))
            pygame.display.update()
            self.main()
            for event in pygame.event.get():
                # 終了処理
                if event.type == pygame.QUIT:
                    exit()

    def main(self):
        """他のプログラムを読み込んで実行する関数
        ここに直接処理は書かない
        """
        pass


app = App()
app.mainloop()
