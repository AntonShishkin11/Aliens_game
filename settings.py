class Settings():
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана.
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (40, 70, 70)
        #Настройки корабля.
        self.ship_speed = 0.5
        #Параметры снаряда.
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = (100, 0, 0)
        self.bullets_allowed = 3