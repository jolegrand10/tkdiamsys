#
# bande d'arrivée
#
edge = frame_width / 2 + cushion_width
self.arr = {
    0: north_diams[6].point[0].move(dy=-edge),
    10: north_diams[7].point[0].move(dy=-edge),
    20: north_diams[8].point[0].move(dy=-edge),
    25: east_diams[4].point[0].move(dy=-self.board.width / 12).move(dx=-edge),
    30: east_diams[4].point[0].move(dy=-self.board.width / 6).move(dx=-edge),
    35: east_diams[3].point[0].move(dx=-edge),
    40: east_diams[3].point[0].move(dy=-self.board.width / 12).move(dx=-edge),
    45: east_diams[3].point[0].move(dy=-self.board.width / 6).move(dx=-edge),
    50: east_diams[2].point[0].move(dx=-edge),
    60: east_diams[2].point[0].move(dy=-self.board.width / 12).move(dx=-edge),
    70: east_diams[2].point[0].move(dy=-self.board.width / 6).move(dx=-edge),
    80: east_diams[1].point[0].move(dx=-edge),
    90: east_diams[1].point[0].move(dy=-self.board.width / 12).move(dx=-edge),
}
#
# bande de direction ou autre extrémité de la ligne d'arrivée
#
self.arr1 = {
    0: south_diams[0].point[0].move(dy=edge),
    10: south_diams[1].point[0].move(dy=edge),
    20: south_diams[2].point[0].move(dy=edge),
    30: south_diams[3].point[0].move(dy=edge),
    40: south_diams[4].point[0].move(dx=-self.board.length / 80).move(dy=edge),
    50: south_diams[4].point[0].move(dx=self.board.length / 16).move(dy=edge),
    60: south_diams[5].point[0].move(dy=edge),
    70: south_diams[5].point[0].move(dx=self.board.length / 16).move(dy=edge),
    80: south_diams[6].point[0].move(dy=edge),
    90: south_diams[6].point[0].move(dx=self.board.length / 16).move(dy=edge),

}
self.play = {
    10: south_diams[0].point[0],
    15: south_diams[1].point[0],
    20: south_diams[2].point[0],
    25: south_diams[3].point[0],
    30: south_diams[4].point[0],
    35: south_diams[5].point[0],
    40: south_diams[6].point[0],
    45: south_diams[7].point[0],
    50: self.board.origin.move(dx=self.board.length),  # south_diams[8].point[0],
    60: east_diams[1].point[0],
    70: east_diams[2].point[0],
    80: east_diams[3].point[0],
    90: east_diams[4].point[0],

}

self.aim = {
    0: north_diams[0].point[0],
    10: north_diams[1].point[0],
    20: north_diams[2].point[0],
    30: north_diams[3].point[0],
    40: north_diams[4].point[0],
    50: north_diams[5].point[0].move(dx=-self.board.length / 80),
    60: north_diams[5].point[0].move(dx=self.board.length / 16),
    70: north_diams[6].point[0],
    80: north_diams[6].point[0].move(dx=self.board.length / 16),
    90: north_diams[7].point[0],

}


