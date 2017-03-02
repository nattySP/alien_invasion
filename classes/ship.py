import pygame

class Ship():

    def __init__(self, screen, settings):
        self.screen = screen
        self.image = pygame.image.load('images/cupcake.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom + 50
        self.moving_right = False
        self.moving_left = False
        self.min_speed = settings.ship_min_speed
        self.speed = self.min_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        self.center+= self.speed

    def move_left(self):
        self.center -= self.speed

    def handle_move(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.move_right()
        if self.moving_left and self.rect.left > 0:
            self.move_left()

        self.rect.centerx = self.center

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        if self.speed - 5 > self.min_speed:
            self.speed -= 5