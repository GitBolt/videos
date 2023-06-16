from manim import *
from create_table import create_table, create_table_progress


def RentIntro(self: Scene):
    map = ImageMobject("assets/validator_map.png")

    source = Text("Source: Validators.app", color=WHITE, font_size=30, weight=BOLD)
    source.move_to(UP * 1)

    self.play(FadeIn(map), Write(source), run_time=0.5)

    self.camera.frame.save_state()
    self.play(self.camera.frame.animate.scale(0.5).move_to([-3, 1, 0]), run_time=2)
    self.play(self.camera.frame.animate.move_to([3, 1, 0]), run_time=1.5)
    self.play(self.camera.frame.animate.move_to([3.5, -1, 0]), run_time=1.5)

    self.play(Restore(self.camera.frame))

    self.wait(2)
    self.play(FadeOut(map), FadeOut(source), run_time=1)

    title = Text("Rent", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("8. Rent", color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,  # Total duration of the animation
    )


    rent, rent_t = create_table(
        [
            ["Field", "Data"],
            ["lamports", "35"],
            ["data", "1 byte"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "Account Rent",
        [0, 0, 0],
        0.5,
    )
    rent_value = Text("Rent: 0", color=PINK, font_size=32, weight=BOLD)
    disclaimer = Text("*not actual rent values", font_size=20)

    rent_value.next_to(rent, RIGHT * 2)
    disclaimer.move_to([4.3, -0.25, 0])

    self.play(Create(rent))

    self.wait(2)

    data = rent_t.get_rows()[2][1]

    arrow = Arrow(
        start=DOWN,
        end=UP,
        stroke_width=7,
        color=PINK,
        max_tip_length_to_length_ratio=0.2,
    ).next_to(data, RIGHT * 3.5)

    self.play(Write(arrow), Write(rent_value), data.animate.set_color(BLUE))

    x = ValueTracker(0)

    rent_value.add_updater(
        lambda z: z.become(
            Text(
                "Rent: " + str(round(x.get_value() * 0.00003784, 5)) + " SOL",
                color=PINK,
                font_size=32,
                weight=BOLD,
            )
        ).next_to(rent, RIGHT * 2)
    )

    data.add_updater(
        lambda z: z.become(
            Text(
                str(round(x.get_value())) + " bytes", font_size=23, color=BLUE
            ).move_to(data.get_center())
        )
    )

    self.add(disclaimer)
    self.play(x.animate.set_value(64), run_time=5, run_func=slow_into)
    self.wait()
    self.camera.frame.save_state()
    self.play(
        self.camera.frame.animate.move_to(RIGHT * 5).scale(1.3),
        Uncreate(disclaimer),
        Uncreate(arrow),
        Uncreate(rent_value),
    )

    self.wait()

    code = Code(
        code="""
        > solana rent 0
        
        Rent-exempt minimum: 0.00089088 SOL

        """,
        language="typescript",
        background="rectangle",
        tab_width=4,
        font_size=15,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.4)

    code.move_to(RIGHT * 8)
    self.play(Write(code))

    self.wait(2)
    data.clear_updaters()
    self.play(Restore(self.camera.frame), Uncreate(code))

    rent2, rent2_t = create_table_progress(
        [
            ["Field", "Data"],
            ["lamports", "35"],
            ["data", "64 bytes"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "Account Rent",
        [0, 0, 0],
        0.5,
    )

    lamports = rent2_t.get_rows()[1][1]

    progress_bar = rent2[0]
    initial_start = progress_bar.get_left()

    # self.play(Transform(rent, rent2))
    self.play(FadeOut(rent), FadeIn(rent2), lamports.animate.set_color(BLUE))

    x = ValueTracker(progress_bar.get_right()[0])

    dot = Dot(color=LIGHT_PINK)
    dot.move_to(progress_bar.get_right())

    self.play(GrowFromCenter(dot))

    dot.add_updater(lambda z: z.set_x(x.get_value()))

    lamports.add_updater(
        lambda z: z.become(
            Text(str(round(x.get_value() * 10) + 19), font_size=23).move_to(
                lamports.get_center()
            )
        )
    )

    progress_bar.add_updater(
        lambda z: z.become(Line(color=PINK, start=initial_start, end=dot.get_center()))
    )

    self.play(
        x.animate.set_value(rent2[1].get_left()[0] + 0.25), run_time=3, rate_func=linear
    )

    self.play(Uncreate(rent2), FadeOut(dot), Uncreate(title), run_time=2)
    self.wait(2)
