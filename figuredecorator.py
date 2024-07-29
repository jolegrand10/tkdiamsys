from figure import Figure
from copy import copy, deepcopy

class FigureDecorator(Figure):
    def __init__(self, f):
        self.figure = deepcopy(f)


    def __repr__(self):
        return repr(self.figure)

    def __len__(self):
        return len(self.figure)

    def _prop(self):
        """ gives a list of strings showing the props as kwargs"""
        return self.figure._prop()

    def _point(self):
        """ gives a list of strings showing the repr of points"""
        return self.figure._point()

    def centre(self):
        return self.figure.centre()


    def translate(self, dx=0.0, dy=0.0):
        self.figure.translate(dx, dy)

    def rotate(self, alpha = 0.0, cen = None):
        self.figure.rotate(alpha, cen)

def main():
    """ a kind of self tests"""
    from dot import Dot
    from point import Point
    df = FigureDecorator(Dot(Point(100, -310)))
    print(df)
    print(repr(df))


if __name__ == '__main__':
    main()