def make_gridr(self, step=20):
    """ Makes a grid in real coordinates"""
    grid_color = 'blue'
    height = self.ymax - self.ymin
    width = self.xmax - self.xmin
    x0 = (self.xmin + self.xmax) / 2
    y0 = (self.ymin + self.ymax) / 2
    display_list = []
    #
    # draw x axis from P
    #
    display_list.append(Line(Point(self.xmin, y0), Point(self.xmax, y0), lineColor=grid_color, lineWidth=1))
    #
    # draw ticks on x axis
    #
    ti = 1.5  # in real world units cm
    dx = width / 2
    n = int(dx / step)
    for i in range(-n + 1, n):
        xi = x0 + i * step
        display_list.append(Line(Point(xi, y0 - ti), Point(xi, y0 + ti), lineColor=grid_color, lineWidth=1))
        # self.canvas.create_text(xi, y0 + 2 * ti, text=str(round(xi)), anchor='n', font=('Arial', 6))
    #
    # draw y axis
    #
    display_list.append(Line(Point(x0, self.ymin), Point(x0, self.ymax), lineColor=grid_color, lineWidth=1))
    dy = height / 2
    n = int(dy / step)
    for i in range(-n + 1, n):
        yi = y0 + i * step
        display_list.append(Line(Point(x0 - ti, yi), Point(x0 + ti, yi), lineColor=grid_color, lineWidth=1))

        # self.canvas.create_text(x0 - ti, yi, text=str(round(yi)), anchor='e', font=('Arial', 6))
    return display_list





    def arrival_grid(self, view):
        color('white')
        for k, p in self.arr.items():
            if int(k) <= 20:
                view.goto(p.move(dy=1))
            else:
                view.goto(p.move(dx=1))
            write(k)
        # for p in billard.arr1:
        #     v.draw(Dot(billard.arr1[p], dotSize=3, dotColor='magenta'))
        for k, p in self.arr1.items():
            # v.goto(p.move(dy=+15))
            view.goto(p.move(dy=-4))
            write(k, align='center')
        for k in range(0, 100, 10):
            view.line(self.arr1[k], self.arr[k])

    def player_grid(self, view):
        # dessiner les bandes du joueur
        color('green')
        #
        #
        # TODO should be based on diams not pay
        for k, p in self.play.items():
            if int(k) <= 50:
                view.goto(p.move(dy=-10))
            else:
                view.goto(p.move(dx=+10))
            write(k, align='center')

    def aim_grid(self, view):
        # dessiner la bande de visée
        color('blue')
        for k, p in self.aim.items():
            view.goto(p.move(dy=+5))
            write(k, align='center')

    def solve(self, a, ball, v):

        def searchx(x, d):
            k1 = None
            k2 = None
            for k in sorted(d):
                if d[k].x < x:
                    k1 = k
            for k in sorted(d, reverse=True):
                if d[k].x > x:
                    k2 = k
            return k1 + (x - d[k1].x) / (d[k2].x - d[k1].x)

        def start(arrivee):
            for visee in range(0, 90, 2):
                depart = arrivee + visee
                if depart >= 10 and depart < 90:
                    print("Essai de départ en ", depart)
                    # On explore les demi droites départ - bille
                    #
                    # le départ peut passer sur la petite bande et ce n'est pas encore fait !
                    #
                    #
                    try:
                        slope, y_intersect = self.play.get(depart, approche(depart, self.play)).line(ball[0].point[0])
                    except ZeroDivisionError:
                        #
                        # c'est le cas où le repère de départ est juste aligné sous la bille.
                        #
                        slope = None
                        y_intersect = None
                    #

                    # intersecte-t-elle la bande de visée dans la limite du billard?
                    if slope:
                        x = (self.board.origin.y + self.board.width - y_intersect) / slope
                        if x >= self.board.origin.x and x <= self.board.origin.x + self.board.length:
                            # vérifier que l'intersection trouvée correspond à la visée souhaitée
                            w = searchx(x, self.aim)

                            if abs(visee - w) < 1:
                                print(
                                    f"Pour arriver en {arrivee}, il faut viser en {visee} en partant de {depart} mais l'on arrive en {w}")
                                yield visee, depart

        def trajectoire(arrivee, visee, depart):
            #
            # on part de la blanche (que l'on appelle la "1" et qui est numérotée 0, en Python !
            #
            p0 = ball[0].point[0]
            #
            # on arrive au point visé sur la bande de visée
            # par la droite
            slope, y_intersect = self.play.get(depart, approche(depart, self.play)).line(
                self.aim.get(visee, approche(visee, self.aim)))
            #
            # qui coupe la bande de visée en x
            x = (self.board.origin.y + self.board.width - y_intersect) / slope
            #
            p1 = (Point(x, self.board.origin.y + self.board.width))
            #
            # le 3ème point est celui où l'on veut arriver sur la 3ème bande
            #
            p3 = self.arr1.get(arrivee, approche(arrivee, self.arr1))
            p4 = self.arr.get(arrivee, approche(arrivee, self.arr))
            #
            # Pour trouver p2 on dit que c'est l'intersection de la 2eme bande
            # avec une droite qui a la même pente que p0,p1
            # et qui passe par p3
            #
            #   y = slope * x + b
            #   b = p3.y - slope * p3.x
            #
            #  On cherche l'intersection avec la verticale x = self.board.origin.x
            p2 = Point(self.board.origin.x,
                       slope * self.board.origin.x + p3.y - slope * p3.x)
            #
            #
            #
            return p0, p1, p2, p3, p4

        gen = start(a)
        while True:
            try:
                visee, depart = next(gen)
                t = trajectoire(a, visee, depart)
                #
                # dessiner la trajectoire
                #
                v.line(*t)
                #
                #
                #
                input("Press enter to continue")
            except StopIteration:
                print("No more choice")
                break


