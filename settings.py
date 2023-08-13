class Settings():
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана.
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (224, 255, 255)
        #Настройки корабля.
        self.ship_speed = 0.5
        #Параметры снаряда.
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (100, 0, 0)
        self.bullets_allowed = 3
        #Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

