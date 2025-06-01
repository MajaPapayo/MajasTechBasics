#making a Pygame animation based on the dvd screensaver, I worked a lot with a youtube video who explains how to do this
#I would say Is till hat to figure a lot myself, since they didn't do it in a class.

#first importing
import pygame
import random

#COnstants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BG_COLOR = (0, 0, 0)
SPEED_MIN = -3
SPEED_MAX = 3
AMOUNT_IMAGES = 10
DEGREE_SPIN = 30
# activate
pygame.init()

# making a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# name of the screen
pygame.display.set_caption("DVD Screensaver")

class Dvd:
    def __init__(self):
        # loading the image
        image = pygame.image.load('DVD Screensaver.png').convert_alpha()
        image = pygame.transform.scale(image, (100,80))
        self.image = self.change_image_color(image)

        # OG position and movement speed
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

        self.speed_x = random.randint(SPEED_MIN, SPEED_MAX)
        self.speed_y = random.randint(SPEED_MIN, SPEED_MAX)

        self.original_image = self.image #original image
        self.angle = 0

    def change_image_color(self, surface):
        r = random.randint(0, 3) * 64
        g = random.randint(0, 3) * 64
        b = random.randint(0, 3) * 64
        surface = surface.copy()
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                pixle_color = surface.get_at((x, y))
                if pixle_color[:3] != 0:
                    new_r = (pixle_color[0] + r) % 256
                    new_g = (pixle_color[1] + g) % 256
                    new_b = (pixle_color[2] + b) % 256
                    surface.set_at((x, y), (new_r, new_g, new_b, pixle_color[3]))
        return surface

    #B-B-B-B-Bonus Rotation
    def rotate_image(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


    def movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            self.image = self.change_image_color(self.original_image)
            self.angle = (self.angle + DEGREE_SPIN) % 360
            self.rotate_image()

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            self.image = self.change_image_color(self.original_image)
            self.angle = (self.angle + DEGREE_SPIN) % 360
            self.rotate_image()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# Looping this :p

#  multiple Dvd instances
dvds = [Dvd() for x in range(AMOUNT_IMAGES)]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    for dvd in dvds:
        dvd.movement()
        dvd.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()















