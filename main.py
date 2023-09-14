import pygame, sys
import random
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
BG = [pygame.image.load(os.path.join("assets/other", "background.jpg")), pygame.image.load(os.path.join("assets/other", "menuBackground.jpg"))]

OBST = [pygame.image.load(os.path.join("assets/obstacles", "obstaculo1.png")),
                pygame.image.load(os.path.join("assets/obstacles", "obstaculo2.png")),
                pygame.image.load(os.path.join("assets/obstacles", "obstaculo3.png"))]

SHIELD = pygame.image.load(os.path.join("assets/powerUps", "shield.png"))

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
            
    def duck(self):

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
            
    def draw(self):
        
        SCREEN.blit(self.image, (self.protagonist_rect.x, self.protagonist_rect.y))

class Enemy:

    def __init__ (self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update (self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw (self):
        SCREEN.blit(self.image[self.type], self.rect)

class Passerby(Enemy):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        if self.type == 0:
            self.rect.y = 623
        elif self.type == 1:
            self.rect.y = 602
        else:
            self.rect.y = 628

class Button:
    
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        pos = pygame.mouse.get_pos()
        print(pos)

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("a")

        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

""" def main_menu():
    
    menuTitleFont = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 100)

    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets/other", "menuMusic.mp3"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        MENU_TEXT = menuTitleFont.render("TEUS GAME", True, "#DA8EE7")
        TEXT_RECT = MENU_TEXT.get_rect()
        TEXT_RECT.center = (600, 200)

        START_BUTTON_IMAGE = pygame.image.load(os.path.join("assets/other", "startIcon.png"))

        start_button = Button(0, 0, START_BUTTON_IMAGE)

        SCREEN.blit(BG[1], (0, 0))
        SCREEN.blit(MENU_TEXT, TEXT_RECT)
        start_button.draw()

        pygame.display.update()

    pygame.mixer.music.stop() """

def main():
    
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    
    scoreFont = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 20)
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

        TEXT = scoreFont.render("Points: " + str(points), True, (0, 0, 0))
        TEXT_RECT = TEXT.get_rect()
        TEXT_RECT.center = (600, 35)
        SCREEN.blit(TEXT, TEXT_RECT)

    def background():

        global x_pos_bg, y_pos_bg

        image_width = BG[0].get_width()

        SCREEN.blit(BG[0], (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0

        x_pos_bg -= game_speed

    pygame.display.set_caption('Teus Game')
    pygame.display.set_icon(pygame.image.load(os.path.join("assets/other", "gameIcon.png")))

    #main_menu()

    pygame.mixer.music.load(os.path.join("assets/other", "slowMainMusic.mp3"))
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

    player = Protagonist()

    run = True
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        background()

        player.draw()
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Passerby(OBST))

        for obstacle in obstacles:
            obstacle.draw()
            obstacle.update()

            if player.protagonist_rect.colliderect(obstacle.rect):
                
                print("a")
                death_count += 1
                #main_menu(death_count)
                    
        score()

        clock.tick(30)
        pygame.display.update()

main()