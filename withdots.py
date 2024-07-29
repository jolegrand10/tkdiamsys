from dot import Dot
from figuredecorator import FigureDecorator


class WithDots(FigureDecorator):
    def __init__(self, f, dotSize = 5, dotColor = 'White', **parms):
        super().__init__(f, **parms)
        self.figure.prop['dotSize'] = dotSize
        self.figure.prop['dotColor'] = dotColor

    def draw(self):
        self.figure.draw()
        for p in self.figure.point:
            Dot(p,
                self.figure.prop['dotSize'],
                self.figure.prop['dotColor']
                ).draw()


def main():
    from turtle import Screen, done, hideturtle
    from rhombus import Rhombus
    from point import Point
    from withtranslation import WithTranslation
    loz = Rhombus(Point(-150, 200), 0, 100, 40, backgroundColor = 'Yellow')
    dloz = WithDots(loz, dotSize = 12, dotColor = "White")
    tdloz = WithTranslation(dloz, dx = -100, dy = -100)
    dtloz = WithDots(WithTranslation(dloz, dx = 100, dy = -100), dotSize = 12, dotColor = "White")
    # tests draw
    win = Screen()
    hideturtle()
    dloz.draw()
    # test that center and translation do commute
    tdloz.draw()
    dtloz.draw()
    done()

if __name__ == '__main__':
    main()