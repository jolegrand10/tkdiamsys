from figure import Figure
from copy import copy
class Polyline(Figure):
    """ a sequence of connected lines defined by a list of points"""
    def __init__(self,*points, **parms):
        super().__init__(**parms)
        for p in points:
            self.point.append(copy(p))





def main():
    from point import Point
    from turtle import Screen, done, hideturtle
    p = Polyline(Point(1, 2), Point(200, 103), Point(130, 140), Point(40, 150), lineColor="pink", backgroundColor="green")
    #tests draw
    win=Screen()
    hideturtle()
    p.draw()
    done()

if __name__ == '__main__':
    main()

