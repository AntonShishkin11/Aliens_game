class GameStats():
    """Отселиживание статистики игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """Инициализирует стаитстику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit