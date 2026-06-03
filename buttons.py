import pygame
from files import Files
from fileview import Fileview
from icon import Icon

class Buttons:

    modes = ["camel_case", "snake_case"]
    mode = ""

    def __init__(self, mouse, directory, window_surface=None,fileview=Fileview):
        self.mouse = mouse
        self.directory = directory
        self.window_surface = window_surface
        self.fileview = fileview

    def set_mode(self, mode):
        self.mode = mode
    
    def get_mode(self):
        return self.mode

    def button_clicks(self, mouse, window_size=(640, 480), window_surface=None):
        new_files = Files(self.directory)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Convert button.
                if 0 <= mouse[0] <= 119 and 0 <= mouse[1] <= 39:
                    new_files.convert_files(self.get_mode())
                    ## TODO todo
                    print("Convert button clicked")
                # Folder button.
                if window_size[0] - 40 <= mouse[0] <= window_size[0] and 0 <= mouse[1] <= 40:
                    self.fileview.update_files_view(self, window_surface=window_surface, mouse=mouse)
                    print("Folder button clicked")
                # Camel case button.
                if 120 <= mouse[0] <= 159 and 0 <= mouse[1] <= 39:
                    print("Camel case button clicked")
                    self.set_mode(self.modes[0])
                # Snake case button.
                if 160 <= mouse[0] <= 199 and 0 <= mouse[1] <= 39:
                    print("Snake case button clicked")
                    self.set_mode(self.modes[1])
                print("Conversion mode: ", self.mode)

    def draw_buttons(self, window_surface, mouse, window_size=(640, 480)):
        folder_icon = Icon("media/icon_folder.png")
        camel_case_icon = Icon("media/icon_camel_case.png")
        snake_case_icon = Icon("media/icon_snake_case.png")

        font = pygame.font.Font(None, 36)
        text = font.render("Convert", True, pygame.Color("#FFFFFF"))

        pygame.draw.rect(window_surface, pygame.Color("#222222"), [0, 0, window_size[0], 40])

        # Convert button.
        if 0 <= mouse[0] <= 119 and 0 <= mouse[1] <= 39:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [1, 1, 119, 38])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [1, 1, 119, 38])
        
        # Folder button.
        if window_size[0] - 40 <= mouse[0] <= window_size[0] and 0 <= mouse[1] <= 40:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [window_size[0] - 39, 1, 38, 38])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [window_size[0] - 39, 1, 38, 38])
        
        # Camel case button.
        if 120 <= mouse[0] <= 159 and 0 <= mouse[1] <= 39:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [121, 1, 38, 38])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [121, 1, 38, 38])
        
        # Snake case button.
        if 160 <= mouse[0] <= 199 and 0 <= mouse[1] <= 39:
            pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [160, 1, 38, 38])
        else:
            pygame.draw.rect(window_surface, pygame.Color("#424242"), [160, 1, 38, 38])

        # superimposing the text onto our button
        window_surface.blit(text, (10, 10))

        # File listing and view.
        self.fileview.update_files_view(
            self,
            window_surface=window_surface,
            mouse=mouse,
            window_size=window_size
        )

        # Button icons superimposed on the buttons
        window_surface.blit(folder_icon.render_icon()[0], (window_size[0] - 40, 0))
        window_surface.blit(camel_case_icon.render_icon()[0], (120, 0))
        window_surface.blit(snake_case_icon.render_icon()[0], (160, 0))