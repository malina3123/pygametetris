import pygame
from colors import Colors


class Button:
    #инициализация
    def __init__(self, x, y, width, height, button_text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alreadyPressed = False
        self.buttonText = button_text

        self.inactive = Colors.black
        self.active = Colors.black
        self.pressed = Colors.black

        self.font = pygame.font.Font(None, 40)
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_text = self.font.render(self.buttonText, True, Colors.white)
        self.next_page = False
        self.pressed = False



    #активация функции кнопки
    def button_pressed(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, self.inactive, self.button_rect, 0, 10)
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.active, self.button_rect, 0, 10)
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                pygame.draw.rect(screen, self.pressed, self.button_rect, 0, 10)
                if not self.alreadyPressed:
                    self.next_page = True
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        #отрисовка кнопки и её центровка
        pygame.draw.rect(screen, self.active, self.button_rect, 3, 10)
        screen.blit(self.button_text,
                    self.button_text.get_rect(centerx=self.button_rect.centerx, centery=self.button_rect.centery))
