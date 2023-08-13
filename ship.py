import pygame

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/rocket.bmp')
        self.image.set_colorkey((40, 70, 70))
        self.rect = self.image.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        #Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
        #Флаг перемещения.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        #Обновляет атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #Обновление атрибута rect.
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)