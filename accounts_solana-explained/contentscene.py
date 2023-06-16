from manim import *


def ContentScene(self: Scene):
    title = Text("Video Content", font_size=48, color=WHITE)
    self.play(Create(title), run_time=1.5)
    self.wait()

    content = [
        "1. Account structure",
        "2. Types of accounts",
        "3. Comparison with Ethereum",
        "4. Program Account Example",
        "5. Creating Accounts",
        "6. Token Accounts",
        "7. Space",
        "8. Rent",
        "9. Closing Accounts"
    ]

    self.play(title.animate.move_to(UP * 3.5), run_time=0.6)

    for index, item in enumerate(content):
        content_item = Text(f"{item}", font_size=32, color=BLUE_C)

        content_item.next_to(title, DOWN * 2.5 + LEFT * 1, aligned_edge=LEFT)

        self.play(FadeIn(content_item), run_time=0.2)
        self.play(content_item.animate.shift(
            RIGHT * 2.5 + DOWN * (index / 1.5)), run_time=0.3)
        self.wait(0.2)

    self.wait(2)
    self.remove(*[obj for obj in self.mobjects])
