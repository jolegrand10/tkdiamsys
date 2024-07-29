from billard import Billard
from point import Point
from dot import Dot
from line import Line
import random

class Grid:
    def __init__(self, billard):
        self.display_list= []
        self.edge = billard.frame.THICKNESS / 2 + billard.cushion.THICKNESS

class Arrival(Grid):
    def __init__(self, billard):
        super().__init__(billard)
        edge_to_edge = False
        if edge_to_edge :
            arr = {
                0:  billard.diams['north'][6].point[0].move(dy=-self.edge),
                10: billard.diams['north'][7].point[0].move(dy=-self.edge),
                20: billard.diams['north'][8].point[0].move(dy=-self.edge),
                25: billard.diams['east'][4].point[0].move(dy=-billard.board.width / 12).move(dx=-self.edge),
                30: billard.diams['east'][4].point[0].move(dy=-billard.board.width / 6).move(dx=-self.edge),
                35: billard.diams['east'][3].point[0].move(dx=-self.edge),
                40: billard.diams['east'][3].point[0].move(dy=-billard.board.width / 12).move(dx=-self.edge),
                45: billard.diams['east'][3].point[0].move(dy=-billard.board.width / 6).move(dx=-self.edge),
                50: billard.diams['east'][2].point[0].move(dx=-self.edge),
                60: billard.diams['east'][2].point[0].move(dy=-billard.board.width / 12).move(dx=-self.edge),
                70: billard.diams['east'][2].point[0].move(dy=-billard.board.width / 6).move(dx=-self.edge),
                80: billard.diams['east'][1].point[0].move(dx=-self.edge),
                90: billard.diams['east'][1].point[0].move(dy=-billard.board.width / 12).move(dx=-self.edge),
            }
            arr1 = {
                0:  billard.diams['south'][0].point[0].move(dy=self.edge),
                10: billard.diams['south'][1].point[0].move(dy=self.edge),
                20: billard.diams['south'][2].point[0].move(dy=self.edge),
                30: billard.diams['south'][3].point[0].move(dy=self.edge),
                40: billard.diams['south'][4].point[0].move(dx=-billard.board.length / 80).move(dy=self.edge),
                50: billard.diams['south'][4].point[0].move(dx=billard.board.length / 16).move(dy=self.edge),
                60: billard.diams['south'][5].point[0].move(dy=self.edge),
                70: billard.diams['south'][5].point[0].move(dx=billard.board.length / 16).move(dy=self.edge),
                80: billard.diams['south'][6].point[0].move(dy=self.edge),
                90: billard.diams['south'][6].point[0].move(dx=billard.board.length / 16).move(dy=self.edge),
            }
        else: # diam to diam
            arr = {
                0: billard.diams['north'][6].point[0],
                10: billard.diams['north'][7].point[0],
                20: billard.diams['north'][8].point[0].move(dy=-self.edge),
                25: billard.diams['east'][4].point[0].move(dy=-billard.board.width / 12),
                30: billard.diams['east'][4].point[0].move(dy=-billard.board.width / 6),
                35: billard.diams['east'][3].point[0],
                40: billard.diams['east'][3].point[0].move(dy=-billard.board.width / 12),
                45: billard.diams['east'][3].point[0].move(dy=-billard.board.width / 6),
                50: billard.diams['east'][2].point[0],
                60: billard.diams['east'][2].point[0].move(dy=-billard.board.width / 12),
                70: billard.diams['east'][2].point[0].move(dy=-billard.board.width / 6),
                80: billard.diams['east'][1].point[0],
                90: billard.diams['east'][1].point[0].move(dy=-billard.board.width / 12),
            }
            arr1 = {
                0: billard.diams['south'][0].point[0],
                10: billard.diams['south'][1].point[0],
                20: billard.diams['south'][2].point[0],
                30: billard.diams['south'][3].point[0],
                40: billard.diams['south'][4].point[0],
                50: billard.diams['south'][4].point[0].move(dx=billard.board.length / 16),
                60: billard.diams['south'][5].point[0],
                70: billard.diams['south'][5].point[0].move(dx=billard.board.length / 16),
                80: billard.diams['south'][6].point[0],
                90: billard.diams['south'][6].point[0].move(dx=billard.board.length / 16),
            }



        for p in arr:
            self.display_list.append(Dot(arr[p],dotText=str(p), dotColor='', lineColor=''))
        for p in arr1:
            self.display_list.append(Dot(arr1[p], dotText=str(p), dotColor='', lineColor=''))
        for p in range(0,100,10):
            self.display_list.append(Line(arr1[p],arr[p],lineColor='blue', lineWidth=1))

