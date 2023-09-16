""" Import pygame module for 2D videogame development functionalities,
 os module for file access, random module to control the rate of ocurrence
 of elements and sys module for quitting the game."""

import pygame
import os
import random
import sys

# Start pygame module.

pygame.init()

""" Definition of global constants, such as the screen dimensions and the screen itself,
the running, jumping, ducking, backgrounds, obstacles and shields assets."""

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 762
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistRun1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistRun2.png"))]
JUMPING = pygame.image.load(os.path.join("assets/protagonist", "protagonistJump.png"))
DUCKING = [pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck1.png")),
           pygame.image.load(os.path.join("assets/protagonist", "protagonistDuck2.png"))]
BG = [pygame.image.load(os.path.join("assets/other", "background.jpg")), pygame.image.load(os.path.join("assets/other", "menuBackground.jpg"))]

OBSTACLE = [pygame.image.load(os.path.join("assets/obstacles", "obstacle1.png")),
                pygame.image.load(os.path.join("assets/obstacles", "obstacle2.png")),
                pygame.image.load(os.path.join("assets/obstacles", "obstacle3.png"))]

SHIELD = [pygame.image.load(os.path.join("assets/powerUps", "shield1.png")), pygame.image.load(os.path.join("assets/powerUps", "shield2.png"))]

# Definition of the Protagonist class

