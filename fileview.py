import pygame
from files import Files
from icon import Icon

class Fileview:

    def __init__(self, directory):
        self.directory = directory
        self.scroll_index = 0

    def click_scroll_buttons(self, mouse, window_size=(640, 480)):
        if mouse is None:
            return

        # Compute how many items and how many fit to determine bounds
        new_folders = Files(self.directory).list_directory(self.directory, True)
        new_files = Files(self.directory).list_directory(self.directory, False)
        total_items = len(new_folders) + len(new_files)
        visible_lines = max(1, (window_size[1] - 40) // 21)
        max_scroll = max(0, total_items - visible_lines)

        x, y = mouse
        # Up button area
        if window_size[0] - 15 <= x <= window_size[0] and 40 <= y <= 55:
            self.scroll_index = max(0, self.scroll_index - 1)
        # Down button area
        if window_size[0] - 15 <= x <= window_size[0] and window_size[1] - 15 <= y <= window_size[1]:
            self.scroll_index = min(max_scroll, self.scroll_index + 1)

    def update_files_view(self, y_offset=45, mouse=None, window_surface=None, window_size=(640, 480)):
        new_folders = Files(self.directory).list_directory(self.directory, True)
        new_files = Files(self.directory).list_directory(self.directory, False)

        scroll_button_up = Icon("media/scroll_button_up.png")
        scroll_button_up_pressed = Icon("media/scroll_button_up_pressed.png")
        scroll_button_down = Icon("media/scroll_button_down.png")
        scroll_button_down_pressed = Icon("media/scroll_button_down_pressed.png")

        if window_surface is None:
            return

        # Scrollbar.
        pygame.draw.rect(window_surface, pygame.Color("#222222"), [window_size[0] - 14, 40, 13, window_size[1] - 40])

        # Scroll up (hover)
        if mouse and (window_size[0] - 15 <= mouse[0] <= window_size[0] and 40 <= mouse[1] <= 55):
            window_surface.blit(scroll_button_up_pressed.render_icon()[0], (window_size[0] - 15, 40))
        else:
            window_surface.blit(scroll_button_up.render_icon()[0], (window_size[0] - 15, 40))

        # Scroll down (hover)
        if mouse and (window_size[0] - 15 <= mouse[0] <= window_size[0] and window_size[1] - 15 <= mouse[1] <= window_size[1]):
            window_surface.blit(scroll_button_down_pressed.render_icon()[0], (window_size[0] - 15, window_size[1] - 15))
        else:
            window_surface.blit(scroll_button_down.render_icon()[0], (window_size[0] - 15, window_size[1] - 15))

        # Click on scroll up.

        # Click on scroll down.

        index = 0

        # apply scroll offset to starting y position
        y_offset = y_offset - (self.scroll_index * 21)

        for folder in new_folders:
            icon_fileview_folder = Icon("media/icon_fileview_folder.png")
            list_item = pygame.font.Font(None, 16).render(folder + "/", True, pygame.Color("#FFFFFF"))
            colors = ["#927B16", "#63530D"]

            if index % 2 == 0:
                pygame.draw.rect(window_surface, pygame.Color(colors[0]), [1, y_offset - 4, window_size[0] - 16, 20])
            else:
                pygame.draw.rect(window_surface, pygame.Color(colors[1]), [1, y_offset - 4, window_size[0] - 16, 20])
            index += 1
            window_surface.blit(list_item, (25, y_offset))
            window_surface.blit(icon_fileview_folder.render_icon()[0], (0, y_offset - 4))
            y_offset += 21

        for file in new_files:
            icon_fileview_file = Icon("media/icon_fileview_file.png")
            list_item = pygame.font.Font(None, 16).render(file, True, pygame.Color("#FFFFFF"))
            colors = ["#162D92", "#0F1066"]

            if index % 2 == 0:
                pygame.draw.rect(window_surface, pygame.Color(colors[0]), [1, y_offset - 4, window_size[0] - 16, 20])
            else:
                pygame.draw.rect(window_surface, pygame.Color(colors[1]), [1, y_offset - 4, window_size[0] - 16, 20])
            index += 1
            window_surface.blit(list_item, (25, y_offset))
            window_surface.blit(icon_fileview_file.render_icon()[0], (0, y_offset - 4))
            y_offset += 21