from polyline import Polyline
from figure import Figure
class Polygon(Polyline):
    """ a polygon defined by its vertices (points)"""
    def __init__(self,*points,**parms):
        super().__init__(*points,**parms)
        self.prop['closed'] = True

def main():
    from point import Point
    from turtle import Screen, hideturtle, done
    p = Polygon (Point(10, 20), Point(200, 130), Point(130, 40), Point(140, 150), lineColor ="pink", backgroundColor ="green")
    #tests draw
    win=Screen()
    hideturtle()
    p.draw()
    done()
if __name__ == '__main__':
    main()

