from copy import deepcopy,copy

from figuredecorator import FigureDecorator
class WithTransparency(FigureDecorator):

    def __init__(self, f):
        super().__init__(f)
        self.figure.prop['fillColor'] = ""



def main():
    from turtle import Screen, done, hideturtle
    from rhombus import Rhombus
    from withtranslation import WithTranslation
    from point import Point
    loz = Rhombus(Point(-150, 200), 0, 100, 40, lineColor ='pink', fillColor='blue')
    tploz = WithTransparency(WithTranslation(deepcopy(loz),+100, -100))
    # tests draw
    win = Screen()
    hideturtle()
    loz.draw()
    tploz.draw()
    done()

if __name__ == '__main__':
    main()