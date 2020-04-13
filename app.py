import pygame

BLACK = (0, 0, 0)


class App:
    def __init__(self):
        pygame.init()

    def mainloop(self):
        while True:
            self.main()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    def main(self):
        """他のプログラムを読み込んで実行する関数
        ここに直接処理は書かない
        """
        pass


app = App()
app.mainloop()
