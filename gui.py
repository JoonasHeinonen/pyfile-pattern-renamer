import pygame
from icon import Icon
from files import Files
clock = pygame.time.Clock()

class GUI:

    def __init__(self, folder_files=None, directory=None, font_size=36, text=""):
        self.folder_files = folder_files
        self.directory = directory
        self.font_size = font_size
        self.text = text
        print("GUI initialized")

    def update_files_view(self, y_offset=45, window_surface=None):
        new_files = Files(self.directory).list_directory_files(self.directory)
        if window_surface is None:
            return

        font = pygame.font.Font(None, 25)
        index = 0
        for file in new_files:
            list_item = font.render(file, True, pygame.Color("#FFFFFF"))
            colors = ["#21DD50", "#169235"]

            if index % 2 == 0:
                pygame.draw.rect(window_surface, pygame.Color(colors[0]), [0, y_offset - 4, 640, 29])
            else:
                pygame.draw.rect(window_surface, pygame.Color(colors[1]), [0, y_offset - 4, 640, 29])
            index += 1
            window_surface.blit(list_item, (10, y_offset))
            y_offset += 30

    def button_clicks(self, mouse, window_size=(640, 480), window_surface=None):
        new_files = Files(self.directory)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Convert button.
                if 0 <= mouse[0] <= 119 and 0 <= mouse[1] <= 39:
                    new_files.convert_files()
                    print("Convert button clicked")
                # Folder button.
                if window_size[0] - 40 <= mouse[0] <= window_size[0] and 0 <= mouse[1] <= 40:
                    self.update_files_view(window_surface=window_surface)
                    print("Folder button clicked")
                # Camel case button.
                if 120 <= mouse[0] <= 159 and 0 <= mouse[1] <= 39:
                    print("Camel case button clicked")
                # Snake case button.
                if 160 <= mouse[0] <= 199 and 0 <= mouse[1] <= 39:
                    print("Snake case button clicked")

    def draw_buttons(self, window_surface, mouse, window_size=(640, 480)):
        folder_icon = Icon("media/icon_folder.png")
        camel_case_icon = Icon("media/icon_camel_case.png")
        snake_case_icon = Icon("media/icon_snake_case.png")

        font = pygame.font.Font(None, self.font_size)
        small_font = pygame.font.Font(None, 16)

        text = font.render("Convert", True, pygame.Color("#FFFFFF"))
        directory_text = small_font.render(self.directory, True, pygame.Color("#FFFFFF"))

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

        # Folder text field.
        pygame.draw.rect(window_surface, pygame.Color("#001AFF"), [199, 0, window_size[0] - (199 + 40), 40])
        pygame.draw.rect(window_surface, pygame.Color("#3549FF"), [200, 1, window_size[0] - (199 + 42), 18])

        # superimposing the text onto our button
        window_surface.blit(text, (10, 10))
        self.update_files_view(window_surface=window_surface)

        # Button icons superimposed on the buttons
        window_surface.blit(folder_icon.render_icon()[0], (window_size[0] - 40, 0))
        window_surface.blit(camel_case_icon.render_icon()[0], (120, 0))
        window_surface.blit(snake_case_icon.render_icon()[0], (160, 0))
        window_surface.blit(directory_text, (205, 5))

        self.button_clicks(mouse, window_size=window_size, window_surface=window_surface)

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
                if event.type == pygame.KEYDOWN:
                    print("Key pressed:", event.unicode)
                    if event.key == pygame.K_BACKSPACE:
                        self.directory = self.directory[:-1]
                    else:
                        self.directory += event.unicode
                        print("Directory: ", self.directory)

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()
            
            self.draw_buttons(window_surface, mouse, WINDOW_SIZE)

            input_box = pygame.Rect(10, 200, 620, 100)
            pygame.draw.rect(window_surface, (255, 255, 255), input_box, 2)
            font = pygame.font.Font(None, 12)
            text_surface = font.render(self.directory, True, (255, 255, 255))
            window_surface.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            # updates the frames of the game
            pygame.display.flip()
            clock.tick(60)