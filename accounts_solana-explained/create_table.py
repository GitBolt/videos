from manim import *


def create_table(table_data, title, move_to=[0, 0, 0], scale=0.4):
    table = Table(table_data, line_config={
        "stroke_width": 1, "color": GRAY_C}, include_outer_lines=True
    )
    table.scale(scale)
    table.add_highlighted_cell((1, 1), color="#163A70")
    table.add_highlighted_cell((1, 2), color="#163A70")
    table.move_to(move_to)

    box = SurroundingRectangle(
        table, buff=0.2, color=WHITE, fill_opacity=0.02, corner_radius=0.2)
    box.set_stroke(width=0)

    title = Text(title, font_size=22, color=WHITE)
    title.next_to(box.get_top(), UP, buff=0.3)

    table_group = VGroup(table, box, title)

    return [table_group, table]