class Aim(Grid):
    def __init__(self, billard):
        super().__init__(billard)
        aim = {
            0:  billard.diams['north'][0].point[0],
            10: billard.diams['north'][1].point[0],
            20: billard.diams['north'][2].point[0],
            30: billard.diams['north'][3].point[0],
            40: billard.diams['north'][4].point[0],
            50: billard.diams['north'][5].point[0], #.move(dx=-billard.board.length / 80),
            60: billard.diams['north'][5].point[0].move(dx=billard.board.length / 16),
            70: billard.diams['north'][6].point[0],
            80: billard.diams['north'][6].point[0].move(dx=billard.board.length / 16),
            90: billard.diams['north'][7].point[0],
        }
        for p in aim:
            self.display_list.append(Dot(aim[p], dotText=str(p), dotColor='', lineColor='', fontColor='black'))

class Play(Grid):
    def __init__(self, billard):
        super().__init__(billard)
        play = {
            10: billard.diams['south'][0].point[0],
            15: billard.diams['south'][1].point[0],
            20: billard.diams['south'][2].point[0],
            25: billard.diams['south'][3].point[0],
            30: billard.diams['south'][4].point[0],
            35: billard.diams['south'][5].point[0],
            40: billard.diams['south'][6].point[0],
            45: billard.diams['south'][7].point[0],
            #50: billard.board.origin.move(dx=billard.board.length),  # south_diams[8].point[0],
            50: billard.diams['east'][0].point[0],
            60: billard.diams['east'][1].point[0],
            70: billard.diams['east'][2].point[0],
            80: billard.diams['east'][3].point[0],
            90: billard.diams['east'][4].point[0],

        }
        for p in play:
            self.display_list.append(Dot(play[p], dotText=str(p), dotColor='', lineColor='', fontColor='black'))


class Ball:
    def __init__(self,color='white'):
        self.color = color
        self.size = 6.1
        self.position = Point(random.randint(18,262), random.randint(18,142))
        self.display_list = Dot(self.position, dotSize=int(self.size), dotColor= self.color, lineColor='')

class Spot:
    def __init__(self, position, color='black'):
        self.color = color
        self.size = 1
        self.position = position
        self.display_list = Dot(self.position, dotSize=int(self.size), dotColor= self.color, lineColor='')
class Model:

    def __init__(self, width=280,  height=160):
        """
        Model uses coordinates in the real world
        Origin is set to the lower left corner of the billard
        Billard's dimensions follow
        :param width: width of the billard in cm, usually 280
        :param height: height in cm, usually 160
        """
        self.billard = Billard(Point(0,0), width, height)
        self.ball = {c:Ball(c) for c in 'white orange red'.split()}
        self.grid = {  'aim': Aim(self.billard),
                       'arr': Arrival(self.billard),
                      'play': Play(self.billard)}
        A = self.billard.board.origin.move(dx=self.billard.board.length/4,dy=self.billard.board.width/2)
        B = self.billard.board.origin.move(dx=self.billard.board.length/2,dy=self.billard.board.width/2)
        D = self.billard.board.origin.move(dx=3*self.billard.board.length/4,dy=self.billard.board.width/2)
        C = D.move(dy=16.30)
        E = D.move(dy=-16.30)
        self.spot = [Spot(p) for p in (A,B,C,D,E)]
        #
        #
        #




