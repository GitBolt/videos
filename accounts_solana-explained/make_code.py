from manim import *


def make_code(content, format):
    metadata = Code(
        code=content,
        language=format,
        background="rectangle",
        tab_width=4,
        font_size=18,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(0.8)

    return metadata
