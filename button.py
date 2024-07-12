import pygame

class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        self.screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def center(self, width, height):
        self.rect.center = (width // 2, height // 2 + 100)
