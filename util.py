
def draw_rect(canvas, x1, y1, x2, y2, ):
    canvas.create_rectangle(x1, y1, x2, y2, outline='red', width=1, fill='pink')


def draw_dot(canvas,x, y, dotSize=4, dotColor='red', lineColor='blue', lineWidth=1):
    dx = dotSize/2
    dy = dotSize/2
    canvas.create_oval(x-dx/2, y-dy/2, x+dx/2, y+dy/2, fill=dotColor, width=lineWidth, outline=lineColor)

def draw_roundedrect(canvas, x, y, width, height, radius, lineWidth=1, lineColor='blue', fillColor='lightblue'):
    num_segments = 20  # Number of line segments for each corner

    # Calculate the coordinates for the rounded rectangle
    x1, y1 = x, y
    x2, y2 = x + width, y + height

    points = []  # List to hold the points for the rounded rectangle

    # Top side
    for i in range(num_segments):
        angle = i * (math.pi / 2) / num_segments  # Angle for each segment
        points.extend([
            x1 + radius - radius * math.cos(angle),
            y1 + radius - radius * math.sin(angle)
        ])

    # Right side
    for i in range(num_segments):
        angle = i * (math.pi / 2) / num_segments  # Angle for each segment
        points.extend([
            x2 - radius + radius * math.sin(angle),
            y1 + radius - radius * math.cos(angle)
        ])

    # Bottom side
    for i in range(num_segments):
        angle = i * (math.pi / 2) / num_segments  # Angle for each segment
        points.extend([
            x2 - radius + radius * math.cos(angle),
            y2 - radius + radius * math.sin(angle)
        ])

    # Left side
    for i in range(num_segments):
        angle = i * (math.pi / 2) / num_segments  # Angle for each segment
        points.extend([
            x1 + radius - radius * math.sin(angle),
            y2 - radius + radius * math.cos(angle)
        ])

    # Fill the rounded rectangle by creating a polygon
    canvas.create_polygon(points, outline=lineColor, fill=fillColor, width=lineWidth)



root = tk.Tk()
canvas = tk.Canvas(root, bg='white', height=600, width=800)

canvas.pack()
draw_rect(canvas, 50, 50, 200, 150)
draw_roundedrect(canvas, 250, 250, width=100, height=200, radius=10)
draw_dot(canvas,200, 200, dotSize=5, dotColor='red', lineColor='blue', lineWidth=0)
root.mainloop()