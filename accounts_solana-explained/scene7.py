from manim import *


def AccountCreation(self: Scene):
    code = Code(
        code="Keypair.generate()",
        language="typescript",
        background="rectangle",
        tab_width=4,
        font_size=15,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.3)

    self.play(Write(code), run_time=0.8)

    self.play(code.animate.move_to(UP*2))

    pubKeyTitle = Text("Public Key / Wallet", font_size=25, color=BLUE_C)
    pubKey = Text("Am5A...f6rWd (32 Bytes)", font_size=25)

    pubKey.next_to(pubKeyTitle.get_bottom(), DOWN, buff=0.2)

    pubKeyGroup = VGroup(pubKeyTitle, pubKey)

    pubKeyGroup.next_to(code, DOWN * 1.5 + LEFT * 1.5, buff=0.2)

    curve_arrow = Arrow(code.get_left(), pubKeyGroup.get_top(),
                        path_arc=90 * DEGREES, color=BLUE_D, stroke_width=3)

    self.play(Write(pubKeyGroup), Create(curve_arrow))

    self.wait()

    privKeyTitle = Text("Private Key", font_size=25, color=BLUE_C)
    privKey = Text("4TzW...8GKpD (64 Bytes)", font_size=25)

    privKey.next_to(privKeyTitle.get_bottom(), DOWN, buff=0.2)

    privKeyGroup = VGroup(privKeyTitle, privKey)

    privKeyGroup.next_to(code, DOWN * 1.5 + RIGHT * 1.5, buff=0.2)

    curve_arrow2 = Arrow(code.get_right(), privKeyGroup.get_top(),
                         path_arc=-90 * DEGREES, color=BLUE_D, stroke_width=3)

    self.play(Write(privKeyGroup), Create(curve_arrow2))

    self.wait()

    code2 = Code(
        code="SystemProgram::CreateAccount",
        language="rust",
        background="rectangle",
        tab_width=4,
        font_size=15,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.3)
    code2.move_to(DOWN*2)

    curve_arrow2 = Arrow(pubKeyGroup.get_right(), code2.get_top(),
                         path_arc=-90 * DEGREES, color=BLUE_D, stroke_width=3)

    self.play(Write(code2), Create(curve_arrow2))
    self.wait()

    solana = SVGMobject(file_name="assets/solana.svg",
                        fill_color=WHITE).scale(0.3)
    solanaAmount = Text("1000", font_size=25, color=WHITE)
    solanaAmount.move_to(solana.get_right() * 2.1)
    lamportGroup = Group(solana, solanaAmount)
    lamportGroup.move_to(LEFT * 5 + DOWN * 2)
    self.play(Write(solana), Write(solanaAmount), run_time=0.9)

    self.play(lamportGroup.animate.move_to(code2.get_left()).scale(0.1))
    self.remove(lamportGroup)

    self.wait()

    space = Text("32 Bytes", font_size=25, color=WHITE)
    space.move_to(LEFT * 5 + DOWN * 2)
    self.play(Write(space), run_time=0.9)

    self.play(space.animate.move_to(code2.get_left()).scale(0.1))
    self.remove(space)

    self.wait()

    self.remove(*[obj for obj in self.mobjects])
