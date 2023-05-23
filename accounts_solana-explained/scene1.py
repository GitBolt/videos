from manim import *


def IntroScene(self: Scene):
    tx1 = Text("Everything in Solana")
    tx2 = Text("Everything", font_size=60)
    tx3 = Text("is an Account")

    self.play(Write(tx1), run_time=1.2)
    self.play(FadeOut(tx1), run_time=0.5)
    self.wait(0.8)

    self.play(ScaleInPlace(tx2, 2), run_time=0.1)
    self.wait()
    self.play(FadeOut(tx2), run_time=0.1)

    self.play(FadeIn(tx3))
    self.wait()
    self.play(FadeOut(tx3), run_time=0.1)

    account_image = ImageMobject("assets/explorer_account.png").scale(1)
    self.add(account_image)
    self.wait()

    rectangle = Rectangle(
        height=0.8,
        width=3,
        stroke_color=WHITE,
        stroke_width=5,
    )
    rectangle.shift([-5.3, 2.4, 0])
    self.play(Write(rectangle))

    point = Dot(color=WHITE)
    point.move_to(rectangle.get_right() + RIGHT * 0.1)

    line = Line(point.get_center(), point.get_center() + RIGHT * 4)
    line.set_color(WHITE)

    self.play(
        FadeIn(point),
        Write(line),
        run_time=1
    )

    what = Text("What?")
    what.next_to(line.get_end(), RIGHT, buff=0.5)
    self.play(Write(what), run_time=0.5)
    self.wait()

    self.remove(account_image, line, point, what, rectangle)
    self.wait()
