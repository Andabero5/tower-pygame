import pygame
import sys
from pygame.locals import *
from logic.game import *
from logic.Menu.HighScore import *
from logic.Menu.Instructions import *
from logic.singleton import *


# Initialize
pygame.init()
mainClock = pygame.time.Clock()

# measures of the window
WIDHT = 500
HEIGHT = 500

# Colors
WHITE = (0, 0, 0)
BLACK = (0, 0, 0)

# Set window
dimensions = [HEIGHT, WIDHT]
pygame.display.set_caption('TOWER BLOXX')
screen = pygame.display.set_mode((dimensions), pygame.NOFRAME)

# main font
font = pygame.font.SysFont('Courier', 20)

# Set Pics of the Background and buttons, and Scale them
image_background = pygame.image.load("Images/Menu/backgroundMenu.png")
image_button = pygame.image.load("Images/Menu/button.png")
image_button_back = pygame.image.load("Images/Menu/buttonBack.png")
background = pygame.transform.scale(image_background, (HEIGHT, WIDHT))

# Draw all the text on the window


def draw_text(surface, text, pos, font, color=BLACK):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Take a text and put it on a container


def draw_ButtonText(textG, image_container, rec_container, render_font, color):
    text = render_font.render(textG, 1, color)
    center = text.get_rect()
    x_diference = image_container.center[0] - center.center[0]
    y_diference = image_container.center[1] - center.center[1]
    screen.blit(text, [rec_container.left + x_diference,
                       rec_container.top + y_diference])


click = False  # Set the click on false (Use it with the Buttons)
origin = Singleton.get_instance()  # Get Instance to Singleton

# Draw the buttons


def drawButtons(button_list):
    for button in button_list:
        screen.blit(button['image'], button['rect'])
        draw_ButtonText(
            button['text'], button['image'].get_rect(), button['rect'], font, BLACK)

# Set the buttons used in the different sections of the menu


def setAlternButtons():

    button_1 = image_button.get_rect()
    button_2 = image_button.get_rect()
    button_3 = image_button_back.get_rect()

    buttons = []
    button_1.topleft = [150, 360]  # Coords where the button will be
    buttons.append({'text': "Nuevo Juego", 'image': image_button,
                    'rect': button_1, 'on_click': False})
    button_2.topleft = [150, 430]
    buttons.append({'text': "Salir", 'image': image_button,
                    'rect': button_2, 'on_click': False})
    button_3.topleft = [20, 430]
    buttons.append({'text': "", 'image': image_button_back,
                    'rect': button_3, 'on_click': False})
    return buttons


def main_menu():
    screen.blit(background, [0, 0])

    while True:

        button_1 = image_button.get_rect()
        button_2 = image_button.get_rect()
        button_3 = image_button.get_rect()
        button_4 = image_button.get_rect()

        buttons = []
        button_1.topleft = [150, 220]
        buttons.append({'text': "Nuevo Juego", 'image': image_button,
                        'rect': button_1, 'on_click': False})
        button_2.topleft = [150, 290]
        buttons.append({'text': "Puntajes Altos", 'image': image_button,
                        'rect': button_2, 'on_click': False})
        button_3.topleft = [150, 360]
        buttons.append({'text': "Instrucciones", 'image': image_button,
                        'rect': button_3, 'on_click': False})
        button_4.topleft = [150, 430]
        buttons.append({'text': "Salir", 'image': image_button,
                        'rect': button_4, 'on_click': False})

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for button in buttons:
                    # Compare between the mouse pos and buttons pos
                    button['on_click'] = button['rect'].colliderect(
                        [mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for button in buttons:
                    # Compare between the click pos and buttons pos
                    button['on_click'] = False

        if buttons[0]['on_click'] and click:
            game()
            click = False
        if buttons[1]['on_click'] and click:
            highScore()
            click = False
        if buttons[2]['on_click'] and click:
            instructions()
            click = False
        if buttons[3]['on_click'] and click:
            exit()
            click = False

        drawButtons(buttons)
        pygame.display.update()
        mainClock.tick(60)


def game():
    pygame.quit()
    main()


def highScore():

    screen.blit(background, [0, 0])

    font = pygame.font.SysFont('Arial', 24)
    draw_text(screen, "HIGH SCORE", (50, 150), font)
    origin.set_valueScore(organizeNumbers())
    draw_text(screen, numsToString(origin.get_valueScore()),
              (400, 200), font)  # Draw the scores
    origin.set_valueNames(organizeNames())
    draw_text(screen, namesToString(origin.get_valueNames()),
              (100, 200), font)  # Draw the names
    buttons = []
    buttons = setAlternButtons()

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for button in buttons:
                    button['on_click'] = button['rect'].colliderect(
                        [mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for button in buttons:
                    button['on_click'] = False

        if buttons[0]['on_click'] and click:
            game()
            click = False
        if buttons[1]['on_click'] and click:
            exit()
            click = False
        if buttons[2]['on_click'] and click:
            main_menu()
            click = False

        drawButtons(buttons)
        pygame.display.update()
        mainClock.tick(60)


def instructions():

    screen.blit(background, [0, 0])

    instructions = setInstructions()  # Take the values of the function's list
    house = setHouses()  # Take the values of the function's list
    font = pygame.font.SysFont('Arial', 24)
    draw_text(screen, "INSTRUCCIONES", (50, 150), font)
    draw_text(screen, instructions[0], (20, 180), font)
    for i in range(4):
        # Draw the text of the types of house
        draw_text(screen, instructions[i+1], [(20+(130*i)), 270], font)
        # Draw the images of the types of house
        screen.blit(house[i], [(20+(120*i)), 300])

    buttons = []
    buttons = setAlternButtons()
    while True:

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for button in buttons:
                    button['on_click'] = button['rect'].colliderect(
                        [mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for button in buttons:
                    button['on_click'] = False

        if buttons[0]['on_click'] and click:
            game()
            click = False
        if buttons[1]['on_click'] and click:
            exit()
            click = False
        if buttons[2]['on_click'] and click:
            main_menu()
            click = False

        drawButtons(buttons)
        pygame.display.update()
        mainClock.tick(60)


def exit():
    pygame.quit()  # close the window
    sys.exit()  # close the process


if __name__ == "__main__":
    main_menu()
