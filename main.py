import pygame
import sys
import webbrowser
import random

# Game window settings
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
H = 10
W = 10
FPS = 2

# Game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Game:

    def __init__(self):
        self.white = WHITE
        self.black = BLACK
        self.red = RED
        self.blue = BLUE
        self.point = 0
        self.colors = [self.red, self.blue]
        self.dir = 'right'
        self.snake = [[0, 0]]
        self.head_snake = [0, 0]

    def render(self, screen, board, map_list):
        board.render(screen, map_list)
        self.show_points()

    def show_points(self):
        pygame.draw.rect(screen, self.red, (5, 5, 100, 50), 5)
        font = pygame.font.Font(None, 60)
        text = font.render(str(self.point), True, (255, 0, 0))
        screen.blit(text, (15, 15))

    def try_spread(self):
        if self.dir == 'up':
            if self.head_snake[0] < 0:
                return False
            if not map_list[self.head_snake[0]][self.head_snake[1]] and map_list[self.head_snake[0]][
                self.head_snake[1]] != 2:
                return False
            return True
        if self.dir == 'left':
            if self.head_snake[1] < 0:
                return False
            if not map_list[self.head_snake[0]][self.head_snake[1]] and map_list[self.head_snake[0]][
                self.head_snake[1]] != 2:
                return False
            return True
        if self.dir == 'right':
            if self.head_snake[1] + 1 > 10:
                return False
            if not map_list[self.head_snake[0]][self.head_snake[1]] and map_list[self.head_snake[0]][
                self.head_snake[1]] != 2:
                return False
            return True
        if self.dir == 'down':
            if self.head_snake[0] + 1 > 10:
                return False
            if not map_list[self.head_snake[0]][self.head_snake[1]] and map_list[self.head_snake[0]][
                self.head_snake[1]] != 2:
                return False
            return True

    def apple_pick(self):
        if self.dir == 'up':
            if map_list[self.head_snake[0] + 1][self.head_snake[1]] == 2:
                self.point += 1
                map_list[self.head_snake[0] + 1][self.head_snake[1]] = 0
                return False
            return True
        if self.dir == 'left':
            if map_list[self.head_snake[0]][self.head_snake[1] + 1] == 2:
                self.point += 1
                map_list[self.head_snake[0]][self.head_snake[1] + 1] = 0
                return False
            return True
        if self.dir == 'right':
            if map_list[self.head_snake[0]][self.head_snake[1] - 1] == 2:
                self.point += 1
                map_list[self.head_snake[0]][self.head_snake[1] - 1] = 0
                return False
            return True
        if self.dir == 'down':
            if map_list[self.head_snake[0] - 1][self.head_snake[1]] == 2:
                self.point += 1
                map_list[self.head_snake[0] - 1][self.head_snake[1]] = 0
                return False
            return True

    def next_move(self):
        if not self.try_spread():
            print('Пробный период игры окончен, для полной версии переведите на этот счет: ******** 5000 рублей')
            print('Для дальнейшей игры перезапустите приложение')
            pygame.quit()
            sys.exit()
        self.add_apple()
        flag2 = True
        if self.dir == 'up':
            self.head_snake[0] -= 1
        if self.dir == 'left':
            self.head_snake[1] -= 1
        if self.dir == 'right':
            self.head_snake[1] += 1
        if self.dir == 'down':
            self.head_snake[0] += 1
        if self.apple_pick():
            self.snake.pop(0)
        self.snake.append(self.head_snake[::])
        # self.snake.append(self.head_snake)

    def add_apple(self):
        for i in map_list:
            for j in i:
                if j == 2:
                    return True
        a, b = random.randrange(len(map_list)), random.randrange(len(map_list))
        while [a, b] in self.snake:
            a, b = random.randrange(len(map_list)), random.randrange(len(map_list))
        map_list[random.randrange(len(map_list))][random.randrange(len(map_list))] = 2


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, map_list):
        for i in range(self.height):
            for j in range(self.width):
                if map_list[i][j] == 2:
                    pygame.draw.rect(screen, BLUE, (
                        self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size, self.cell_size),
                                     0,
                                     3)
                if [i, j] in game.snake:
                    pygame.draw.rect(screen, RED,
                                     (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, WHITE,
                                     (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size), 1)


class Main_win:

    def __init__(self):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.btn_play = (170, 250, 150, 50)
        self.btn_exp = (115, 350, 275, 50)
        self.active_menu = 'start'
        self.url = 'https://www.youtube.com/watch?v=ptw2FLKXDQE'

    def start_menu(self, screen):
        font = pygame.font.Font(None, 60)
        text = font.render('Играть', True, (255, 0, 0))
        screen.blit(text, (175, 255))
        font = pygame.font.Font(None, 60)
        text = font.render('Достижения', True, (255, 0, 0))
        screen.blit(text, (120, 355))

    def play_menu(self, screen, board, game, map_list):
        game.render(screen, board, map_list)

    def click(self, click_coord):
        global flag
        if self.active_menu == 'start':
            if click_coord[0] > self.btn_exp[0] \
                    and click_coord[0] < self.btn_exp[0] + self.btn_exp[2] \
                    and click_coord[1] > self.btn_exp[1] \
                    and click_coord[1] < self.btn_exp[1] + self.btn_exp[3]:
                webbrowser.open(self.url)
            if click_coord[0] > self.btn_play[0] \
                    and click_coord[0] < self.btn_play[0] + self.btn_play[2] \
                    and click_coord[1] > self.btn_play[1] \
                    and click_coord[1] < self.btn_play[1] + self.btn_play[3]:
                self.active_menu = 'play'
                flag = True

    def show_screen(self, screen, board, game, map_list):
        if self.active_menu == 'start':
            self.start_menu(screen)
        elif self.active_menu == 'play':
            self.play_menu(screen, board, game, map_list)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Змейка')
    a = Main_win()
    game = Game()
    board = Board(H, W)
    board.set_view(60, 60, 40)
    map_list = list()
    for i in range(H):
        map_list.append(list())
        for j in range(W):
            map_list[i].append(1)
    background = pygame.image.load('data/background.jpg')
    clock = pygame.time.Clock()
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    a.click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    game.dir = 'down'
                if event.key == pygame.K_LEFT:
                    game.dir = 'left'
                if event.key == pygame.K_RIGHT:
                    game.dir = 'right'
                if event.key == pygame.K_UP:
                    game.dir = 'up'
        screen.blit(background, (0, 0))
        a.show_screen(screen, board, game, map_list)
        if flag:
            game.add_apple()
            game.next_move()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)
