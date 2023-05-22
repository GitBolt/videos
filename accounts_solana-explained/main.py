from manim import *
from create_table import create_table

from scene1 import IntroScene
from scene2 import LearningScene
from scene3 import AccountStructureCode
from scene4 import TwoAccountDesc
from scene5 import RunSOLAccountsToEth
from scene6 import ProgramAndDataAccount
from scene7 import AccountCreation

class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        IntroScene(self)
        LearningScene(self)
        account = AccountStructureCode(self)
        non_ex_account = TwoAccountDesc(self, account)

        self.play(Write(non_ex_account), run_time=0.8)
        self.wait(2)

        # Add Non Ex Details First
        self.play(Uncreate(non_ex_account))

        eth_acc, eth_acc_t = RunSOLAccountsToEth(self)
        ProgramAndDataAccount(self, eth_acc)
        self.wait()

        AccountCreation(self)