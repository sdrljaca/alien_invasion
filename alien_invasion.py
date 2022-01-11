import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasions:

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alieen Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the mail loop for the game"""
        while True:
            # Lauscht auf Tastatur- und Mausereignisse.
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Bewegt das Schiff nacht rechts
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Macht den zuletzt gezeichneten Bildschrim sichtbar.
        pygame.display.flip()

if __name__ == '__main__':
    # Uspostavlja instanzu za igru i pokreće igru
    ai = AlienInvasions()
    ai.run_game()