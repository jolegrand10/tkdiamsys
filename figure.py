from copy import copy, deepcopy
from turtle import *
from point import Point
from math import sin, cos, pi


class Figure():
    def __init__(self, **parms):
        self.point = []  # list of points
        self.prop = {}
        #default prop values
        self.prop['closed']=False
        self.prop['fillColor'] = 'Red'
        self.prop['backgroundColor']= ""
        self.prop['showTurtle'] = False
        self.prop['lineColor'] = 'Blue'
        self.prop['lineWidth'] = 10
        #update with parms
        for k in parms:
            self.prop [k]= parms[k]

    def __str__(self):
        return "\n".join(self._point() + self._prop())

    def _prop(self):
        """ gives a list of strings showing the props as kwargs"""
        return ["%s = %s" % (str(k), repr(v)) for k, v in self.prop.items()]

    def _point(self):
        """ gives a list of strings showing the repr of points"""
        return list(map(repr,self.point))

    def __repr__(self):
        """ the string that can be evaluated to yield the current object"""
        return "Figure(%s)"%(", ".join(self._point() + self._prop()))

    def __len__(self):
        return len(self.point)


    def centre(self):
        """ computes the center of gravity"""
        n = len(self.point)
        return Point(
            sum(map(lambda p: p.x, self.point)) / n,
            sum(map(lambda p: p.y, self.point)) / n
        )

    def translate(self, dx=0.0, dy=0.0):
        """Translates current object"""
        for p in self.point:
            p.x += dx
            p.y += dy

    def translate1(self, dx=0.0, dy=0.0):
        """creates a new translated object"""
        # copy into new figure nf
        nf = deepcopy(self)
        # apply translation
        for p in nf.point:
            p.x += dx
            p.y += dy
        return nf

    def rotate(self, alpha=0.0, cen=None):
        """Rotates current object"""
        #convert degrees to rads
        alpha = (alpha / 360)*2*pi
        #centre of rotation is center of gravity of the figure,
        #unless otherwise specified
        if cen is None:
            cen= self.centre()
        #change origin of coordinates to local ones
        self.translate(-cen.x, -cen.y)
        for p in self.point:
            x1 =  p.x * cos(alpha) + p.y * sin(alpha)
            y1 = -p.x * sin(alpha) + p.y * cos(alpha)
            p.x,p.y = x1,y1
        #change back coordinates to global
        self.translate(+cen.x, +cen.y)

    def rotate1(self, alpha=0.0, cen=None):
        """Creates a new rotated object"""
        # convert degrees to rads
        alpha = (alpha / 360) * 2 * pi
        # centre of rotation is center of gravity of the figure,
        # unless otherwise specified
        if cen is None:
            cen = self.centre()
        # change origin of coordinates to local ones
        nf = self.translate1(-cen.x, -cen.y)
        for p in nf.point:
            x1 =  p.x * cos(alpha) + p.y * sin(alpha)
            y1 = -p.x * sin(alpha) + p.y * cos(alpha)
            p.x,p.y = x1,y1
        #change back coordinates to global
        return nf.translate1(+cen.x, +cen.y)

def main():
    pass



if __name__ == '__main__':
    main()