import tkinter as tk

from typedefs import rect_to_xxyy


def initialize_window(window_size):
    root = tk.Tk() # create window
    width, height = window_size
    root.geometry("{}x{}".format(width, height)) # set window size
    return root

def create_canvas_on(root, canvas_size, *, canvas_place):
    width, height = canvas_size
    canvas = tk.Canvas(root, width = width, height = height) # create canvas
    x, y = canvas_place
    canvas.place(x = x, y = y)
    return canvas

def draw_rect_on(canvas, rect, *, fill_color, stipple, outline_color, width, tag):
    x1, x2, y1, y2 = rect_to_xxyy(rect)
    canvas.create_rectangle(
        x1, y1, x2, y2,
        fill = fill_color,
        stipple = stipple,
        outline = outline_color,
        width = width,
        tag = tag
    )
