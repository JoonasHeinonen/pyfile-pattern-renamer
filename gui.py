from tkinter import font

import pygame
from input import Input
from buttons import Buttons

clock = pygame.time.Clock()

class GUI:

    def __init__(self, directory=None, font_size=36, text=""):
        self.directory = directory
        self.font_size = font_size
        self.text = text

    def run(self):
        pygame.init()
        pygame.display.set_caption('File Name Normalizer')

        WINDOW_SIZE = (640, 480)
        window_surface = pygame.display.set_mode(WINDOW_SIZE)

        # Create buttons instance once, before the loop, so mode persists
        buttons = Buttons((0, 0), self.directory)

        is_running = True

        while is_running:
            window_surface.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    print("Key pressed:", event.unicode)
                    if event.key == pygame.K_BACKSPACE:
                        self.directory = self.directory[:-1]
                    else:
                        self.directory += event.unicode
                        print("Directory: ", self.directory)

            # Mouse.
            mouse = pygame.mouse.get_pos()
            buttons.mouse = mouse
            buttons.directory = self.directory
            
            # Folder text field & features.
            input = Input(window_surface, self.directory)
            input.handle_events()
            input.render_input()

            # Buttons.
            buttons.draw_buttons(window_surface, mouse, window_size=WINDOW_SIZE)
            buttons.button_clicks(mouse, window_size=WINDOW_SIZE, window_surface=window_surface)

            # updates the frames of the game
            pygame.display.flip()
            clock.tick(60)