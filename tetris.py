import sys
import pygame
import time
from game import Game
from colors import Colors
from button import Button

#инициализация pygame
pygame.init()

# текстовые элементы и фигуры
title_font = pygame.font.Font(None, 40)
records_font = pygame.font.Font(None, 25)
score_surface = title_font.render("Score", True, Colors.black)
next_surface = title_font.render("Next", True, Colors.black)
game_over_surface = title_font.render("GAME OVER", True, Colors.black)
score_rect = pygame.Rect(320, 45, 170, 50)
record_rect = pygame.Rect(320, 100, 170, 210)
next_rect = pygame.Rect(320, 345, 170, 180)

# создание экрана игры
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# таймер
clock = pygame.time.Clock()

# вызов основного класса Game
game = Game()

#событие для рассчёта сложности
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 100)

#сложность и пауза
pause = True
difficulty = 0

#отрисовка кнопок в главном меню
button=Button(100,100,300,150,"Начать игру")
escbutton=Button(100,300,300,150,"Выход из игры")

#игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    button.button_pressed(screen)
    escbutton.button_pressed(screen)

    if escbutton.next_page:
        pygame.quit()
        sys.exit()



    pygame.display.update()
    clock.tick()

    while button.next_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pause = False
                if game.game_over:
                    game.game_over = False
                    game.reset()
                    pause = True
                if event.key == pygame.K_LEFT and not game.game_over and not pause:
                    game.move_left()
                if event.key == pygame.K_RIGHT and not game.game_over and not pause:
                    game.move_right()
                if event.key == pygame.K_DOWN and not game.game_over and not pause:
                    game.move_down()
                if event.key == pygame.K_UP and not game.game_over and not pause:
                    game.rotate()
                if event.key == pygame.K_SPACE:
                    game.reset()


            if event.type == GAME_UPDATE and not game.game_over and not pause:
                game.move_down()
                if difficulty < 125:
                    difficulty += 0.1
                    pygame.time.set_timer(GAME_UPDATE, 200-round(difficulty))



        #заливка поля
        screen.fill(Colors.dark_orange)
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.blit(score_surface, (365, 15, 50, 50))
        pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
        pygame.draw.rect(screen, Colors.gold, score_rect, 5, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                      centery=score_rect.centery))
        #отображение текущего количества очков
        pygame.draw.rect(screen, Colors.black, record_rect, 0, 10)
        pygame.draw.rect(screen, Colors.gold, record_rect, 5, 10)
        game.records.print_records(screen, records_font)

        #прошлые рекорды
        screen.blit(next_surface, (375, 315, 50, 50))
        pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
        pygame.draw.rect(screen, Colors.gold, next_rect, 5, 10)

        game.draw_blocks(screen)

        #конец игры
        if game.game_over:
            screen.blit(game_over_surface, (320, 550, 50, 50))

        pygame.display.update()
        clock.tick(60)