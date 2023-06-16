from manim import *
from create_table import create_table


def ProgramAndDataAccount(self: Scene, eth_acc):
    program_account, program_account_t = create_table(
        [
            ["Field", "Data"],
            ["owner", "BPF...11"],
            ["lamports", "10"],
            ["executable", "true"],
            ["data", "byecode.bin"],
        ],
        "Solana Program  Account",
        [0, 0, 0],
        0.3,
    )
    program_account.shift(UP * 1.2)

    owner = program_account_t.get_rows()[1]

    data_account, data_account_t = create_table(
        [
            ["Field", "Data"],
            ["owner", "Program"],
            ["lamports", "1000000"],
            ["executable", "false"],
            ["data", "some_data: 69.420"],
        ],
        "Solana Data Account",
        [0, 0, 0],
        0.3,
    )
    data = data_account_t.get_rows()[4][1]

    data_account.move_to(DOWN * 2)

    self.wait(2)

    self.play(eth_acc.animate.shift(UP))
    self.play(Transform(eth_acc, VGroup(program_account, data_account)))

    self.wait(3)

    self.play(
        program_account.animate.move_to(LEFT * 2).scale(1.2),
        data_account.animate.next_to(
            program_account, RIGHT, buff=0.1).scale(1.2),
        FadeOut(eth_acc),
    )

    self.wait()

    curve_arrow = Arrow(
        data_account.get_left(),
        program_account.get_top(),
        path_arc=90 * DEGREES,
        color=BLUE_D,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.05,
    )
    self.play(Create(curve_arrow), run_time=1.6)

    rect_path = SurroundingRectangle(program_account_t)

    circle = Circle(color=GREEN, fill_opacity=0.4, radius=0.5)
    caption = Text("*Blink represents code executing from program", font_size=20)
    caption.to_edge(DL)
    for i in range(1, 10):
        circle.move_to(program_account_t.get_corner(UR))
        self.play(GrowFromCenter(circle), run_time=0.5 if i < 3 else 0.1)

        data.become(
            Text(f"some_data: {round(i*PI, 2)}", font_size=22, color=GREEN).move_to(
                data.get_center()
            )
        )
        self.play(FadeOut(circle), run_time=0.5 if i < 3 else 0.1)

        data.become(
            Text(f"some_data: {round(i*PI, 2)}", font_size=20, color=WHITE).move_to(
                data.get_center()
            )
        )

        if (i == 2):
            self.add(caption)
        self.wait(1 if i < 3 else 0.2)
    self.wait(2)

    self.play(Uncreate(curve_arrow))

    self.camera.frame.save_state()
    self.play(
        self.camera.frame.animate.set_width(program_account.get_width() * 1.2),
        self.camera.frame.animate.move_to(program_account).scale(0.5),
        owner.animate.set_color(BLUE_C),
    )
    self.wait(2)

    self.play(Restore(self.camera.frame), owner.animate.set_color(WHITE))
    self.wait()

    image = ImageMobject("assets/native_programs.png")
    image.move_to(DOWN * 6.2)
    self.play(FadeIn(image))

    self.play(
        image.animate.move_to(UP * 5),
        run_time=5,
    )
    self.wait(1)
    self.remove(*[obj for obj in self.mobjects])
    self.play(FadeOut(image))
