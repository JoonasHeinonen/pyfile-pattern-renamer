import pygame
from files import Files
from fileview import Fileview
from icon import Icon
import os
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

class Buttons:

    modes = ["camel_case", "snake_case"]
    mode = ""
    mode_text = "Welcome to Pyfile Pattern Renamer! Please select a mode."

    def __init__(self, mouse, directory, window_surface=None, fileview=None):
        self.mouse = mouse
        self.directory = directory
        self.window_surface = window_surface
        self.fileview = fileview or Fileview(directory, dotenv_file)

    def set_mode(self, mode):
        self.mode = mode
    
    def get_mode(self):
        return self.mode
    
    def update_folder(self, key=""):
        folder_value = getattr(self, "directory", None) or os.environ.get(key, "")
        try:
            dotenv.set_key(dotenv_file, "FOLDER", folder_value)
        except PermissionError:
            print("Cannot write .env: permission denied")
            os.environ[key] = folder_value
        # keep Fileview in sync with the current directory
        if getattr(self, 'fileview', None) is not None:
            try:
                self.fileview.directory = folder_value
            except Exception:
                pass

    def button_clicks(self, mouse, window_size=(640, 480), window_surface=None, events=None):
        new_files = Files(self.directory)
        if events is None:
            events = []

        for ev in events:
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Check if back button was clicked
                if self.fileview.hover_over_back_btn:
                    parent_dir = self.fileview.trim_after_last_slash(self.fileview.directory)
                    self.directory = parent_dir
                    self.fileview.directory = parent_dir
                    self.update_folder("FOLDER")
                    self.mode_text = f"Back to: {parent_dir}"
                    continue

                # Check if a file/folder row was clicked in the Fileview
                clicked = None
                try:
                    clicked = self.fileview.get_item_at(mouse, window_size=window_size)
                except Exception:
                    clicked = None
                if clicked:
                    typ, name = clicked
                    if typ == "folder":
                        new_dir = os.path.join(self.fileview.directory, name)
                        # update both Buttons and Fileview
                        self.directory = new_dir
                        self.fileview.directory = new_dir
                        # persist the selected folder
                        self.update_folder("FOLDER")
                        self.mode_text = f"Entered folder: {name}"
                        continue
                    elif typ == "file":
                        new_files.rename_file(self.directory, self.get_mode(), name)
                        continue
                # Convert button.
                if 0 <= mouse[0] <= 119 and 0 <= mouse[1] <= 39:
                    new_files.convert_files(self.get_mode())
                    if self.get_mode() == "":
                        self.mode_text = "Please select mode first!"
                    else:
                        self.mode_text = f"Conversion mode: {self.get_mode()}"
                # Folder button.
                if window_size[0] - 40 <= mouse[0] <= window_size[0] and 0 <= mouse[1] <= 40:
                    self.fileview.update_files_view(window_surface=window_surface, mouse=mouse, window_size=window_size)
                    self.mode_text = "Updated the file view."
                    self.update_folder("FOLDER")
                # Allow Fileview to handle scroll button clicks on any mouse down
                self.fileview.click_scroll_buttons(mouse, window_size=window_size)
                # Camel case button.
                if 120 <= mouse[0] <= 159 and 0 <= mouse[1] <= 39:
                    self.set_mode(self.modes[0])
                    self.mode_text = f"Camel case conversion selected!"
                # Snake case button.
                if 160 <= mouse[0] <= 199 and 0 <= mouse[1] <= 39:
                    self.set_mode(self.modes[1])
                    self.mode_text = f"Snake case conversion selected!"

    def draw_buttons(self, window_surface, mouse, window_size=(640, 480)):
        folder_icon = Icon("media/icon_folder.png")
        camel_case_icon = Icon("media/icon_camel_case.png")
        snake_case_icon = Icon("media/icon_snake_case.png")

        font = pygame.font.Font(None, 36)
        text = font.render("Convert", True, pygame.Color("#FFFFFF"))

        # File listing and view.
        self.fileview.update_files_view(
            window_surface=window_surface,
            mouse=mouse,
            window_size=window_size
        )

        pygame.draw.rect(window_surface, pygame.Color("#222222"), [0, 0, 199, 40])
        pygame.draw.rect(window_surface, pygame.Color("#222222"), [window_size[0] - 40, 0, 40, 40])

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

        pygame.draw.rect(window_surface, pygame.Color("#000000"), [200, 0, 400, 40])
        mode_text_surface = pygame.font.Font(None, 16).render(self.mode_text, True, (0, 255, 0))
        window_surface.blit(mode_text_surface, (205, 25))

        # Button icons superimposed on the buttons
        window_surface.blit(folder_icon.render_icon()[0], (window_size[0] - 40, 0))
        window_surface.blit(camel_case_icon.render_icon()[0], (120, 0))
        window_surface.blit(snake_case_icon.render_icon()[0], (158, 0))