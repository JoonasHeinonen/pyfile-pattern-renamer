import pygame
import sys
from icon import Icon

class GUI:

    def __init__(self, folder_files=None, directory=None, font_size=36):
        self.folder_files = folder_files
        self.directory = directory
        self.font_size = font_size
        print("GUI initialized")

    def update_files_view(self, files, y_offset=45, window_surface=None):
        if window_surface is None:
            return

        font = pygame.font.Font(None, self.font_size)
        for file in files:
            list_item = font.render(file, True, pygame.Color("#FFFFFF"))
            window_surface.blit(list_item, (10, y_offset))
            y_offset += 30

    def draw_buttons(self, files, window_surface, mouse, window_size=(640, 480)):
        folder_icon = Icon("media/icon_folder.png")
        camel_case_icon = Icon("media/icon_camel_case.png")
        snake_case_icon = Icon("media/icon_snake_case.png")

        font = pygame.font.Font(None, self.font_size)
        small_font = pygame.font.Font(None, 16)

        text = font.render("Convert", True, pygame.Color("#FFFFFF"))
        directory_text = small_font.render(self.directory, True, pygame.Color("#FFFFFF"))

        # Normalize button.
        if 0 <= mouse[0] <= 120 and 0 <= mouse[1] <= 40:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [0, 0, 120, 40])
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [window_size[0] - 40, 0, 40, 40])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [0, 0, 120, 40])
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [window_size[0] - 40, 0, 40, 40])
        
        # Folder button.
        if window_size[0] - 40 <= mouse[0] <= window_size[0] and 0 <= mouse[1] <= 40:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [window_size[0] - 40, 0, 40, 40])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [window_size[0] - 40, 0, 40, 40])
        
        # Camel case button.
        if 120 <= mouse[0] <= 160 and 0 <= mouse[1] <= 40:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [120, 0, 40, 40])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [120, 0, 40, 40])
        
        # Snake case button.
        if 160 <= mouse[0] <= 200 and 0 <= mouse[1] <= 40:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [160, 0, 40, 40])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [160, 0, 40, 40])

        pygame.draw.rect(window_surface, pygame.Color("#001AFF"), [200, 0, window_size[0] - (200 + 40), 20], 1)
        pygame.draw.rect(window_surface, pygame.Color("#3549FF"), [201, 1, window_size[0] - (200 + 42), 18])

        # superimposing the text onto our button
        window_surface.blit(text, (10, 10))
        self.update_files_view(files, window_surface=window_surface)

        # Button icons superimposed on the buttons
        window_surface.blit(folder_icon.render_icon()[0], (window_size[0] - 40, 0))
        window_surface.blit(camel_case_icon.render_icon()[0], (120, 0))
        window_surface.blit(snake_case_icon.render_icon()[0], (160, 0))
        window_surface.blit(directory_text, (205, 5))

    def run(self):
        pygame.init()
        pygame.display.set_caption('File Name Normalizer')

        WINDOW_SIZE = (640, 480)
        window_surface = pygame.display.set_mode(WINDOW_SIZE)

        is_running = True

        files = self.folder_files if self.folder_files else []

        while is_running:
            window_surface.fill((0,0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # if mouse is hovered on a button it
            # changes to lighter shade 
            
            self.draw_buttons(files, window_surface, mouse, WINDOW_SIZE)

            # updates the frames of the game
            pygame.display.update()