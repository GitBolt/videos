from manim import *
from create_table import create_table


def LearningScene(self: Scene):

    [account_table, _] = create_table(
        [["Field", "Data"],
         ["lamports", "100020"],
         ["owner", "1111..1111"],
         ["executable", "true"],
         ["data", "..."],
         ["rent_epoch", "1234"]
         ],
        "Account 1",
        [-4.5, 0, 0]
    )

    self.play(Create(account_table))
    self.wait()

    code = Code(
        code="SystemProgram::CreateAccount",
        language="rust",
        background="rectangle",
        tab_width=4,
        font_size=10,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.3)

    code.next_to(account_table, RIGHT, buff=0.5)
    self.play(Write(code), run_time=0.5)
    self.wait()

    [account_table2, _] = create_table(
        [["Field", "Data"],
         ["lamports", "69420"],
         ["owner", "1111..1111"],
         ["executable", "false"],
         ["data", "solami"],
         ["rent_epoch", "1234"]
         ],
        "Account 2"
    )

    account_table2.next_to(code, RIGHT, buff=0.5)
    self.play(Create(account_table2))


    curve_arrow = Arrow(account_table.get_top(), account_table2.get_top(),
                        path_arc=-50 * DEGREES, color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.03)

    self.play(Create(curve_arrow), run_time=1.6)

    self.wait(2)
    self.remove(curve_arrow, account_table, account_table2, code)
