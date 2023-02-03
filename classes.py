import pygame


class Button:
    def __init__(self, pos_x, pos_y, size_x, size_y, color, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sx = size_x
        self.sy = size_y
        self.color = color
        self.w = width

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (
            self.pos_x, self.pos_y, self.sx, self.sy), self.w)