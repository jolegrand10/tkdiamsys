from figuredecorator import FigureDecorator
class WithTranslation(FigureDecorator):
    def __init__(self, f, dx=0.0, dy=0.0, **parms):
        super().__init__(f)
        self.dx = dx
        self.dy = dy
        self.figure.translate(self.dx, self.dy)
        self.figure = f


def main():
    from turtle import Screen, done, hideturtle
    from rhombus import Rhombus
    from point import Point
    loz = Rhombus(Point(-150, 200), 0, 100, 40, backgroundColor = 'Yellow')
    tloz=WithTranslation(loz, dx =0, dy = 100.0, backgroundColor = 'Blue')
    print(tloz)
    # tests draw
    win = Screen()
    hideturtle()
    loz.draw()
    tloz.draw()
    done()

if __name__ =='__main__':
    main()