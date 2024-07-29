from polygon import Polygon
from math import cos, sin, pi, sqrt

class Rhombus(Polygon):
    def __init__(self, origin, angle, length, width, **parms):
        self.origin =origin
        self.angle = angle
        self.length = length
        self.width = width

        p0 = origin
        p2 = p0.move(length, angle)
        m = p0.middle(p2)
        p1 = m.move(width / 2, angle - pi / 2)
        p3 = m.move(width / 2, angle + pi / 2)
        points = [p0, p1, p2, p3]
        super().__init__(*points, **parms)


def main():
    from point import Point
    from turtle import Screen, hideturtle, done
    r = Rhombus (Point(1, 2), pi / 10, 150, 100, lineColor ="pink", fillColor='blue', backgroundColor ="green")
#    r = Rhombus(Point(-150, 200), 0, 100, 40)
    #tests draw
    win=Screen()
    hideturtle()
    r.draw()
    done()

if __name__ == '__main__':
    main()