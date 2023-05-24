from manim import *
from create_table import create_table
from make_code import make_code


def BurnIntro(self: Scene):
    title = Text("Closing Accounts", font_size=60)
    self.play(FadeIn(title))
    self.wait(2)
    self.play(Uncreate(title), run_time=2)

    self.wait(1)

    [account, _] = create_table(
        [
            ["Field", "Data"],
            ["lamports", "1336320"],
            ["data", "64_bytes.bin"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "Your Account",
    )
    self.play(DrawBorderThenFill(account), run_time=0.8)

    code = make_code(
        """
        spl-token close skG...RTE
        """,
        "python",
    )

    code.move_to(RIGHT * 3)

    self.play(account.animate.move_to(LEFT * 3), Write(code))

    arrow = Arrow(code.get_left(), account.get_right())
    self.play(
        GrowArrow(arrow),
        path_arc=20 * DEGREES,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.1,
    )

    self.play(arrow.animate.set_color(RED), run_time=0.2)
    self.play(Unwrite(account), run_time=0.8)

    sol = Text("+ 0.00133632 SOL", color=GREEN, font_size=30, weight=BOLD)
    sol.move_to(account.get_center())
    self.play(Create(sol), arrow.animate.set_color(GREEN))

    self.play(Uncreate(arrow), Uncreate(code), Uncreate(account), Uncreate(sol))
    self.wait(1)
    wallet = RoundedRectangle(
        width=3,
        height=5,
        fill_color="#21252E",
        fill_opacity=1,
        stroke_width=2,
        stroke_color="#363B44",
        corner_radius=0.1,
    )
    wallet_label = Text("Some Wallet", font_size=24).next_to(wallet, UP)
    self.play(Create(wallet), Write(wallet_label))

    scam_nft = Rectangle(
        width=2,
        height=2.5,
        fill_color=["#5AB543", "#6B91B5", "#53A62C"],
        fill_opacity=1,
        stroke_width=0,
    ).scale(0.6)

    scam_nft.next_to(wallet.get_left(), LEFT * 7)
    scam_title = Text("Scam NFT #0000", font_size=15)

    scam_title.next_to(scam_nft, DOWN)
    self.play(Create(scam_nft), Create(scam_title))

    self.wait(2)

    burn_button = Rectangle(
        width=2, height=0.5, fill_color=RED, fill_opacity=1, stroke_width=0
    )
    burn_button.move_to(wallet.get_center())
    burn_button.move_to(UP * 2)

    burn_text = Text("Burn", font_size=15, weight=BOLD)
    burn_text.move_to(burn_button.get_center())

    self.play(
        scam_nft.animate.move_to(wallet.get_center()).move_to(DOWN * 0.3).scale(1.8),
        scam_title.animate.move_to(wallet.get_bottom()).move_to(DOWN * 2).scale(1.5),
        Write(burn_button),
        Write(burn_text),
    )

    self.wait(1)

    fire_icon = SVGMobject("assets/burn.svg")
    self.play(
        burn_button.animate.scale(0.9), burn_text.animate.scale(0.9), run_time=0.7
    )
    self.play(
        burn_button.animate.scale(1.2),
        Transform(scam_nft, fire_icon),
        Transform(
            scam_title,
            Text("+ 0.00203 SOL", color=GREEN, font_size=25, weight=BOLD).move_to(
                scam_title.get_center()
            ),
        ),
    )

    self.wait(6)

    self.play(*[FadeOut(obj) for obj in self.mobjects])
    tables = []
    for i in range(1, 7):
        table, _ = create_table(
            [
                ["Field", "Data"],
                ["lamports", "69420"],
                ["data", "metadata"],
                ["owner", "Token...5DA"],
                ["executable", "false"],
                ["rent_epoch", "1234"],
            ],
            "Scam NFT Account " + " " + str(i),
            [0, 0, 0],
            0.2,
        )
        table[2].scale(0.6)
        table.move_to(UP * 2)
        tables.append(table)

    # Create button
    button = RoundedRectangle(
        width=2.5,
        height=0.8,
        corner_radius=0.2,
        fill_color=RED,
        stroke_width=0,
        fill_opacity=1,
    )
    button.move_to(LEFT * 5)
    button_text = Text("Close Account", color=WHITE, font_size=25, weight=BOLD)
    button_text.move_to(button.get_center())
    self.add(button, button_text)

    for idx, table in enumerate(tables):
        if idx + 1 <= 3:
            table.move_to([1, -2.5 + idx * 2.5, 0])
        else:
            table.move_to([4, -2.5 + (idx - 3) * 2.5, 0])

        self.play(FadeIn(table), run_time=0.3)

    arrows = []
    for table in tables:
        arrow = Arrow(
            start=button.get_right(),
            end=table.get_center(),
            color=WHITE,
        )
        arrows.append(arrow)

    for arrow, table in zip(arrows, tables):
        burn = SVGMobject("assets/burn.svg")
        burn.move_to(table.get_center())
        self.play(GrowArrow(arrow), Transform(table, burn), run_time=0.4)
        self.play(Uncreate(arrow), run_time=0.3)

    self.play(
        *[FadeOut(obj) for obj in self.mobjects],
        Write(Text("Cleared Storage", color=GREEN, font_size=50, weight=BOLD))
    )
    self.wait(3)
