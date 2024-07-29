from turtle import *
from figure import Figure
from point import Point
class Dot(Figure):
    """ a simple figure made of a dot defined by 1 point """
    def __init__(self,p,dotSize=5, dotColor='White', dotText='', fontName='Arial', fontSize=8, fontColor='blue',
                 lineColor='blue'):
        """ setup the features of a dot at point p """
        super().__init__()
        self.point = [p]
        self.prop['dotSize'] = dotSize
        self.prop['dotColor'] = dotColor
        self.prop['dotText'] = dotText
        self.prop['fontName'] = fontName
        self.prop['fontSize'] = fontSize
        self.prop['fontColor'] = fontColor
        self.prop['lineColor'] = lineColor


    def __repr__(self):
        return "Dot(%s)" % (", ".join(self._point() + self._prop()))



def main():
    pass

if __name__ == '__main__':
    main()