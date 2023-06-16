from manim import *
from create_table import create_table


def CounterExample(self: Scene):
    title = Text("Program Account Example", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("4. Program Account Example",
                   color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,
    )

    self.wait(3)

    code = Code(
        file_name="codeblocks/counter_program.rs",
        background="rectangle",
        tab_width=4,
        font_size=10,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.5)

    code.move_to(DOWN * 1.5)
    self.play(Write(code))
    self.wait(2)
    self.play(code.animate.move_to(UP * 1), run_time=1.5)
    self.wait(2)

    def code_zoom(mob):
        mob.scale(2)
        mob.move_to(RIGHT * 5)
        return mob

    self.play(ApplyFunction(code_zoom, code))
    highlight = Rectangle(
        fill_opacity=0.2,
        stroke_width=0,
        color=BLACK,
        width=7,
        height=2.3

    ).shift(LEFT * 3.3 + DOWN * 0.5)

    self.play(Create(highlight))
    self.wait(1)
    self.play(
        Uncreate(highlight)
    )

    def code_zoom_out(mob):
        mob.scale(0.8)
        mob.move_to(DOWN * 4 + RIGHT * 1.8)
        return mob

    def code_zoom_out_full(mob):
        mob.scale(0.3)
        return mob

    self.play(ApplyFunction(code_zoom_out, code),
              )
    self.wait(2)
    self.play(ApplyFunction(code_zoom_out_full, code), Uncreate(code))

    program_account, program_account_t = create_table(
        [
            ["Field", "Data"],
            ["owner", "BPF...11"],
            ["lamports", "10000"],
            ["executable", "true"],
            ["data", "code.bin"],
        ],
        "Counter Program  Account",
        [0, 0, 0],
        0.5,
    )
    program_account.shift(LEFT * 4)

    data_account, data_account_t = create_table(
        [
            ["Field", "Data"],
            ["owner", "Program"],
            ["lamports", "10000"],
            ["executable", "false"],
            ["data", "count: 0"],
        ],
        "Counter Data Account",
        [0, 0, 0],
        0.5,
    )
    data = data_account_t.get_rows()[4][1]

    data_account.next_to(program_account, RIGHT, buff=3)

    self.play(Write(data_account))
    self.wait(2)
    self.play(Create(program_account))

    self.wait(3)

    code2 = Code(
        code="increment()",
        language="rust",
        background="rectangle",
        tab_width=4,
        font_size=15,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.3)
    code2.move_to(program_account_t.get_center() + DOWN * 2.5)

    for i in range(1, 10):
        self.play(FadeIn(code2), run_time=0.5 if i < 3 else 0.1)

        data.become(
            Text(f"count: {i + 1}", font_size=25, color=GREEN).move_to(
                data.get_center()
            )
        )
        self.play(FadeOut(code2),
                  run_time=0.5 if i < 3 else 0.1)

        data.become(
            Text(f"count: {i + 1}", font_size=23, color=WHITE).move_to(
                data.get_center()
            )
        )

        self.wait(1 if i < 3 else 0.2)
    self.wait(2)
    curve_arrow = Arrow(
        data_account.get_left() + UP * 0.2,
        program_account.get_top(),
        path_arc=90 * DEGREES,
        color=BLUE_D,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.05,
    )
    self.play(Create(curve_arrow), run_time=1.6)

    self.wait(2)

    self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=3)
    self.wait(2)
