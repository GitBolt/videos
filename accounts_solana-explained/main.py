from manim import *
from scene1 import IntroScene
from scene2 import LearningScene
from scene3 import AccountStructureCode
from scene4 import TwoAccountDesc
from scene5 import RunSOLAccountsToEth
from scene6 import ProgramAndDataAccount
from scene7 import AccountCreation
from scene8 import RentIntro
from scene9 import TokenAccounts

from create_table import create_table
from make_code import make_code


class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        # IntroScene(self)
        # LearningScene(self)
        # account = AccountStructureCode(self)
        # TwoAccountDesc(self, account)

        # eth_acc, _ = RunSOLAccountsToEth(self)
        # ProgramAndDataAccount(self, eth_acc)

        # AccountCreation(self)
        # RentIntro(self)
        # TokenAccounts(self)

        title = Text("Closing Accounts", font_size=60)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(Uncreate(title), run_time=2)

        self.wait(1)

        [account, _] = create_table(
            [["Field", "Data"],
             ["lamports", "1336320"],
             ["data", "64_bytes.bin"],
             ["owner", "1111..1111"],
             ["executable", "false"],
             ["rent_epoch", "1234"]
             ],
            "Your Account"
        )
        self.play(DrawBorderThenFill(account), run_time=0.8)

        self.wait()

        code = make_code(
            """
            spl-token close skG...RTE
            """,
            "python"
        )

        code.move_to(RIGHT * 3)

        self.play(account.animate.move_to(LEFT * 3), Write(code))

        arrow = Arrow(code.get_left(), account.get_right())
        self.play(GrowArrow(arrow),
                  path_arc=20*DEGREES,
                  stroke_width=3,
                  max_tip_length_to_length_ratio=0.1)

        self.wait()

        self.play(arrow.animate.set_color(RED), run_time=0.2)
        self.play(Unwrite(account), run_time=0.8)

        sol = Text("+ 0.00133632 SOL", color=GREEN, font_size=30, weight=BOLD)
        sol.move_to(account.get_center())
        self.play(Create(sol))
        self.wait(4)