class Protagonist:

    """ Attributes of the Protagonist class, such as the x and y position
    when running and ducking and the jump velocity. These are meant to
    be first value constants since the sprite itself will be modified
    using the pygame Rect object."""

    X_POS = 80 
    Y_POS = 620
    X_POS_DUCK = 76
    Y_POS_DUCK = 660
    JUMP_VEL = 8.5
    
    """ Constructor of the Protagonist class. It stablishes the character
    sprites for each action, that the character itself will be running 
    at first instance, its jump velocity variable that starts with the
    previously defined constant value but it's set to be changing with the 
    character fall and the step index responsible for the sprite alternation."""

    def __init__(self):
        
        self.runImage = RUNNING
        self.jumpImage = JUMPING
        self.duckImage = DUCKING
        
        self.protagonistRun = True
        self.image = self.runImage[0]

        self.protagonistDuck = False

        self.protagonistJump = False
        self.jumpVelocity = self.JUMP_VEL

        self.protagonistRect = self.image.get_rect()
        self.protagonistRect.x = self.X_POS
        
        self.stepIndex = 0

    """ Definition of the update method that will be called constantly
    to change the character action based on user interaction."""
        
    def update(self, userInput):
        
        """ If up key is pressed an the character is not jumping already
        set the character action to jump. Otherwise, if down key is pressed 
        and the character is not jumping set the character action to duck.
        Finally, if the character is not jumping or is not pressing the
        down key, set its action to run."""

        if userInput[pygame.K_UP] and not self.protagonistJump:

            self.protagonistRun = False
            self.protagonistDuck = False
            self.protagonistJump = True
        elif userInput[pygame.K_DOWN] and not self.protagonistJump:

            self.protagonistRun = False
            self.protagonistDuck = True
            self.protagonistJump = False

        elif not (self.protagonistJump or userInput [pygame.K_DOWN]):

            self.protagonistRun = True
            self.protagonistDuck = False
            self.protagonistJump = False

        # Execute the corresponding method based on the previous check.

        if self.protagonistDuck:
            
            self.duck()

        if self.protagonistRun:
            
            self.run()

        if self.protagonistJump:
           
            self.jump()

        # Reset step index.

        if self.stepIndex >= 10:

            self.stepIndex = 0
            
    """Duck method. Sets the character sprite to the ducking one."""
    def duck(self):

        self.image = self.duckImage[self.stepIndex // 5]
        self.protagonistRect = self.image.get_rect()
        self.protagonistRect.x = self.X_POS_DUCK
        self.protagonistRect.y = self.Y_POS_DUCK
        self.stepIndex += 1
        
    def run(self):

        self.image = self.runImage[self.stepIndex // 5]
        self.protagonistRect = self.image.get_rect()
        self.protagonistRect.x = self.X_POS
        self.protagonistRect.y = self.Y_POS
        self.stepIndex += 1
        
    def jump (self): 

        self.image = self.jumpImage

        if self.protagonistJump:
            self.protagonistRect.y -= self.jumpVelocity * 4
            self.jumpVelocity -= 0.8

        if self.jumpVelocity < -self.JUMP_VEL:
            self.protagonistJump = False
            self.jumpVelocity = self.JUMP_VEL
            
    def draw(self):
        
        SCREEN.blit(self.image, (self.protagonistRect.x, self.protagonistRect.y))

class Enemy:

    def __init__ (self, image, type):
        
        self.image = image
        self.type = type

        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

        self.collideRect = pygame.rect.Rect((0, 0), (self.rect.width * 0.8, self.rect.height * 0.9))
    
    def update(self):

        self.rect.x -= gameSpeed
        self.collideRect.x -= gameSpeed

        if self.rect.x < -self.rect.width:
            enemies.pop()
    
    def draw (self):

        SCREEN.blit(self.image[self.type], self.rect)

class Obstacle(Enemy):

    def __init__(self, image):

        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        if self.type == 0:

            self.rect.y = 623
            self.collideRect.y = self.rect.y + 90
            self.collideRect.x = SCREEN_WIDTH + 53

        elif self.type == 1:

            self.rect.y = 602
            self.collideRect.y = self.rect.y + 120
            self.collideRect.x = SCREEN_WIDTH + 55

        else:

            self.rect.y = 628
            self.collideRect.y = self.rect.y + 90
            self.collideRect.x = SCREEN_WIDTH + 50

class Item:

    def __init__ (self, image, type):

        self.image = image
        self.type = type

        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

        self.collideRect = pygame.rect.Rect((0, 0), (self.rect.width * 0.8, self.rect.height * 0.9))
    
    def update (self):

        self.rect.x -= gameSpeed
        self.collideRect.x -= gameSpeed

        if self.rect.x < -self.rect.width:
            items.pop()
    
    def draw (self):

        SCREEN.blit(self.image[self.type], self.rect)
        
class Shield(Item):
    
    def __init__(self, image):
        
        self.type = random.randint(0,1)
        super().__init__(image, self.type)

        self.rect.y = 350
        self.collideRect.y = self.rect.y + 90
        self.collideRect.x = SCREEN_WIDTH + 53

        if self.type == 0:

            self.protectionTime = 10000

        else:

            self.protectionTime = 15000

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

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join("assets/other", "menuMusic.mp3")))

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
    
    global gameSpeed, x_pos_bg, y_pos_bg, points, enemies, items
    
    SCORE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 20)
    gameSpeed = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    enemies = []
    items = []
    death_count = 0
    
    def score():

        global points, gameSpeed

        points += 1

        if points % 200 == 0:
            gameSpeed += 1

        SCORE_TEXT = SCORE_FONT.render("Points: " + str(points), True, (0, 0, 0))
        SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
        SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 15)
        SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)

    def background():

        global x_pos_bg, y_pos_bg

        image_width = BG[0].get_width()

        SCREEN.blit(BG[0], (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG[0], (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0

        x_pos_bg -= gameSpeed

    pygame.display.set_caption('Teus Game')
    pygame.display.set_icon(pygame.image.load(os.path.join("assets/other", "gameIcon.png")))

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join("assets/other", "mainMusic.mp3")))

    PLAYER = Protagonist()

    run = True
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        SCREEN.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()

        background()

        PLAYER.draw()
        PLAYER.update(userInput)

        if len(enemies) == 0:

            if random.randint(0, 2) == 0:
                enemies.append(Obstacle(OBSTACLE))

        if len(items) == 0:

            if random.randint(0, 100) == 0:
                items.append(Shield(SHIELD))

        for obstacle in enemies:
            obstacle.draw()
            obstacle.update()

            if PLAYER.protagonistRect.colliderect(obstacle.collideRect):
                pygame.time.delay(500)
                death_count += 1
                menu(death_count)

        for shield in items:
            shield.draw()
            shield.update()

            if PLAYER.protagonistRect.colliderect(shield.collideRect):
                print("a")
                    
        score()

        clock.tick(30)
        pygame.display.update()

menu(death_count = 0)