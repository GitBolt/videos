from manim import *
from scene1 import IntroScene
from scene3 import AccountStructureCode
from scene4 import TwoAccountDesc
from scene5 import RunSOLAccountsToEth
from scene6 import ProgramAndDataAccount
from scene7 import AccountCreation
from scene8 import RentIntro
from scene9 import TokenAccounts
from scene10 import BurnIntro
from contentscene import ContentScene
from counter_example import CounterExample
from space_scene import SpaceScene
from outro import OutroScene

class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        IntroScene(self)
        ContentScene(self)
        account = AccountStructureCode(self)
        TwoAccountDesc(self, account)

        eth_acc, _ = RunSOLAccountsToEth(self)
        ProgramAndDataAccount(self, eth_acc)
        
        CounterExample(self)
        
        AccountCreation(self)
        TokenAccounts(self)

        SpaceScene(self)
        RentIntro(self)
        BurnIntro(self)
        OutroScene(self)