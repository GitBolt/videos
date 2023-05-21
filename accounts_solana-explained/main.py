from manim import *
import random
import string
from scene1 import IntroScene
from scene2 import LearningScene
from scene3 import AccountStructureCode
from scene4 import TwoAccountDesc
from create_table import create_table
import secrets
import hashlib


rand = ["random1", "random2", "random3", "random4", "random5"]


class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        # IntroScene(self)
        # LearningScene(self)
        # account = AccountStructureCode(self)
        # non_ex_account = TwoAccountDesc(self, account)

        # self.play(Write(non_ex_account), run_time=0.8)
        # self.wait(2)

        # Add Non Ex Details First

        ex, ext = create_table([["Field", "Data"],
                                ["lamports", "69420"],
                                ["data", "bytedata.bin"],
                                ["owner", "BPFL...1111"],
                                ["executable", "true"],
                                ["rent_epoch", "1234"]],
                               "Exectuable Account",
                               [-2.5, 0, 0]
                               )

        self.play(Create(ex), run_time=1)

        data_field = ext.get_rows()[2][1]

        nex, next = create_table([["Field", "Data"],
                                  ["lamports", "69420"],
                                  ["data", "solami"],
                                  ["owner", "1111..1111"],
                                  ["executable", "false"],
                                  ["rent_epoch", "1234"]],
                                 "Non-Exectuable Account")

        nex.next_to(ex, buff=0.6)
        self.play(Create(nex), run_time=1)

        data_field2 = next.get_rows()[2][1]

        circle = Circle(radius=0.1, color=GREEN)
        circle.move_to(ex[1].get_corner(UR))
        self.play(Create(circle))

        path_animation = MoveAlongPath(circle, ex[1], run_time=2)
        self.play(path_animation.always())

        table = ex[1]  # Assuming ex[1] represents the table object

        code = Code(
            file_name="codeblocks/instruction_execution.rs",
            background="rectangle",
            tab_width=4,
            font_size=10,
            corner_radius=0.1,
            background_stroke_width=0,
            insert_line_no=False,
            style="dracula",
        ).scale(1.5)

        code.move_to([0, 3, 0])

        self.play(ApplyMethod(code.move_to, [0, 0, 0]), run_time=0.5)
        self.play(Transform(code, data_field), run_time=0.7)

        self.play(self.camera.frame.animate.scale(2))

        self.wait()
