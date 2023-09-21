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
            
    # Duck method. Sets the character sprite and position to the ducking ones.

    def duck(self):

        self.image = self.duckImage[self.stepIndex // 5]
        self.protagonistRect = self.image.get_rect()
        self.protagonistRect.x = self.X_POS_DUCK
        self.protagonistRect.y = self.Y_POS_DUCK
        self.stepIndex += 1
    
    # Run method. Sets the character sprite and position to the running ones."""

    def run(self):

        self.image = self.runImage[self.stepIndex // 5]
        self.protagonistRect = self.image.get_rect()
        self.protagonistRect.x = self.X_POS
        self.protagonistRect.y = self.Y_POS
        self.stepIndex += 1
    
    """ Run method. Sets the character sprite and position to the jumping ones.
    Y position decreases so it looks like the character is jumping until it has reached the ground
    where the values restart."""

    def jump (self): 

        self.image = self.jumpImage

        if self.protagonistJump:
            self.protagonistRect.y -= self.jumpVelocity * 4
            self.jumpVelocity -= 0.8

        if self.jumpVelocity < -self.JUMP_VEL:
            self.protagonistJump = False
            self.jumpVelocity = self.JUMP_VEL
    
    # Drawing method. Displays the character on screen.

    def draw(self):
        
        SCREEN.blit(self.image, (self.protagonistRect.x, self.protagonistRect.y))

# Definition of the Enemy class.

class Enemy:
    
    """ Constructor of the Enemy class. It stablishes the characteristics of the enemy: 
    the reference of the image, the type of each item, the limits of the item by the 
    function rect, the position on screen and the attribute collide."""
    
    def __init__ (self, image, type):
        
        self.image = image
        self.type = type

        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

        self.collideRect = pygame.rect.Rect((0, 0), (self.rect.width * 0.8, self.rect.height * 0.9))
    
    
    """Update method. Update the position of the enemy on screen 
    and when it eliminates the enemy on the list. """
    
    def update(self):

        self.rect.x -= gameSpeed
        self.collideRect.x -= gameSpeed

        if self.rect.x < -self.rect.width:
            enemies.pop()
    
    """Draw method. Show on screen the item."""
    
    def draw (self):

        SCREEN.blit(self.image[self.type], self.rect)

# Class derived from Enemy class, it specifies stiff enemies that scroll along the background.

class Obstacle(Enemy):

    def __init__(self, image):

        # Gets enemy type, there are three: Cat, Deer and Peacock.

        self.type = random.randint(0, 2)

        # Calls upper class constructor.

        super().__init__(image, self.type)

        # Specifies position of enemy based on its type.

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

# Definition of the Item class.

class Item:
    
    """ Constructor of the Item class. It stablishes the characteristics of the item: 
    the reference of the image, the type of each item, the limits of the item by the 
    function rect, the position on screen and tha attribute of invencible when protagonist 
    reach the item."""
    
    def __init__ (self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.invencible = False
    
    """Update method. Update the position of the item on screen 
    and when it eliminates the item on the list. """
    
    def update (self):
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width-2500:
            items.pop()
    
    """Draw method. Show on screen the item."""
    
    def draw (self):
        SCREEN.blit(self.image[self.type], self.rect)
    
    """Activate method. Update the invencible attribute."""
      
    def activate (self):
        self.invencible = True

# Definition of the Shield class.  
   
class Shield(Item):
    
    """ Constructor of the Shield class, which is a subclass of Item. It stablishes 
    the characteristics of the shield: the reference of the image, the type of each 
    shield, the limits of the shield by the function rect, the position on screen 
    and the attribute of invencible when protagonist reach the shield."""
    
    def __init__ (self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.invencible = False
    
    """Draw method. Show on screen the shield."""
    
    def draw (self):
        SCREEN.blit(self.image[self.type], self.rect)
    
    """ Constructor of the Shield class. It initialize randomly which type of shield 
    will show the game. If its the first one will show higher up on screen than the 
    second."""
    
    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)

        if self.type == 0:
            self.rect.y = 350
        elif self.type == 1:
            self.rect.y = 450
    
    """Update method. Updates the position of the shield on the screen 
    and removes the shield from the item list when it reaches a certain distance.
    Shields of type 0 persist longer than shields of type 1."""
    
    def update (self):
        self.rect.x -= gameSpeed
        if self.type == 0:
            if self.rect.x < -self.rect.width-3000:
                items.pop()
        elif self.type == 1:
            if self.rect.x < -self.rect.width-2000:
                items.pop()
                
    """Activate method. Update the invencible attribute.""" 
    
    def activate (self):
        self.invencible = True

# Definition of the Button class. An instance of this class is used on the menu.

class Button:
    
    """ Constructor for the Button class. It sets its image and rect attributes and
    stablishes that the button is not clicked at first."""

    def __init__(self, x, y, image):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    # Method that checks if the button is pressed and draws it on screen.

    def draw(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

""" Method to display the menu. It stablishes the fonts for the title and subtitle text, creates and positions
them along with the button."""

def menu(death_count):
    
    # Fonts.

    MENU_TITLE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 100)
    MENU_SUBTITLE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 40)
    
    # Creation and siting of title text.

    TITLE_TEXT = MENU_TITLE_FONT.render("TEUS GAME", True, "#C1EB17")
    TITLE_TEXT_RECT = TITLE_TEXT.get_rect()
    TITLE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6)

    # Creation and sitting of button.

    START_BUTTON_IMAGE = pygame.image.load(os.path.join("assets/other", "startIcon.png"))
    START_BUTTON = Button(SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 3, START_BUTTON_IMAGE)

    # Plays the menu music.

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join("assets/other", "menuMusic.mp3")))
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        
        # If close window button is pressed, execution stops.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # If button is clicked, menu changes to main function, where the game takes place.

        if START_BUTTON.clicked == True:
            SCREEN.fill("black")
            main()

        # Display of menu background, title text and button.

        SCREEN.blit(BG[1], (0, 0))
        SCREEN.blit(TITLE_TEXT, TITLE_TEXT_RECT)
        START_BUTTON.draw()

        """ Creates subtitle text based on death count. Also creates, ubicates and displays score text if the game has already
        been played once."""

        if death_count == 0:
            SUBTITLE_TEXT = MENU_SUBTITLE_FONT.render("PRESS THE BUTTON TO START", True, "#83EBE7")
        elif death_count > 0:
            SUBTITLE_TEXT = MENU_SUBTITLE_FONT.render("PRESS THE BUTTON TO RESTART", True, "#83EBE7")

            SCORE_TEXT = MENU_SUBTITLE_FONT.render("Your Score: " + str(points), True, "#9CD7EB")
            SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
            SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 2 + (SCREEN_WIDTH // 24))

            SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)
        
        # Displays subtitle text.

        SUBTITLE_TEXT_RECT = SUBTITLE_TEXT.get_rect()
        SUBTITLE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_WIDTH // 6 * 2)

        SCREEN.blit(SUBTITLE_TEXT, SUBTITLE_TEXT_RECT)

        # Updating screen.

        clock.tick(30)
        pygame.display.update()

    # Menu music stops playing.

    pygame.mixer.music.stop()

