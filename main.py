
##TODO 
# Drag factor (friction)

# import pygame
# pygame.init()

class World():
    def __init__(self) -> None:
        self.Height = 50 ## Might want to generate custom world rather than a rectangle
        self.Width  = 100

        self.ball = Ball()

    def main(self):

        while(True):
            new_x = self.ball.x + self.ball.vx
            new_y = self.ball.y + self.ball.vy

            if new_x == (self.Width - 1) or new_x == 0:
                self.ball.vx = -self.ball.vx
            
            if new_y == (self.Height - 1) or new_y == 0:
                self.ball.vy = self.ball.vy


    def display(self):
        for y
        pass


class Ball():
    def __init__(self, initial_x, initial_y, initial_vx = 1, initial_vy= 1) -> None:
        self.x  = initial_x
        self.y  = initial_y
        self.vx = initial_vx #
        self.vy = initial_vy

    

