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

class Protagonist:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    
    def __init__(self):
    
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        
        self.protagonist_duck = False
        self.protagonist_run = True
        self.protagonist_jump = False
        
        self.step_index = 0
        self.img = self.run_img[0]
        self.protagonist_rect = self.imgn.get_rect ()
        self.protagonist_rect.x = self.X_POS
        self.protagonist_rect.y = self.Y_POS
    
    def update (self, userInput):
        if self.protagonist_duck:
            self.duck()
        if self.protagonist_run:
            self.run()
        if self.protagonist_jump:
            self.jum()
        
        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput [pygame.K_UP] and not self.protagonist_jump:
            self.protagonist_duck = False
            self.protagonist_run = False
            self.protagonist_jump = True
        elif userInput [pygame.K_DOWN] and not self.protagonist_jump:
            self.protagonist_duck = True
            self.protagonist_run = False
            self.protagonist_jump = False
        elif not (self.protagonist_jump or userInput [pygame.K_DOWN]):
            self.protagonist_duck = False
            self.protagonist_run = True
            self.protagonist_jump = False
            
def duck (self):
    self.img = self.duck_img[self.step_index // 5]
    self.protagonist_rect = self.img.get_rect()
    self.protagonist_rect.x = self.X_POS
    self.protagonist_rect.y = self.Y_POS_DUCK
    self.step_index += 1
    
def run(self):
    self.img = self.run_img[self.step_index // 5]
    self.protagonist_rect = self.img.get_rect()
    self.protagonist_rect.x = self.X_POS
    self.protagonist_rect.y = self.Y_POS
    self.step_index += 1
    
def jump (self):
    self.img = self.jum_img
    if self.protagonist_jump:
        self.protagonist_rect.y -=self.jump_vel * 4
        self.jump_vel -= 0.8
    if self.jump_vel < - self.JUMP_VEL:
        self.protagonist_jump = False
        self.jump_vel = self.JUMP_VEL
        
def draw(self, SCREEN):
    SCREEN.blit(self.image, (self.protagonist_rect.x, self.protagonist_rect.y))

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