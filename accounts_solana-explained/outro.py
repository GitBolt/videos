from manim import *


def OutroScene(self: Scene):
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
