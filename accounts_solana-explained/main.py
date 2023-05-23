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


class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        IntroScene(self)
        LearningScene(self)
        account = AccountStructureCode(self)
        TwoAccountDesc(self, account)


        eth_acc, _ = RunSOLAccountsToEth(self)
        ProgramAndDataAccount(self, eth_acc)
        self.wait()

        AccountCreation(self)
        RentIntro(self)
        self.wait(2)

        TokenAccounts(self)
