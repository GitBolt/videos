from manim import *
from create_table import create_table


def SpaceScene(self: Scene):
    title = Text("Space", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("7. Space",
                   color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,
    )

    self.wait(3)

    