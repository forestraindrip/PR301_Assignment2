# created by Kieran Jerry Jonathon
from tigr import AbstractSourceReader


class MainTIGr(AbstractSourceReader):

    def go(self):
        global interface
        if config[2] == 'FrontEndKieran':
            from front_end_kieran import TkinterInterface
            interface = TkinterInterface(self)
        elif config[2] == 'FrontEndJerry':
            from front_end_jerry import GuiInterface
            interface = GuiInterface(self)
        interface.start()


if __name__ == '__main__':
    config = open('config.txt', "r+").read().splitlines()
    if config[0] == 'DrawerKieran':
        from drawer_kieran import Drawer
    elif config[0] == 'DrawerJack':
        from drawer_jack import Drawer
    elif config[0] == 'DrawerTurtleJack':
        from drawer_turtle_jack import Drawer

    if config[1] == 'ParserDang':
        from parser_dang import ParserDang
    elif config[1] == 'ParserJerry':
        from parser_jerry import ParserJerry
    elif config[1] == 'ParserJonathanV2':
        from parser_jonathan_v2 import ParserJonathon

    main = MainTIGr(ParserJonathon(Drawer()))
    main.go()
