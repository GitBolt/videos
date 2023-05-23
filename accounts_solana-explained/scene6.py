from manim import *
from create_table import create_table


def ProgramAndDataAccount(self: Scene, eth_acc):
    program_account, program_account_t = create_table([
        ["Field", "Data"],
        ["owner", "BPF...11"],
        ["lamports", "10"],
        ["executable", "true"],
        ["data", "byecode.bin"],
    ],

        "Solana Program Account",
        [0, 0, 0],
        0.3
    )
    program_account.shift(UP)

    owner = program_account_t.get_rows()[1]

    data_account, data_account_t = create_table([
        ["Field", "Data"],
        ["owner", "Program Account"],
        ["lamports", "10"],
        ["executable", "false"],
        ["data", "userId: 1"],

    ],            "Solana Data Account",
        [0, 0, 0],
        0.3,

    )
    data = data_account_t.get_rows()[4][1]


    data_account.move_to(eth_acc.get_bottom() * 1.2)

    self.wait(2)

    self.play(eth_acc.animate.shift(UP))
    self.play(Transform(eth_acc, VGroup(program_account, data_account)))

    self.wait(3)
    
    self.play(program_account.animate.move_to(LEFT * 2).scale(1.2), data_account.animate.next_to(
        program_account, RIGHT, buff=0.1).scale(1.2), FadeOut(eth_acc))
    
    self.play(Transform(data, Text("count: 1", font_size=20,
                                   color=GREEN).move_to(data.get_center())))

    self.wait()

    curve_arrow = Arrow(data_account.get_left(), program_account.get_top(),
                        path_arc=90 * DEGREES, color=BLUE_D, stroke_width=3)
    self.play(Create(curve_arrow), run_time=1.6)

    rect_path = SurroundingRectangle(program_account_t)

    dot = Dot(color=GREEN)

    for i in range(1, 10):
        dot.move_to(program_account_t.get_corner(UR))
        self.play(GrowFromCenter(dot), run_time=0.5 if i < 2 else 0.1)

        move_along_animation = MoveAlongPath(
            dot, rect_path, run_time=0.5 if i < 2 else 0.1, rate_func=linear)

        self.play(move_along_animation, run_time=0.5 if i < 2 else 0.3)

        self.play(dot.animate.move_to(RIGHT * 1.3 + DOWN * 0.05),
                  run_time=0.3 if i < 2 else 0.08)

        data.become(Text(f"count: {i+1}", font_size=20,
                    color=random_bright_color()).move_to(data.get_center()))
        self.play(FadeOut(dot), run_time=0.5 if i < 2 else 0.1)

    self.wait(2)

    self.play(Uncreate(curve_arrow))

    self.camera.frame.save_state()
    self.play(
        self.camera.frame.animate.set_width(program_account.get_width()*1.2),
        self.camera.frame.animate.move_to(program_account).scale(0.5),
        owner.animate.set_color(BLUE_C)
    )
    self.wait()

    self.play(Restore(self.camera.frame), owner.animate.set_color(WHITE))
    self.wait()

    image = ImageMobject("assets/native_programs.png")
    image.move_to(DOWN*6.2)  # Position the image at the center of the screen

    # Animate the scrolling effect
    self.play(
        # Move the image to the top of the screen
        image.animate.move_to(UP * 5),
        run_time=5,
    )

    self.wait(1)
    self.remove(image)

