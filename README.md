# PR301_Assignment2
The program is fully functional now

## Feature list
1. User can select pen
2. User can put pen down
3. User can move pen up
4. User can move the pen horizontally (go along)
5. User can move the pen vertically (go down)
6. User can draw a line with input direction and distance
7. The system can read commands from text file
8. The system can parse the commands from text file

## Interfaces(Abstract classes) to be tested
* AbstractSourceReader
* AbstractParser
* AbstractDrawer

## Tasks for programmers
- Refactoring
- Make sure the refactored codes still have same behaviours

## Tasks for tester
- Write unit tests
- Evaluate of coder's codes

## doctest example
in parser_jerry.py

        """
        >>> import tkinter
        >>> canvas = tkinter.Canvas(tkinter.Tk(), width=500, height=500)
        >>> import drawer_kieran
        >>> d = DrawerKieran(canvas)
        >>> p = ParserJerry(d)
        >>> p.parse(["X 100"])
        GOTO X=100
        """