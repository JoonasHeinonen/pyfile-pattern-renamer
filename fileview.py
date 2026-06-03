import pygame
from files import Files
from icon import Icon

class Fileview:

    def __init__(self, directory):
        self.directory = directory

    def click_scroll_buttons(self, mouse):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                print("Mouse clicked at: ", mouse)

    def update_files_view(self, y_offset=45, mouse=None, window_surface=None, window_size=(640, 480)):
        new_files = Files(self.directory).list_directory_files(self.directory)

        scroll_button_up = Icon("media/scroll_button_up.png")
        scroll_button_up_pressed = Icon("media/scroll_button_up_pressed.png")
        scroll_button_down = Icon("media/scroll_button_down.png")
        scroll_button_down_pressed = Icon("media/scroll_button_down_pressed.png")

        if window_surface is None:
            return

        # Scrollbar.
        pygame.draw.rect(window_surface, pygame.Color("#222222"), [640 - 14, 40, 13, 480 - 40])

        # Scroll up.
        if window_size[0] - 15 <= mouse[0] <= window_size[0] and 0 <= mouse[1] >= 40  and 0 <= mouse[1] <= 55:
            window_surface.blit(scroll_button_up_pressed.render_icon()[0], (640 - 15, 40))
        else:
            window_surface.blit(scroll_button_up.render_icon()[0], (640 - 15, 40))

        # Scroll down.
        if window_size[0] - 15 <= mouse[0] <= window_size[0] and 0 <= mouse[1] >= window_size[1] - 15:
            window_surface.blit(scroll_button_down_pressed.render_icon()[0], (640 - 15, 480 - 15))
        else:
            window_surface.blit(scroll_button_down.render_icon()[0], (640 - 15, 480 - 15))

        index = 0

        for file in new_files:
            list_item = pygame.font.Font(None, 16).render(file, True, pygame.Color("#FFFFFF"))
            colors = ["#162D92", "#0F1066"]

            if index % 2 == 0:
                pygame.draw.rect(window_surface, pygame.Color(colors[0]), [0, y_offset - 4, 640 - 15, 20])
            else:
                pygame.draw.rect(window_surface, pygame.Color(colors[1]), [0, y_offset - 4, 640 - 15, 20])
            index += 1
            window_surface.blit(list_item, (5, y_offset))
            y_offset += 21