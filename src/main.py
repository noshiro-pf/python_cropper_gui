from PIL import Image, ImageTk

from typedefs import (
    Point,
    RectSize,
    rect_from_2points
)

from canvas_utils import (
    initialize_window,
    create_canvas_on,
    draw_rect_on
)


IMAGE_FILE = "img/cityscapes_lindau_000057_000019_leftImg8bit.png"



def main():
    # setup gui
    image = Image.open(IMAGE_FILE)
    image_width, image_height = image.size
    window_size = RectSize(width = image_width, height = image_height)
    root = initialize_window(window_size)
    canvas = create_canvas_on(root, window_size, canvas_place=Point(0, 0))
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=image_tk, anchor="nw")

    def draw_rect(rectangle):
        canvas.delete("rect")
        draw_rect_on(
            canvas,
            rectangle,
            fill_color = 'orange',
            stipple = "gray12",
            outline_color = "orange",
            width = 1.0,
            tag = "rect"
        )

    # state
    mouse_left_is_down = False
    rect_begin = Point(0, 0)
    rect_end = Point(0, 0)

    def rect():
        nonlocal rect_begin, rect_end
        return rect_from_2points(rect_begin, rect_end)

    def on_mouse_move(x, y):
        nonlocal mouse_left_is_down, rect_end
        if not mouse_left_is_down: return
        rect_end = Point(x, y)
        draw_rect(rect())

    def on_mouse_left_down(x, y):
        nonlocal mouse_left_is_down, rect_begin, rect_end
        mouse_left_is_down = True
        rect_begin = Point(x, y)
        rect_end = Point(x, y)
        draw_rect(rect())

    def on_mouse_left_up():
        nonlocal mouse_left_is_down
        mouse_left_is_down = False

    root.bind('<Motion>',
      lambda event: on_mouse_move(event.x, event.y)
    )

    root.bind('<Button-1>',
      lambda event: on_mouse_left_down(event.x, event.y)
    )

    root.bind('<ButtonRelease-1>',
      lambda event: on_mouse_left_up()
    )

    root.mainloop()


if __name__ == '__main__':
    main()
    