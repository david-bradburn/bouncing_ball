
##TODO 
# Drag factor (friction)

# import pygame
# pygame.init()
import time

class World():
    def __init__(self) -> None:
        self.Height = 20 ## Might want to generate custom world rather than a rectangle
        self.Width  = 30

        self.ball = Ball(2, 3)

        self.main()

    def main(self):
        self.display()
        n = 0
        while(True):
            time.sleep(0.1)
            n += 1
            self.ball.x += self.ball.vx
            self.ball.y += self.ball.vy

            if self.ball.x == (self.Width - 1) or self.ball.x == 0:
                self.ball.vx = -self.ball.vx
            
            if self.ball.y == (self.Height - 1) or self.ball.y == 0:
                self.ball.vy = -self.ball.vy
            


            self.display()
            

    def screen_clear(self):

        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'

        for i in range(self.Height + 1):
            print(LINE_UP, end=LINE_CLEAR)

    def display(self):#|-+
        display_str = ""
        for y_coord in range(self.Height):
            str_temp = ""
            for x_coord in range(self.Width):
                if x_coord == self.ball.x and y_coord == self.ball.y:
                    str_temp += "X"
                else:
                    str_temp += " "

            display_str = str_temp + "\n" + display_str

            # print()
        self.screen_clear()
        print(display_str)


class Ball():
    def __init__(self, initial_x, initial_y, initial_vx = 1, initial_vy= 1) -> None:
        self.x  = initial_x
        self.y  = initial_y
        self.vx = initial_vx #
        self.vy = initial_vy


g = World()    

