import pygame

from classes.settings import Settings
from classes.ship import Ship
import util.game_functions as game_functions
from pygame.sprite import Group


# if __name__ == '__main__':
def run_game():
    #initialize game nad create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    game_functions.create_fleet(ai_settings, screen, aliens)
    #start the main
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        game_functions.update_bullets(bullets)
        game_functions.update_screen(screen, ai_settings, ship, bullets, aliens)

run_game()



