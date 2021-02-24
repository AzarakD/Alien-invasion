import sys
import pygame

class AlineInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit():
                    sys.exit()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlineInvasion()
    ai.run_game()
