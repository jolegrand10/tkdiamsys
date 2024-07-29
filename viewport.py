
import tkinter as tk
from itertools import chain
from functools import reduce
from point import Point

class Viewport:
    def __init__(self, rect_area, canvas):
        """
        Maps a rectangular area of the real world to a region of the screen, the canvas
        :param rect_area: a Rectangle object in real-world coordinates
        :param canvas: a canvas
        :param color: the default color for the drawings
        :param width: the default line width for the drawing
        """
        self.canvas = canvas
        self.area = rect_area
        # origin in real world is Point(0,0)
        #
        # length is supposed to be the larger dimension of the rectangle
        # mapped to the width of the canvas
        #
        self.zoom = canvas.winfo_reqwidth() / self.area.length
        #
        # find the bottom left corner
        #
        self.xmin = min(map(lambda p: p.x, self.area.point))
        self.ymin = min(map(lambda p: p.y, self.area.point))

    def t(self, p):
        """ converts real world coordinates to canvas coordinates with the origin set at its bottom left corner
          p is a Point
          returns a Point """
        return  Point((p.x -self.xmin) * self.zoom ,
                      -(p.y - self.ymin) * self.zoom + self.canvas.winfo_reqheight())



    def line(self, *p):
        if len(p)<2:
            raise TypeError("A line needs at least two points")
        r = p[0]
        for q in p[1:]:
            self.canvas.create_line(*self.t(r).to_tuple()
                             *self.t(q).to_tuple(),
                             fill='blue',
                             width=2)
            r = q

    def dot(self, p,  dotSize=3, dotColor='red', dotText='', fontName='Arial', fontSize=8, fontColor='blue', lineColor='black'):
        #TODO adapt font size with zoom factor
        l = []
        if dotSize:
            dx = dotSize * self.zoom
            dy = dotSize * self.zoom
            oval_id = self.canvas.create_oval(p.x-dx/2, p.y-dy/2, p.x+dx/2, p.y+dy/2, fill=dotColor, outline=lineColor)
            l.append(oval_id)
        if dotText:
            text_id = self.canvas.create_text(p.x, p.y, text=dotText, font=(fontName, fontSize), fill=fontColor)
            l.append(text_id)
        if len(l)==1:
            return l[0]
        return l

    def draw(self, f):
        """ f is a figure, a list of figures or dict of figures and draw returns a drawing leaving in self.canvas"""
        # TODO structural pattern matching would be appropriate here
        if type(f) is list:
            return [self.draw(x) for x in f]
        elif type(f) is dict:
            return { k: self.draw(v) for k,v in f.items()}
        elif len(f.point) == 1 :
            #
            # Dot
            #
            return self.dot(self.t(f.point[0]),
                            dotSize=f.prop['dotSize'],
                            dotColor=f.prop['dotColor'],
                            dotText=f.prop['dotText'],
                            fontName=f.prop['fontName'],
                            fontSize=f.prop['fontSize'],
                            fontColor=f.prop['fontColor'],
                            lineColor=f.prop['lineColor'])
        elif f.prop['closed']:
            #
            # Polygon
            #
            return self.canvas.create_polygon(
                *chain.from_iterable(map(lambda p: self.t(p).to_tuple() , f.point)),
                outline=f.prop['lineColor'],
                fill=f.prop['fillColor'],
                width=f.prop['lineWidth']
            )
        else:
            #
            # Polyline
            #
            return self.canvas.create_line(
                list(
                    reduce(lambda a,b: a+b,
                           [ (e.x, e.y) for e in map(lambda p: self.t(p), f.point)]
                    )
                ),
                fill=f.prop['lineColor'],
                width=f.prop['lineWidth'])



def main():
    pass




if __name__ == '__main__':
    main()