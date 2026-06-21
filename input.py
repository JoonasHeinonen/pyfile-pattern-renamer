import pygame

class Input:

    def __init__(self, screen, user_text = "", mode_text = ""):
        self.screen = screen
        self.user_text = user_text
        self.mode_text = mode_text

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode

    def render_input(self):
        font = pygame.font.Font(None, 16)
        pygame.draw.rect(self.screen, pygame.Color("#001AFF"), [199, 0, 640 - (199 + 40), 20])
        pygame.draw.rect(self.screen, pygame.Color("#001AFF"), [199, 20, 640 - (199 + 40), 20], 2)
        pygame.draw.rect(self.screen, pygame.Color("#3549FF"), [202, 3, 640 - (200 + 44), 16])
        text_surface = font.render(self.user_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (205, 5))