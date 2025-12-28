import pygame
import random
# Initialize Pygame
pygame.init()
#Cusomt event IDs for color change events
SPRITE_COLOR_CHANGE = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE = pygame.USEREVENT + 2
#define basic colors using pygamae.Color
#background colors
BLUE = pygame.Color('blue')
LIGHT_BLUE = pygame.Color('lightblue')
DARK_BLUE = pygame.Color('darkblue')
#sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
#sprite class representing a colored square
class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit =  False
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE))
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background():
        global bg_color 
        bg_color = random.choice([BLUE, LIGHT_BLUE, DARK_BLUE])