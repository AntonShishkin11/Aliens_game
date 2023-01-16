import sys

import pygame

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (40, 70 ,70)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            #Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            #Отображение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()