import pygame
from files import Files

class Fileview:

    def __init__(self, directory):
        self.directory = directory
    
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