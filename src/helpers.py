"""処理をまとめるモジュール"""

import pygame


def load_img(path):
    """画像を読み込む.pngのみ
    読み込んだ画像を返す
    """
    image = pygame.image.load(path).convert_alpha()
    return image
