# Works by KC and Jack
import turtle
import my_enums
from tigr import AbstractDrawer


class DrawerTurtleJack(AbstractDrawer):
    config = open('config.txt', "r+").read().splitlines()
    if config[2] == 'FrontEndKieran':
        from front_end_kieran import TkinterInterface
        this_canvas = TkinterInterface.canvas
    elif config[2] == 'FrontEndJerry':
        from front_end_jerry import GuiInterface
        this_canvas = GuiInterface.canvas

    def __init__(self, ):
        self.test_string = ''
        self.cursor = turtle.RawPen(self.this_canvas)
        self.cursor.speed(1)
        self.penIsDown = True

    # pen_num should be int
    def select_pen(self, pen_num):
        self.cursor.color(my_enums.Pen.colours[pen_num])
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.penIsDown = True
        print('pen down')

    def pen_up(self):
        self.penIsDown = False
        print('pen up')

        # along should be int

    def go_along(self, along):
        self.pen_up()
        self.cursor.setx(along - 250)
        print(f'GOTO X={along}')

        # down should be int

    def go_down(self, down):
        self.pen_up()
        self.cursor.sety(down - 250)
        print(f'GOTO X={down}')

        # direction and distance should be int

    def draw_line(self, direction, distance):
        self.cursor.setheading(direction + 90)
        self.cursor.forward(distance)
        print(f'drawing line of length {distance} at {direction} degrees')
