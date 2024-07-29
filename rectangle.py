from copy import copy
from point import Point
from polygon import Polygon
from math import cos, sin, pi, sqrt
class Rectangle(Polygon):
    """ a rectangle defined by its origin, orientation and size"""
    def __init__(self, origin, angle, length, width, **parms):
        """ origin is the starting point for the drawing
            angle is an angle in radians / gives the direction of the axis of the rectangle
            length is the size of the biggest edge of the rectangle
            width is the size of its smallest edge
        """
        self.origin =origin
        self.angle = angle
        self.length = length
        self.width = width

        #prepare the list of points
        points =[]
        p=copy(origin)
        points.append(p)
        p=p.move(rho=length, theta=angle)
        points.append(p)
        p=p.move(rho=width, theta=angle + pi/2)
        points.append(p)
        p=p.move(rho=length, theta=angle-pi)
        points.append(p)
        super().__init__(*points,**parms)

    @classmethod
    def make2p(cls, p1, p2, **parms):
        origin= copy(p1)
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        if dx * dy > 0:
            if dx > 0:
                angle = 0
            else:
                angle = pi
        else:
            if dy > 0:
                angle = pi / 2
            else:
                angle = 3 * pi / 2
        length = abs(dx)
        width = abs(dy)
        return Rectangle(origin, angle, length, width, **parms)



def main():
    from point import Point
    from turtle import Screen, hideturtle, done
    r = Rectangle (Point(1, 2), pi / 10, 150, 100, lineColor ="pink", fillColor ="green")
    print(r)
    #tests draw
    win=Screen()
    hideturtle()
    r.draw()
    done()

if __name__ == '__main__':
    main()