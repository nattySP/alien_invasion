import sys
import pygame
from classes.bullet import Bullet
from classes.alien import Alien

def check_events(settings, screen, ship, bullets):
    # watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or detect_q(event):
            sys.exit()
        elif (event.type == pygame.KEYDOWN):
            handle_keydown(event, settings, screen, ship, bullets)
        elif (event.type == pygame.KEYUP):
            handle_keyup(ship, event)
    ship.handle_move()


def update_screen(screen, settings, ship, bullets, aliens):
    screen.blit(settings.bg_image, (0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    pygame.display.flip()

def handle_keyup(ship, event):
    if (event.key == pygame.K_RIGHT):
        ship.moving_right = False
    elif (event.key == pygame.K_LEFT):
        ship.moving_left = False

def handle_keydown(event, settings, screen, ship, bullets):
    if (event.key == pygame.K_RIGHT):
        ship.moving_right = True
    elif (event.key == pygame.K_LEFT):
        ship.moving_left = True
    elif (event.key == pygame.K_UP):
        ship.increase_speed()
    elif (event.key == pygame.K_DOWN):
        ship.decrease_speed()
    elif (event.key == pygame.K_SPACE):
        fire_bullet(bullets, settings, screen, ship)

def update_bullets(bullets):
    bullets.update()
    remove_bullets(bullets)

def remove_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(bullets, settings, screen, ship):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def detect_q(event):
    return event.type == pygame.KEYDOWN and event.key == pygame.K_q

def create_fleet(settings, screen, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width

    available_space_width = settings.screen_width - (2 * alien_width)
    number_aliens = int(available_space_width / (alien_width * 2))

    for alien_number in range(number_aliens):
        alien = Alien(settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)