def approche(kval, dico):
    try:
        return dico[kval]
    except KeyError:
        #
        # interpolate
        #
        k1 = None
        k2 = None
        for k in sorted(dico):
            if k < kval:
                k1 = k
            else:
                break
        for k in sorted(dico, reverse=True):
            if k > kval:
                k2 = k
            else:
                break
        if k1 is not None and k2 is not None:
            #
            # on fait une interpolation linéaire
            #
            p1 = dico[k1]
            p2 = dico[k2]
            t = (kval - k1) / (k2 - k1)
            return Point(p1.x + t * (p2.x - p1.x),
                         p1.y + t * (p2.y - p1.y))
        elif k2 is None:
            # extrapolate to the right
            print(f"Cannot extrapolate to the right for {kval}")
            return dico[max(dico.keys())]
        else:  # k1 is None
            # extrapolate to the left
            print(f"Cannot extrapolate to the left for {kval}")
            return dico[min(dico.keys())]


    def make_gridr(self, step=20):
        """ Makes a grid in real coordinates"""
        grid_color = 'blue'
        height = self.ymax - self.ymin
        width = self.xmax - self.xmin
        x0 = (self.xmin+self.xmax)/2
        y0 = (self.ymin+self.ymax)/2
        display_list = []
        #
        # draw x axis from P
        #
        display_list.append(Line(Point(self.xmin, y0), Point(self.xmax, y0), lineColor=grid_color, lineWidth=1 ))
        #
        # draw ticks on x axis
        #
        ti = 1.5 #in real world units cm
        dx = width / 2
        n = int(dx / step)
        for i in range(-n + 1, n):
            xi = x0 + i * step
            display_list.append(Line(Point(xi, y0 - ti), Point(xi, y0 + ti), lineColor=grid_color, lineWidth=1 ))
            #self.canvas.create_text(xi, y0 + 2 * ti, text=str(round(xi)), anchor='n', font=('Arial', 6))
        #
        # draw y axis
        #
        display_list.append(Line(Point(x0, self.ymin), Point(x0, self.ymax), lineColor=grid_color, lineWidth=1))
        dy = height / 2
        n = int(dy / step)
        for i in range(-n + 1, n):
            yi = y0 + i * step
            display_list.append(Line(Point(x0 - ti, yi), Point(x0 + ti, yi), lineColor=grid_color, lineWidth=1))

            #self.canvas.create_text(x0 - ti, yi, text=str(round(yi)), anchor='e', font=('Arial', 6))
        return display_list

    def make_gridc(self, step=10):
        """ Makes a grid in canvas coordinates"""
        #
        # draw x axis
        #
        height = self.canvas.winfo_reqheight()
        width = self.canvas.winfo_reqwidth()
        self.canvas.create_line(0, height/2,  width, height/2,
                         fill=Viewport.GRID_COLOR,
                         width=self.lineWidth)
        #
        # draw ticks on x axis
        #
        ti = 5
        x0 = width / 2
        y0 = height /2

        dx = width / 2
        n = int(dx / step)
        for i in range(-n+1, n):
            xi = x0 + i * step
            self.canvas.create_line(xi,y0-ti, xi, y0+ti, fill=Viewport.GRID_COLOR,
                         width=self.lineWidth)

            self.canvas.create_text(xi, y0+2*ti, text=str(round(xi)), anchor='n', font=('Arial', 6))
        #
        # draw y axis
        #
        self.canvas.create_line(width / 2, 0, width / 2, height,
                                fill=Viewport.GRID_COLOR,
                                width=self.lineWidth)
        dy = height / 2
        n = int(dy / step)
        for i in range(-n+1, n):
            yi = y0 + i * step
            self.canvas.create_line(x0-ti, yi, x0+ti, yi, fill=Viewport.GRID_COLOR,
                         width=self.lineWidth)

            self.canvas.create_text(x0-ti, yi, text=str(round(yi)), anchor='e', font=('Arial', 6))