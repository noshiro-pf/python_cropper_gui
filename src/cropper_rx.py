import rx
from rx import operators as ops
from PIL import Image, ImageTk

from canvas_utils import create_canvas_on, draw_rect_on, initialize_window
from typedefs import Point, RectSize, rect_from_2points

IMAGE_FILE = "img/cat_illust_small.png"


def createMouseEventStream(window, event_name: str):
    stream = rx.Subject()
    window.bind(event_name, lambda ev: stream.on_next(Point(ev.x, ev.y)))
    return stream


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
    mouse_left_click = createMouseEventStream(window, "<Button-1>")
    mouse_left_drag = createMouseEventStream(window, "<B1-Motion>")
    rect_begin = mouse_left_click
    rect_end = rx.merge(mouse_left_drag, mouse_left_click)
    rect = rx.combine_latest(rect_begin, rect_end).pipe(
        ops.map(lambda tpl: rect_from_2points(*tpl))
    )

    rect.subscribe(draw_rect)

    window.mainloop()


if __name__ == "__main__":
    main()
