import pygame

class Input:

    def __init__(self, screen, user_text=""):
        self.screen = screen
        self.user_text = user_text

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("Key pressed:", event.unicode)
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode

    def render_input(self):
        font = pygame.font.Font(None, 16)
        pygame.draw.rect(self.screen, pygame.Color("#001AFF"), [199, 0, 640 - (199 + 40), 40])
        pygame.draw.rect(self.screen, pygame.Color("#3549FF"), [200, 1, 640 - (199 + 42), 18])
        text_surface = font.render(self.user_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (205, 5))