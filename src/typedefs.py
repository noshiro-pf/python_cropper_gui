from collections import namedtuple

Point = namedtuple('Point' , ["x", "y"])
RectSize = namedtuple('RectSize' , ["width", "height"])
Rect = namedtuple('Rect' , ["left", "top", "width", "height"])


def rect_to_xxyy(rect):
    return [
        rect.left,
        rect.left + rect.width,
        rect.top,
        rect.top + rect.height
    ]

def xxyy_to_rect(x1, x2, y1, y2):
    return Rect(
        left = min(x1, x2),
        top = min(y1, y2),
        width = abs(x1 - x2),
        height = abs(y1 - y2)
    )

def rect_from_2points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return xxyy_to_rect(x1, x2, y1, y2)
