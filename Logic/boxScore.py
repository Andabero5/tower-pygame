"""
Copyright 2017, Silas Gyger, silasgyger@gmail.com, All rights reserved.
Borrowed from https://github.com/Nearoo/pygame-text-input under the MIT license.
"""

import os.path
import pygame.locals as pl
import pygame, sys
from pygame.locals import *
from Menu.HighScore import *
from singleton import *


#Initialize
pygame.init()
mainClock = pygame.time.Clock()

#measures of the window
WIDHT = 500
HEIGHT = 300

#Colors
WHITE = (0,0,0)
BLACK = (0,0,0)

#Set window
dimensions = [WIDHT,HEIGHT]
pygame.display.set_caption('TOWER BLOXX')
screen = pygame.display.set_mode((dimensions),pygame.NOFRAME)

#main font 
font = pygame.font.SysFont('Courier', 20)

#Set Pics of the Background and buttons, and Scale them
image_background = pygame.image.load("Images/Menu/backgroundMenu.png")
image_button = pygame.image.load("Images/Menu/button.png")
whiteRectangle = pygame.image.load("Images/Menu/whiteRectangle.png")
background = pygame.transform.scale(image_background, (WIDHT,HEIGHT))
textBox = pygame.transform.scale(whiteRectangle, (270,40))


#Draw all the text on the window
def draw_text(surface, text, pos, font, color=BLACK):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
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


#Take a text and put it on a container
def draw_ButtonText(textG, image_container, rec_container, render_font, color):
    text = render_font.render(textG, 1, color)
    center = text.get_rect()
    x_diference = image_container.center[0] - center.center[0]
    y_diference = image_container.center[1] - center.center[1]
    screen.blit(text, [rec_container.left + x_diference, rec_container.top + y_diference])


click = False #Set the click on false (Use it with the Buttons)

#Draw the buttons
def drawButtons(button_list):
    for button in button_list:
        screen.blit(button['image'], button['rect'])
        draw_ButtonText(button['text'], button['image'].get_rect(), button['rect'], font, BLACK)


class TextInput:
    
    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=35,
            antialias=True,
            text_color=BLACK,
            cursor_color=(0, 0, 1),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35,
            max_string_length=16):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when held
        :param max_string_length: Allowed length of text
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.max_string_length = max_string_length
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size / 20 + 1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif len(self.input_string) < self.max_string_length or self.max_string_length == -1:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False
    
    
    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0



def main():

    final = Singleton.get_instance()
    screen.blit(background, [0, 0])
    draw_text(screen,"INGRESE SU NOMBRE", (20, 100), font)

    # Create TextInput-object
    textinput = TextInput()

    while True:
        postButton = image_button.get_rect()
        
        buttons = []
        postButton.topleft = [150, 220]
        buttons.append({'text': "Enviar", 'image': image_button, 'rect': postButton, 'on_click': False})
        events = pygame.event.get()
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for button in buttons:
                    button['on_click'] = button['rect'].colliderect([mouse[0], mouse[1], 1, 1]) #Compare between the mouse pos and buttons pos 
                click = True
            if event.type == MOUSEBUTTONUP:
                for button in buttons:
                    button['on_click'] = False #Compare between the click pos and buttons pos 
            if event.type == pygame.QUIT:
                exit()

        if buttons[0]['on_click'] and click:

            numGotten=0
            saveScore(numGotten)
            saveName(textinput.get_text())
            final.set_valueScore(organizeNumbers())
            final.set_valueNames(organizeNames())

            exit()
            click = False
        
        drawButtons(buttons)
        screen.blit(textBox,[60,130])
        
        # Feed it with events every frame
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.get_surface(), (65, 140))

        pygame.display.update()
        mainClock.tick(30)