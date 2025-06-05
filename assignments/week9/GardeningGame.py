# my plan is a planting game, where you can plant seed, then water them and they grow after a pre-defined amount of seconds.
# EXTRAS: adding different types of plants, adding a cat walking instead of a just flowing gießkanne

#Final: so as you can see no cat :,) and a lot of thinks actually dont look like I imagined, but im happy with the end result!
#Also Im suprised at what I can actually already code, tho I have to admit, there was a lot of googling and youtube involved

import pygame
import time
import random
import sys

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255, 255, 255)
SPEED = 5
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# colors
WHITE = (255, 255, 255)
GREEN = (53, 94, 59)
BROWN = (54, 21, 9)

# Initialize pygame
pygame.init()
pygame.display.set_caption('Gardening Game')

# clock
clock = pygame.time.Clock()
FPS = 60

# watering timing
watering_start_time = 0
WATERING_DURATION = 1
is_watering = False

# images
BACKGROUND_PICTURE = pygame.image.load("backgroundpicture.jpg")
BACKGROUND_PICTURE = pygame.transform.scale(BACKGROUND_PICTURE, (SCREEN_WIDTH, SCREEN_HEIGHT))
WATERING_PICTURE = pygame.image.load("watering.png")


class GameObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_pos(self):
        return self._x, self._y

    def set_pos(self, x, y):
        self._x = x
        self._y = y


class Plant(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__growth_stage = 0
        self.__max_stage = 5
        self.__planted_time = time.time()

    def grow(self):
        if time.time() - self.__planted_time > 1:
            if self.__growth_stage < self.__max_stage:
                self.__growth_stage += 1
                self.__planted_time = time.time()

    def get_stage(self):
        return self.__growth_stage

    def draw(self, surface):
        color = (0, 255 - self.__growth_stage * 40, 0)
        pygame.draw.rect(surface, color, (self._x, self._y - self.__growth_stage * 10, 20, self.__growth_stage * 10 + 20))


class WateringCan(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.original_image = pygame.transform.scale(WATERING_PICTURE, (100, 100))
        self.image = self.original_image
        self.angle = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._x -= SPEED
        if keys[pygame.K_RIGHT]:
            self._x += SPEED

    def rotate(self, is_watering):
        self.angle = 30 if is_watering else 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def draw(self, surface):
        rotated_rect = self.image.get_rect(center=(self._x + 50, self._y + 50))
        surface.blit(self.image, rotated_rect.topleft)


plants = []
watering_can = WateringCan(100, SCREEN_HEIGHT - 150)


def handle_events():
    global is_watering, watering_start_time, plants
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            plants.append(Plant(x, y))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                is_watering = True
                watering_start_time = time.time()
                for plant in plants:
                    plant.grow()
            elif event.key == pygame.K_r:
                plants = []


def instruction_screen():
    font = pygame.font.SysFont(None, 48)
    text = font.render("Click to Start Planting", True, WHITE)
    while True:
        win.fill((0, 100, 0))
        win.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return


def main():
    global is_watering
    while True:
        clock.tick(FPS)
        handle_events()
        watering_can.move()

        # End watering after a delay
        if is_watering and time.time() - watering_start_time > WATERING_DURATION:
            is_watering = False

        watering_can.rotate(is_watering)

        win.blit(BACKGROUND_PICTURE, (0, 0))
        pygame.draw.rect(win, BROWN, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))  # ground

        for plant in plants:
            plant.draw(win)

        watering_can.draw(win)
        pygame.display.update()


instruction_screen()
main()

#HOW TO USE IT!!!
# ~ Click to plant a seed
# ~ Press G to water all plants // G for Grow, everytime you water they grow one stage
# ~ Press R to clear everything you have grown
# ~ move the watering can to water each individual plant (dosnt actually make a difference, but I tried :,) )
# "Goal" is to have fun with many plants