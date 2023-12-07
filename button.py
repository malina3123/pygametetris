import pygame
from colors import Colors

class Button:
    def __init__(self, x, y, width, height, button_text, change_mode):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alreadyPressed = False
        self.buttonText = button_text

        self.inactive = Colors.silver
        self.active = Colors.grey
        self.pressed = Colors.white

        self.font = pygame.font.Font(None, 40)
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_text = self.font.render(self.buttonText, True, Colors.black)
        self.next_page = False
