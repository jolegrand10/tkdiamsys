import tkinter as tk
from point import Point
from rectangle import Rectangle
from viewport import Viewport
class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("TkDiamSys")

        # Create a menubar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Create a File menu
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Draw Line", command=self.controller.draw_line)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        # Create a Ball menu
        ball_menu = tk.Menu(self.menubar, tearoff=0)
        ball_menu.add_command(label="Start", command=self.set_balls_at_start)
        ball_menu.add_separator()
        ball_menu.add_command(label="Set Pos White", command=self.set_pos_white_ball)
        ball_menu.add_command(label="Set Pos Amber", command=self.set_pos_orange_ball)
        ball_menu.add_command(label="Set Pos Red", command=self.set_pos_red_ball)
        ball_menu.add_separator()
        ball_menu.add_command(label="Show White", command=self.controller.show_white_ball)
        ball_menu.add_command(label="Show Amber", command=self.controller.show_orange_ball)
        ball_menu.add_command(label="Show Red", command=self.controller.show_red_ball)
        self.menubar.add_cascade(label="Ball", menu=ball_menu)

        # Create a Grid menu with checkable options to show/hide each grid
        self.grid_menu = tk.Menu(self.menubar, tearoff=0)
        self.var={}
        for g in self.controller.GRIDS:
            self.var[g] = tk.IntVar(self.root)
            self.var[g].set(self.controller.display_dict[g][0])
            self.grid_menu.add_checkbutton(label=g, variable=self.var[g],
                                           onvalue=1, offvalue=0,
                                           command=lambda x=g: self.toggle_grid(x))
        self.menubar.add_cascade(label="Grid", menu=self.grid_menu)


        # Create a canvas
        w = 1400
        h = 800
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg="white")
        self.canvas.pack(expand=True)

        # Bind resize event
        self.root.bind("<Configure>", self.controller.center_canvas)

        # Create the viewport to map real world coordinates to the canvas
        p1 = Point(0, 0)
        p2 = Point(280, 160)
        self.vp = Viewport(Rectangle.make2p(p1,p2), self.canvas)
        #
        # Populate drawing with items supplied by controller
        #
        self.drawing = {}
        for f,v in self.controller.display_dict.items():
            self.drawing[f] = self.vp.draw(v[1])
        #
        # Hide grids
        #
        for g in controller.GRIDS:
            self.hide(self.drawing[g])

    def toggle_grid(self, g):
        if self.var[g].get() :
            print(f"{g} is now enabled")
            self.controller.display_dict[g] = True, self.controller.display_dict[g][1]
            self.show(self.drawing[g])
        else:
            print(f"{g} is now disabled")
            self.controller.display_dict[g] = False, self.controller.display_dict[g][1]
            self.hide(self.drawing[g])
        self.canvas.update()

    def show(self, f):
        if type(f) is list:
            for e in f:
                self.show(e)
        elif type(f) is dict:
            for k, v in f:
                self.show(v)
        else:
            self.canvas.itemconfigure(f, state='normal')

    def hide(self, f):
        if type(f) is list:
            for e in f:
                self.hide(e)
        elif type(f) is dict:
            for k,v in f:
                self.hide(v)
        else:
            self.canvas.itemconfigure(f, state='hidden')

    def set_balls_at_start(self):
        print("Set balls at starting pos")
        self.controller.set_balls_at_start()
        print("Updating canvas")
        self.canvas.update()


    def set_pos_white_ball(self):
        pass
    def set_pos_orange_ball(self):
        pass
    def set_pos_red_ball(self):
        pass

