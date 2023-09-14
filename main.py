import pygame
import os

pygame.init()

# GLOBAL CONSTANTS

SCREEN_WIDTH = 1200
SCREEN_HEIGTH = 762
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

RUNNING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistRun1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistRun2.png"))]
JUMPING = pygame.image.load(os.path.join("assets/protagonist", "protagonistJump.png"))
DUCKING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck2.png"))]
BG = pygame.image.load(os.path.join("assets/other", "background.jpg"))

class Protagonist:

    X_POS = 80
    Y_POS = 620
    X_POS_DUCK = 76
    Y_POS_DUCK = 660
    JUMP_VEL = 8.5
    
    def __init__(self):
    
        self.duck_image = DUCKING
        self.run_image = RUNNING
        self.jump_image = JUMPING
        
        self.protagonist_duck = False
        self.protagonist_run = True
        self.protagonist_jump = False
        
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_image[0]
        self.protagonist_rect = self.image.get_rect()
        self.protagonist_rect.x = self.X_POS
        self.protagonist_rect.y = self.Y_POS
    
    def update(self, userInput):

        if self.protagonist_duck:
            self.duck()

        if self.protagonist_run:
            self.run()

        if self.protagonist_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0
        
        if userInput[pygame.K_UP] and not self.protagonist_jump:
            self.protagonist_duck = False
            self.protagonist_run = False
            self.protagonist_jump = True

        elif userInput[pygame.K_DOWN] and not self.protagonist_jump:
            self.protagonist_duck = True
            self.protagonist_run = False
            self.protagonist_jump = False

        elif not (self.protagonist_jump or userInput [pygame.K_DOWN]):
            self.protagonist_duck = False
            self.protagonist_run = True
            self.protagonist_jump = False
            
    def duck (self):

        self.image = self.duck_image[self.step_index // 5]
        self.protagonist_rect = self.image.get_rect()
        self.protagonist_rect.x = self.X_POS_DUCK
        self.protagonist_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        
    def run(self):

        self.image = self.run_image[self.step_index // 5]
        self.protagonist_rect = self.image.get_rect()
        self.protagonist_rect.x = self.X_POS
        self.protagonist_rect.y = self.Y_POS
        self.step_index += 1
        
    def jump (self):

        self.image = self.jump_image

        if self.protagonist_jump:
            self.protagonist_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.protagonist_jump = False
            self.jump_vel = self.JUMP_VEL
            
    def draw(self, SCREEN):
        
        SCREEN.blit(self.image, (self.protagonist_rect.x, self.protagonist_rect.y))

def main():
    
    pygame.display.set_caption('Teus Game')
    pygame.display.set_icon(pygame.image.load(os.path.join("assets/other", "gameIcon.png")))

    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets/other", "slowMainMusic.mp3"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()


    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    font = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 20)

    run = True
    clock = pygame.time.Clock()

    player = Protagonist()

    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    obstacles = []
    death_count = 0

    def score():

        global points, game_speed

        points += 1

        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (600, 35)
        SCREEN.blit(text, textRect)

    def background():

        global x_pos_bg, y_pos_bg

        image_width = BG.get_width()

        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0

        x_pos_bg -= game_speed

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        background()

        player.draw(SCREEN)
        player.update(userInput)

        score()
        
        clock.tick(30)
        pygame.display.update()

main()