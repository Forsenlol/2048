#coding by forsenlol
#!/usr/bin/env python

import pygame
from random import randint
from pygame import font

pygame.font.init()

class Window:

    __name = "2048"
    __size = [450, 450]
    __background_color = "#AA9C99"

    __square_size = [98, 98]
    __square_clean_color = "#BBADA0"
    __square_space = 12

    x_pos = y_pos = __square_space
    play_block = []

    square_font_name = font.Font(None, 25)


    def new_game(self):
        self.screen = pygame.display.set_mode(self.__size)
        pygame.display.set_caption(self.__name)

        self.bg = pygame.Surface(self.__size)
        self.bg.fill(pygame.Color(self.__background_color))

        for i in range(16):
            self.play_block.append(0)

        self.new_square()
        self.new_square()

    def draw_square(self):
        self.x_pos = self.y_pos = self.__square_space
        for i in range(16):
            pf = pygame.Surface(self.__square_size)

            if self.play_block[i] == 0:
                pf.fill(pygame.Color(self.__square_clean_color))
            else:
                p_color = Square().color(self.play_block[i])
                pf.fill(pygame.Color(p_color))

            self.screen.blit(pf, (self.x_pos, self.y_pos))

            if self.play_block[i] > 0:
                self.screen.blit(self.square_font_name.render(str(self.play_block[i]), 1, (0, 0, 0)), (self.x_pos + 10, self.y_pos + 10))

            self.x_pos += self.__square_size[0] + self.__square_space
            if self.x_pos == (self.__square_size[0] + self.__square_space) * 4 + self.__square_space:
                self.x_pos = self.__square_space
                self.y_pos += self.__square_size[0] + self.__square_space

    def new_square(self):
        p_rand_pos = randint(0, 15)

        while self.play_block[p_rand_pos] != 0:
            p_rand_pos = randint(0, 15)
        self.play_block[p_rand_pos] = 2


class Square(Window):


    def key(self, event):
        p_flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for j in range(16):
                for i in range(16):
                    if i != 0 and i != 4 and i != 8 and i != 12 and self.play_block[i] > 0:
                        if self.play_block[i - 1] == self.play_block[i]:
                            self.play_block[i - 1] = self.play_block[i]*2
                            self.play_block[i] = 0
                            p_flag = True
                            break
                        if self.play_block[i - 1] == 0:
                            self.play_block[i - 1] = self.play_block[i]
                            self.play_block[i] = 0
                            p_flag = True
                            continue
            if p_flag == True:
                p_flag = False
                self.new_square()

        p_flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for j in range(16):
                for i in range(15, -1, -1):
                    if i != 3 and i != 7 and i != 11 and i != 15 and self.play_block[i] > 0:
                        if self.play_block[i + 1] == self.play_block[i]:
                            self.play_block[i + 1] = self.play_block[i]*2
                            self.play_block[i] = 0
                            p_flag = True
                            break
                        if self.play_block[i + 1] == 0:
                            self.play_block[i + 1] = self.play_block[i]
                            self.play_block[i] = 0
                            p_flag = True
                            continue
            if p_flag == True:
                p_flag = False
                self.new_square()

        p_flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for j in range(16):
                for i in range(16):
                    if i != 0 and i != 1 and i != 2 and i != 3 and self.play_block[i] > 0:
                        if self.play_block[i - 4] == self.play_block[i]:
                            self.play_block[i - 4] = self.play_block[i]*2
                            self.play_block[i] = 0
                            p_flag = True
                            break
                        if self.play_block[i - 4] == 0:
                            self.play_block[i - 4] = self.play_block[i]
                            self.play_block[i] = 0
                            p_flag = True
                            continue
            if p_flag == True:
                p_flag = False
                self.new_square()

        p_flag = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for j in range(16):
                for i in range(15, -1, -1):
                    if i != 12 and i != 13 and i != 14 and i != 15 and self.play_block[i] > 0:
                        if self.play_block[i + 4] == self.play_block[i]:
                            self.play_block[i + 4] = self.play_block[i]*2
                            self.play_block[i] = 0
                            p_flag = True
                            break
                        if self.play_block[i + 4] == 0:
                            self.play_block[i + 4] = self.play_block[i]
                            self.play_block[i] = 0
                            p_flag = True
                            continue
            if p_flag == True:
                p_flag = False
                self.new_square()

    def color(self, value):
        if value == 2: return "#EEE4DA"
        if value == 4: return "#EDE0C8"
        if value == 8: return "#F2B179"
        if value == 16: return "#F59563"
        if value == 32: return "#F67C5F"
        if value == 64: return "#F65E3B"
        if value == 128: return "#EDCF72"
        if value == 256: return "#EDCC61"
        if value == 512: return "#EDC850"
        if value == 1024: return "#EDC53F"
        if value == 2048: return "#EDC22E"
        if value > 2048: return "#3C3A32"


win = Window()

def main():
    pygame.init()

    win.new_game()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            Square().key(event)
        win.screen.blit(win.bg, (0,0))
        win.draw_square()
        pygame.display.update()


if __name__ == "__main__":
    main()
