from figure import Figure
from point import Point
from turtle import *
from copy import copy
class Line(Figure):
    """ another less simple figure made of a segment defined by 2 points """
    def __init__(self, a, b, **parms):
        """ the line from a to b, where a and b are Points """
        super().__init__(**parms)
        self.point.append(copy(a))
        self.point.append(copy(b))
        self.prop['closed'] = False

    def __repr__(self):
        return "Line(%s)"%(", ".join(self._point() + self._prop()))


def main():
    from turtle import hideturtle, done, Screen
    p1 = Point(0,0)
    p2 = Point( 200,200)
    l= Line (p1, p2)
    win=Screen()
    hideturtle()
    l.draw()
    done()




if __name__ == '__main__':
    main()