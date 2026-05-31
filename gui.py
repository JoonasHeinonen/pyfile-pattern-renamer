import pygame
import sys
from icon import Icon

pygame.init()
pygame.display.set_caption('File Name Normalizer')

WINDOW_SIZE = (640, 480)

window_surface = pygame.display.set_mode(WINDOW_SIZE)

is_running = True

files = ["example file.txt", "another_file.doc", "file with spaces.pdf"]
files_txt = ", ".join(files)
font_size = 36

folder_icon = Icon("media/icon_folder.png")
font = pygame.font.Font(None, font_size)

while is_running:
    window_surface.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    text = font.render("Normalize files", True, pygame.Color("#FFFFFF"))
    list = font.render(files_txt, True, pygame.Color("#FFFFFF"))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade 
    
    # Normalize button.
    if 0 <= mouse[0] <= 200 and 0 <= mouse[1] <= 40:
        pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [0, 0, 200, 40])
        pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [WINDOW_SIZE[0] - 40, 0, 40, 40])
    else:
        pygame.draw.rect(window_surface, pygame.Color("#424242"), [0, 0, 200, 40])
        pygame.draw.rect(window_surface, pygame.Color("#424242"), [WINDOW_SIZE[0] - 40, 0, 40, 40])
    
    # Folder button.
    if WINDOW_SIZE[0] - 40 <= mouse[0] <= WINDOW_SIZE[0] and 0 <= mouse[1] <= 40:
        pygame.draw.rect(window_surface, pygame.Color("#CCCCCC"), [WINDOW_SIZE[0] - 40, 0, 40, 40])
    else:
        pygame.draw.rect(window_surface, pygame.Color("#424242"), [WINDOW_SIZE[0] - 40, 0, 40, 40])


    pygame.draw.rect(window_surface, pygame.Color("#001AFF"), [200, 0, WINDOW_SIZE[0] - (200 + 40), 40], 1)
    pygame.draw.rect(window_surface, pygame.Color("#3549FF"), [201, 1, WINDOW_SIZE[0] - (200 + 42), 38])

    # superimposing the text onto our button
    window_surface.blit(text, (10, 10))
    y_offset = 45
    for file in files:
        list_item = font.render(file, True, pygame.Color("#FFFFFF"))
        window_surface.blit(list_item, (10, y_offset))
        y_offset += 30
    window_surface.blit(folder_icon.render_icon()[0], (WINDOW_SIZE[0] - 40, 0))

    # updates the frames of the game
    pygame.display.update()