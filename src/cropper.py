from PIL import Image, ImageTk

from canvas_utils import create_canvas_on, draw_rect_on, initialize_window
from typedefs import Point, RectSize, rect_from_2points

IMAGE_FILE = "img/cat_illust_small.png"


def main():
    # setup gui
    image = Image.open(IMAGE_FILE)
    image_width, image_height = image.size
    window_size = RectSize(width=image_width, height=image_height)
    window = initialize_window(window_size)
    canvas = create_canvas_on(window, window_size, canvas_place=Point(0, 0))
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=image_tk, anchor="nw")

    def draw_rect(rectangle):
        canvas.delete("rect")
        draw_rect_on(
            canvas,
            rectangle,
            fill_color="orange",
            stipple="gray12",
            outline_color="orange",
            width=1.0,
            tag="rect",
        )

    # state
    rect_begin = Point(0, 0)
    rect_end = Point(0, 0)

    def on_mouse_left_down(x, y):
        nonlocal rect_begin, rect_end
        rect_begin = Point(x, y)
        rect_end = Point(x, y)
        draw_rect(rect_from_2points(rect_begin, rect_end))

    def on_mouse_move(x, y):
        nonlocal rect_begin, rect_end
        rect_end = Point(x, y)
        draw_rect(rect_from_2points(rect_begin, rect_end))

    window.bind("<Button-1>", lambda ev: on_mouse_left_down(ev.x, ev.y))
    window.bind("<B1-Motion>", lambda ev: on_mouse_move(ev.x, ev.y))

    window.mainloop()


if __name__ == "__main__":
    main()
