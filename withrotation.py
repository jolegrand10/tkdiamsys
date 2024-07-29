from figuredecorator import FigureDecorator
class WithRotation(FigureDecorator):
    def __init__(self, f, alpha=0.0, **parms):
        #alpha is in degrees
        super().__init__(f,**parms)
        self.figure.rotate(alpha)


def main():
    from turtle import Screen, done, hideturtle
    from rhombus import Rhombus
    from point import Point
    loz = Rhombus(Point(-150, 200), 0, 100, 40, backgroundColor = 'Yellow')
    rloz=WithRotation(loz, alpha = 90)
    # tests draw
    win = Screen()
    hideturtle()
    loz.draw()
    rloz.draw()
    done()

if __name__ =='__main__':
    main()