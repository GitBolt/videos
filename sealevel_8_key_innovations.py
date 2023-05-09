from manim import *

class NewPublicKey(Scene):
    def construct(self):
        Text.set_default(font="Hack", font_size=50)

        public_key = Text("New Public Key:", font_size=30)
        public_key.move_to(UP * 2)

        key = Text("T47T7NzrcKUTwVf8uSk6dPHV7Goy9XzLJjg4m4n1fQn", font_size=24)
        key.next_to(public_key, DOWN)

        self.play(Write(public_key))
        self.play(Write(key))