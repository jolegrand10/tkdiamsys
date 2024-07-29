from rectangle import Rectangle
from point import Point
from dot import Dot


class Frame(Rectangle):
    THICKNESS = 10  # units are cm

    def __init__(self, origin, dx, dy):
        super().__init__(origin, 0, dx, dy, fillColor='gray50', lineWidth=1)


class Cushion(Rectangle):
    THICKNESS = 5  # units are cm

    def __init__(self, origin, width, height):
        super().__init__(origin,
                         0,
                         width,
                         height,
                         fillColor='RoyalBlue2',
                         lineWidth=1)


class Board(Rectangle):
    def __init__(self, origin, dx, dy):
        super().__init__(origin, 0, dx, dy, fillColor='RoyalBlue3', lineWidth=1)


class Diamond(Dot):
    def __init__(self, p):
        super().__init__(p, dotSize=2, dotColor='yellow', lineColor='')


class Ball(Dot):
    def __init__(self, p=None, color='white'):
        super().__init__(p, dotSize=6, dotColor=color)


class Billard:
    def __init__(self, origin, width, height):
        """

        :param origin: a Point
        :param width: in real world units cm
        :param height: in real world units cm
        """
        #
        #
        #
        self.origin = origin
        self.xmin = origin.x
        self.xmax = origin.x + width
        self.ymin = origin.y
        self.ymax = origin.y + height
        #
        #
        #
        self.display_list = []
        #
        # The most external rectangular wooden frame of the billard
        #
        self.frame = Frame(self.origin, width, height)
        self.display_list.append(self.frame)
        #
        # the inner part where the balls bump is the cushion
        #
        d = Frame.THICKNESS
        self.cushion = Cushion(self.origin.move(dx=d, dy=d),
                               width - 2 * d, height - 2 * d)
        self.display_list.append(self.cushion)
        #
        # the place where the balls roll is the board
        #
        d = Frame.THICKNESS + Cushion.THICKNESS
        self.board = Board(self.origin.move(dx=d, dy=d),
                           width - 2 * d, height - 2 * d)
        self.display_list.append(self.board)
        #
        # add diamonds in the middle of the wooden frame
        #
        frame_width = (self.frame.length - self.cushion.length) / 2
        #
        # the first x is the origin of the board
        #
        xs0 = self.board.origin.x
        #
        # the first y is
        #
        ys0 = self.frame.origin.y + frame_width / 2
        #
        # first diam is at ps0
        #
        ps0 = Point(xs0, ys0)
        south_diams = [Diamond(ps0.move(dx=i * self.board.length / 8)) for i in range(9)]
        north_diams = [Diamond(d.point[0].move(dy=self.frame.width - frame_width)) for d in south_diams]
        self.display_list += south_diams
        self.display_list += north_diams

        #
        # east diams
        #
        xe0 = self.frame.origin.x + frame_width / 2
        ye0 = self.board.origin.y
        pe0 = Point(xe0, ye0)
        #
        # east and west are mixed - ??
        #
        west_diams = [Diamond(pe0.move(dy=i * self.board.width / 4)) for i in range(5)]
        east_diams = [Diamond(d.point[0].move(dx=self.frame.length - frame_width)) for d in west_diams]
        self.display_list += west_diams
        self.display_list += east_diams
        self.diams = { 'north':north_diams, 'east':east_diams, 'south':south_diams , 'west':west_diams}

        #