# Method where game takes place.

def main():
    
    """ Declaration of global variables of speed of game, position of the background,
    points and list of enemies and items."""

    global gameSpeed, xPosBg, yPosBg, points, enemies, items

    # Definition of variables, which includes non global font for the score text in the game and death count.
    
    SCORE_FONT = pygame.font.Font(os.path.join("assets/other", "arcadeFont.ttf"), 20)
    gameSpeed = 20
    xPosBg = 0
    yPosBg = 0
    points = 0
    enemies = []
    items = []
    death_count = 0
    
    # Method for increasing points, accelerating game if certain points are won, and rendering score text.

    def score():

        global points, gameSpeed

        points += 1

        if points % 200 == 0:
            gameSpeed += 1

        SCORE_TEXT = SCORE_FONT.render("Points: " + str(points), True, (0, 0, 0))
        SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
        SCORE_TEXT_RECT.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 15)
        SCREEN.blit(SCORE_TEXT, SCORE_TEXT_RECT)

    """Method por displaying background by countiniously rendering the same background image one after
    another and moving them along with the game speed."""

    def background():

        global xPosBg, yPosBg

        image_width = BG[0].get_width()

        SCREEN.blit(BG[0], (xPosBg, yPosBg))
        SCREEN.blit(BG[0], (image_width + xPosBg, yPosBg))

        if xPosBg <= -image_width:
            SCREEN.blit(BG[0], (image_width + xPosBg, yPosBg))
            xPosBg = 0

        xPosBg -= gameSpeed

    # Setting game caption and icon.

    pygame.display.set_caption('Teus Game')
    pygame.display.set_icon(pygame.image.load(os.path.join("assets/other", "gameIcon.png")))

    # Play game music.

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join("assets/other", "mainMusic.mp3")))

    # Creating instance of Protagonist class for the game character.

    PLAYER = Protagonist()

    run = True
    clock = pygame.time.Clock()

    # Game loop.

    while run:
        
        # If close window button is pressed, execution stops.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Gets user keyboard input.

        userInput = pygame.key.get_pressed()

        # Draws background and character, also updates the last one based on input.

        background()

        PLAYER.draw()
        PLAYER.update(userInput)

        # Generates random enemies and items.

        if len(enemies) == 0:

            if random.randint(0, 2) == 0:
                enemies.append(Obstacle(OBSTACLE))

        if len(items) == 0:

            if random.randint(0, 100) == 0:
                items.append(Shield(SHIELD))

        """ Draws and updates obstacles, 
         if protagonist touches them game is over and menu function is called."""

        for obstacle in enemies:
            obstacle.draw()
            obstacle.update()

            if PLAYER.protagonistRect.colliderect(obstacle.collideRect):
                if len(items) == 0 :
                    pygame.time.delay(500)
                    death_count += 1
                    menu(death_count)
                elif (len(items) > 0):
                    if (items[0].invencible == True):
                        print ("Power Up\n")
                    else :
                        pygame.time.delay(500)
                        death_count += 1
                        menu(death_count)

        """ Draws and updates shields, 
         if protagonist touches them game gains invulnerability, more or less,
         doesn't die when touched by obstacle."""
                
        for shield in items:
            shield.draw()
            shield.update()

            if PLAYER.protagonistRect.colliderect(shield.rect):
                shield.activate()
            
        # Displays points.

        score()

        # Updating screen.

        clock.tick(30)
        pygame.display.update()

# Calls menu function by first time, with death count equal to zero.

menu(death_count = 0)