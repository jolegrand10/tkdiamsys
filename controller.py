from model import Model
from view import View


class Controller:
    GRIDS = 'aim', 'arr', 'play'
    BALLS = 'white orange red'.split()
    def __init__(self, root):
        self.model = Model()

        self.display_dict={}
        self.display_dict['billard'] = True, self.model.billard.display_list
        for g in Controller.GRIDS:
            self.display_dict[g] = False, self.model.grid[g].display_list
        for b in Controller.BALLS:
            self.display_dict[b] = True, self.model.ball[b].display_list
        self.display_dict['spot'] = True, [s.display_list for s in self.model.spot]
        self.view = View(root, self)

    def draw_line(self):
        self.line_id = self.view.canvas.create_line(50, 50, 200, 200, fill="blue", width=2)

    def center_canvas(self, event=None):
        # TODO consider moving this to View
        self.view.canvas.update_idletasks()
        canvas_width = self.view.canvas.winfo_reqwidth()
        canvas_height = self.view.canvas.winfo_reqheight()
        window_width = self.view.root.winfo_width()
        window_height = self.view.root.winfo_height()

        x_offset = (window_width - canvas_width) // 2
        y_offset = (window_height - canvas_height - self.view.menubar.winfo_height()) // 2

        self.view.canvas.place_configure(x=x_offset, y=y_offset)



