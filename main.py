import pygame
import os

pygame.init()

# GLOBAL CONSTANTS

SCREEN_WIDTH = 1100
SCREEN_HEIGTH = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

RUNNING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistRun1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistJump.png"))]
DUCKING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck2.png"))]

def main():

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()