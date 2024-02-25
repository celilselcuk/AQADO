import pygame
import random


pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("AQADo")

# colour
white_ish = (220, 220, 220)
purple = (221, 160, 221)
black = (0, 0, 0)
grey = (100, 100, 100)
red = (140, 0, 0)
blue = (16, 47, 87)
green = (28, 77, 28)
orange = (201, 59, 12)
background_col = blue
# text
my_font = pygame.font.SysFont('Arial', 36)
text_surface = my_font.render('AQADo', False, black)
my_font1 = pygame.font.SysFont('Arial', 26)
text_surface1 = my_font1.render('|~~PLAY~~|', False, black)
# checkers
name_1_entered = False
name_2_entered = False

menu_screen = True
game_screen = False
# images
Name_1 = pygame.image.load('Name 1.PNG')
Name_2 = pygame.image.load('Name 2.PNG')
Play = pygame.image.load('PLAY.PNG')
board = pygame.image.load('board.png')
a1 = pygame.image.load('a1.png')
a2 = pygame.image.load('a2.png')
b1 = pygame.image.load('b1.png')
b2 = pygame.image.load('b2.png')
# dice
d1 = pygame.image.load('d1.png')
d2 = pygame.image.load('d2.png')
d3 = pygame.image.load('d3.png')
d4 = pygame.image.load('d4.png')
d_roll = pygame.image.load('roll_img.png')


# pos
a1_y = 433
a2_y = 433
b1_y = 433
b2_y = 433
# screen stuff
screen.fill(background_col)


# button class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


Name1Button = Button(220, 250, Name_1)
Name2Button = Button(216, 320, Name_2)
Play_Button = Button(234, 410, Play)
D1 = Button(115, 500, d1)
D2 = Button(115, 500, d2)
D3 = Button(115, 500, d3)
D4 = Button(115, 500, d4)
D_ROLL = Button(115, 500, d_roll)


def dice_roll():
    possible_choices = [d1, d2, d3, d4]
    dice_choose = random.randint(1,4)
    chosen_dice = possible_choices[dice_choose - 1]
    print(dice_choose)


def counter(p1c1,p1c2,p2c1,p2c2):
    p1c1.rect

def menu():
    # title
    global name_1_entered, name_2_entered

    pygame.draw.rect(screen, white_ish, pygame.Rect(225, 45, 150, 50))
    pygame.draw.rect(screen, orange, pygame.Rect(225, 45, 150, 50), 3)
    screen.blit(text_surface, (250, 50))
    # enter_names


def game():
    screen.fill(blue)
    pygame.draw.rect(screen, orange, pygame.Rect(0, 0, 600, 600), 3)
    screen.blit(board, (115, 100))



running = True
while running:

    if menu_screen:
        menu()
    if game_screen:
        menu_screen = False
        game()

    if menu_screen:

        if Name1Button.draw():
            name_1_entered = True
            print('1st working')
            # player_1_name = input("Contestant 1, Enter your name... ")

        if Name2Button.draw():
            name_2_entered = True
            print('2nd working')
            # player_2_name = input("Contestant 2, Enter your name... ")

        if name_1_entered == True and name_2_entered == True:
            if Play_Button.draw():
                game_screen = True
                print("Let's Play")

    if game_screen:
        if D_ROLL.draw():
            #dice_roll()
            possible_choices = [d1, d2, d3, d4]
            dice_choose = random.randint(1, 4)
            print(dice_choose)
            chosen_dice = possible_choices[dice_choose - 1]
            screen.blit(chosen_dice, (0, 0))
            #chosen_d_button = Button(115, 500, chosen_dice)
            print("workwrk")




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
