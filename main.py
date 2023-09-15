import pygame, sys
import random
import os

pygame.init()

# GLOBAL CONSTANTS

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 762
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

        self.collideRect = pygame.rect.Rect((0, 0), (self.rect.width * 0.60, self.rect.height * 0.60))
    
    def update (self):

        self.rect.x -= game_speed
        self.collideRect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()
    
    def draw (self):
        SCREEN.blit(self.image[self.type], self.rect)

class Passerby(Enemy):

    def __init__(self, image):

        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        #P
        #V
        #G

        if self.type == 0:
            self.rect.y = 623
        elif self.type == 1:
            self.rect.y = 602
        else:
            self.rect.y = 628

        self.collideRect.center = self.rect.center

        if self.type == 0:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 48
        elif self.type == 1:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 60
        else:
            self.collideRect.y = self.rect.y + 100
            self.collideRect.x = SCREEN_WIDTH + 27

class Button:
    
    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

def menu(death_count):
    
    MENU_TITLE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 100)
    MENU_SUBTITLE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 40)
   
    TITLE_TEXT = MENU_TITLE_FONT.render("TEUS GAME", True, "#C1EB17")
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6)

    START_BUTTON_IMAGE = pygame.image.load(os.path.join("assets/other", "startIcon.png"))
    START_BUTTON = Button(SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 3, START_BUTTON_IMAGE)

    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("assets/other", "menuMusic.mp3"))
    pygame.mixer.music.set_volume(0.7)
    #pygame.mixer.music.play()

    run = True
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if START_BUTTON.clicked == True:
            SCREEN.fill("black")
            main()

        SCREEN.blit(BG[1], (0, 0))
        SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
        START_BUTTON.draw()

        if death_count == 0:
            SUBTITLE_TEXT = MENU_SUBTITLE_FONT.render("PRESS THE BUTTON TO START", True, "#83EBE7")
        elif death_count > 0:
            SUBTITLE_TEXT = MENU_SUBTITLE_FONT.render("PRESS THE BUTTON TO RESTART", True, "#83EBE7")

            SCORE_TEXT = MENU_SUBTITLE_FONT.render("Your Score: " + str(points), True, "#9CD7EB")
            SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
            SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 2 + (SCREEN_WIDTH // 24))

            SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)
        
        SUBTITLE_TEXT_RECT = SUBTITLE_TEXT.get_rect()
        SUBTITLE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 2)

        SCREEN.blit(SUBTITLE_TEXT, SUBTITLE_TEXT_RECT)
        
        clock.tick(30)
        pygame.display.update()

    pygame.mixer.music.stop()

def main():
    
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    
    SCORE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 20)
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

        SCORE_TEXT = SCORE_FONT.render("Points: " + str(points), True, (0, 0, 0))
        SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
        SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)
        SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)

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

    pygame.mixer.music.load(os.path.join("assets/other", "slowMainMusic.mp3"))
    pygame.mixer.music.set_volume(0.7)
    #pygame.mixer.music.play()

    PLAYER = Protagonist()

    run = True
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        background()

        PLAYER.draw()
        PLAYER.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Passerby(OBST))

        for obstacle in obstacles:
            obstacle.draw()
            obstacle.update()

            if PLAYER.protagonist_rect.colliderect(obstacle.collideRect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
                    
        score()

        clock.tick(30)
        pygame.display.update()

menu(death_count = 0)