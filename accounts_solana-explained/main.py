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
from scene10 import BurnIntro


class Accounts(MovingCameraScene):
    def construct(self):
        Text.set_default(font="Cantarell", font_size=50)

        IntroScene(self)
        LearningScene(self)
        account = AccountStructureCode(self)
        TwoAccountDesc(self, account)

        eth_acc, _ = RunSOLAccountsToEth(self)
        ProgramAndDataAccount(self, eth_acc)

        AccountCreation(self)
        RentIntro(self)
        TokenAccounts(self)
        BurnIntro(self)

        self.remove(*[obj for obj in self.mobjects])

        twitter_logo = SVGMobject("assets/twitter.svg").scale(0.5)
        twitter_logo.move_to(LEFT * 1.5)
        twitter = Text("0xBolt", color=BLUE, font_size=60, weight=BOLD)
        twitter.next_to(twitter_logo, RIGHT)
        self.play(FadeIn(twitter), Write(twitter_logo))

        feedback = Text("Feedback pls", font_size=35)
        feedback.next_to(twitter, DOWN, buff=0.5)
        self.wait(1)
        self.add(feedback)
        self.wait(2)
