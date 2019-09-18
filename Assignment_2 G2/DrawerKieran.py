# created by Kieran Jerry Jonathon
import math
import MyEnums
from TIGr import AbstractDrawer


class Drawer(AbstractDrawer):
    x_pos = 0
    y_pos = 0
    config = open('config.txt', "r+")
    c = config.read().splitlines()
    if c[2] == 'FrontEndKieran':
        from FrontEndKieran import TkinterInterface
        this_canvas = TkinterInterface.canvas
        model_capture = TkinterInterface.interface_capture
    elif c[2] == 'FrontEndJerry':
        from FrontEndJerry import GuiInterface
        this_canvas = GuiInterface.canvas
        model_capture = GuiInterface.interface_capture
    config.close()

    def __init__(self):
        self.test_string = ''
        self.colour = ''
        self.can_draw = False

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.colours[pen_num]
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.can_draw = True
        print('pen down')
        self.model_capture += ['pen down']
        self.update_interface()

    def pen_up(self):
        self.can_draw = False
        print('pen up')
        self.model_capture += ['pen up']
        self.update_interface()

    def go_along(self, along):
        self.x_pos = along
        print(f'GOTO X={along}')
        self.model_capture += [f'GOTO X={along}']
        self.update_interface()

    def go_down(self, down):
        self.y_pos = down
        print(f'GOTO X={down}')
        self.model_capture += [f'GOTO X={down}']
        self.update_interface()

    def draw_line(self, direction, distance):
        if self.can_draw:
            degrees = direction
            shape = ''
            if degrees == 0:
                degrees = 360
            # test a direction angle direction = 30 Angle direction needs to be converted a decimal and divided into
            # pie. This is required math.sin and math.cos
            degrees = (math.pi * 2) / (360 / degrees)
            new_x = distance * math.sin(degrees)
            new_y = -distance * math.cos(degrees)
            shape = self.this_canvas.create_line(self.x_pos, self.y_pos, self.x_pos + round(new_x),
                                                 self.y_pos + round(new_y), fill=self.colour)
            self.x_pos += round(new_x)
            self.y_pos += round(new_y)
            print(f'drawing line of length {distance} at {direction} degrees')
            self.model_capture += [self.this_canvas.coords(shape)]
            self.update_interface()

    def update_interface(self):
        if self.c[2] == 'FrontEndKieran':
            from FrontEndKieran import TkinterInterface
            # print(self.model_capture)
            TkinterInterface.interface_capture = self.model_capture
        elif self.c[2] == 'FrontEndJerry':
            # print(self.model_capture)
            from FrontEndJerry import GuiInterface
            GuiInterface.interface_capture = self.model_capture
