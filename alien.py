import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        #Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/aliens_pic.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        #Каждый новый пришелец появлется в верхнем левом углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #Сохранение точно горизонтальной позиции пришельца.
        self.x = float(self.rect.x)
