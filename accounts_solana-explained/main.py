from manim import *
from scene1 import IntroScene
from scene2 import LearningScene
from scene3 import AccountStructureCode
from create_table import create_table


class Accounts(Scene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        IntroScene(self)
        LearningScene(self)
        account = AccountStructureCode(self)

        [ex_account, ex_account_table] = create_table(
            [["Field", "Data"],
             ["lamports", "69420"],
             ["owner", "BPFL...1111"],
             ["executable", "true"],
             ["data", "bytedata.bin"],
             ["rent_epoch", "1234"]
             ],
            "Executable Account",
            [0, 0, 0],
            0.5
        )
        ex_account.next_to(account, RIGHT, buff=-0.7)

        [non_ex_account, non_ex_account_table] = create_table(
            [["Field", "Data"],
             ["lamports", "69420"],
             ["owner", "1111..1111"],
             ["executable", "false"],
             ["data", "solami"],
             ["rent_epoch", "1234"]
             ],
            "Non-Executable Account",
            [0, 0, 0],
            0.5
        )
        non_ex_account.next_to(account, LEFT, buff=-0.7)

        self.play(Transform(account, VGroup(
            non_ex_account, ex_account)))
        self.wait()

        rect_nex = SurroundingRectangle(
            non_ex_account_table.get_rows()[1], color=BLUE_C, buff=0.1)
        rect_ex = SurroundingRectangle(
            ex_account_table.get_rows()[1], color=BLUE_C, buff=0.1)

        self.play(Write(non_ex_account_table.add(rect_nex)),
                  Write(ex_account_table.add(rect_ex)))
        self.wait(5)

        for i in range(1, 5):
            new_rect_nex = SurroundingRectangle(
                non_ex_account_table.get_rows()[i+1], color=BLUE_C, buff=0.1)

            new_rect_ex = SurroundingRectangle(
                ex_account_table.get_rows()[i+1], color=BLUE_C, buff=0.1)
            self.play(ApplyMethod(rect_nex.move_to, new_rect_nex),
                      ApplyMethod(rect_ex.move_to, new_rect_ex),
                      run_time=1)
            self.wait(5)

        self.play(FadeOut(non_ex_account), FocusOn(ex_account), run_time=1)
        self.wait(2)

        ethDev = ImageMobject("assets/eth.png").scale(0.1)
        ethDev.move_to(ex_account_table.get_center() + 3 * UP)

        self.play(ApplyMethod(ethDev.shift, 5 * LEFT + 2 * DOWN))
        self.wait(2)

        program_image = ImageMobject("assets/explorer_program.png").scale(1)
        self.add(program_image)
        self.wait()

        rectangle = Rectangle(
            height=0.5,
            width=3,
            stroke_color=WHITE,
            stroke_width=6,
        )
        rectangle.shift([5.3, -0.1, 0])
        self.remove(ethDev)
        self.play(Write(rectangle))

        self.wait()

        self.remove(
            *[mob for mob in self.mobjects],
        )
        self.wait()

        self.play(Write(non_ex_account), run_time=0.8)
        self.wait(2)
