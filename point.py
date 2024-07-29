from turtle import *

from math import cos, sin, pi, sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%3.1f, %3.1f)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%3.1f, %3.1f)" % (self.x, self.y)

    def move(self, **kwargs):
        """
            new point at rho, theta from current point
            rho is the distance
            theta is the angle in radians, no default
            dx, dy are the shift coordinates, default is 0
            x, y are absolute coordinates, default is "unchanged"
        """
        if 'rho' in kwargs:
            rho = kwargs['rho']
            theta = kwargs['theta']
            return Point(self.x + rho * cos(theta), self.y + rho * sin(theta))
        if 'dx' in kwargs or 'dy' in kwargs:
            dx = kwargs.get('dx',0)
            dy = kwargs.get('dy',0)
            return Point(self.x+dx, self.y+dy)
        if 'x' in kwargs or 'y' in kwargs:
            x = kwargs.get('x',self.x)
            y = kwargs.get('y', self.y)
            return Point(x,y)
        raise Exception("Named arguments expected for polar or cartesian coordinates")

    def middle(self, p):
        """
            new point at the middle of the segmment from current point to p
        """
        return Point((self.x + p.x) / 2, (self.y + p.y) / 2)

    def distance(self, p):
        """
            distance from current point to p
        """
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    def line(self, p):
        """
            slope and y-intercept of the line passing through self and p
        """
        slope = (p.y - self.y) / (p.x - self.x)
        y_intercept = self.y - slope * self.x
        return slope, y_intercept

    def to_tuple(self):
        return self.x, self.y


def main():
    pass


if __name__ == '__main__':
    main()