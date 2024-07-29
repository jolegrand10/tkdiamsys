from dot import Dot
from figuredecorator import FigureDecorator
from withtranslation import WithTranslation


class WithCentre(FigureDecorator):
    def __init__(self, f, centreSize = 5, centreColor ='Yellow',**parms):
        super().__init__(f, **parms)
        self.figure.prop['centreSize'] = centreSize
        self.figure.prop['centreColor'] = centreColor

    def draw(self):
        self.figure.draw()
        Dot(self.centre(), dotColor = self.figure.prop['centreColor'], dotSize = self.figure.prop['centreSize']).draw()


def main():
    from turtle import Screen, done, hideturtle
    from rhombus import Rhombus
    from point import Point
    loz = Rhombus(Point(-150, 200), 0, 100, 40, backgroundColor = 'Yellow')
    cloz = WithCentre(loz, centreSize = 12, centreColor = "White")
    tcloz = WithTranslation(cloz, dx=-100, dy= -100)

    ctloz= WithCentre(WithTranslation(cloz, dx=100, dy= -100), centreSize = 12, centreColor = "White")
    # tests draw
    win = Screen()
    hideturtle()
    cloz.draw()
    #test that center and translation do commute
    tcloz.draw()
    ctloz.draw()
    done()


if __name__ == '__main__':
    main()
