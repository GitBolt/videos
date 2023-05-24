from manim import *
from create_table import create_table
import random


random_data = [
    "userid: 1",
    "count: 2",
    "tweet: 69",
    "content",
    "12/7/2006",
    "active: false",
]


def RunSOLAccountsToEth(self: MovingCamera):
    ex, ext = create_table(
        [
            ["Field", "Data"],
            ["lamports", "69420"],
            ["data", "bytedata.bin"],
            ["owner", "BPFL...1111"],
            ["executable", "true"],
            ["rent_epoch", "1234"],
        ],
        "Exectuable Account (Program)",
        [-2.5, 0, 0],
    )

    self.play(Create(ex), run_time=1)
    data_field = ext.get_rows()[2][1]

    nex, next = create_table(
        [
            ["Field", "Data"],
            ["lamports", "69420"],
            ["data", "solami"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "Non-Exectuable Account (Data)",
    )

    nex.next_to(ex, buff=0.6)
    self.play(Create(nex), run_time=1)

    self.wait(1)

    dot = Dot(color=GREEN)
    dot.move_to(ext.get_corner(UR))
    self.play(GrowFromCenter(dot))

    rect_path = SurroundingRectangle(ext)

    code = Code(
        file_name="codeblocks/instruction_execution.rs",
        background="rectangle",
        tab_width=4,
        font_size=10,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1.5)

    code.move_to([2, 7, 0])

    move_along_animation = MoveAlongPath(dot, rect_path, run_time=10, rate_func=linear)

    self.play(move_along_animation, run_time=2)

    self.add(code)

    self.play(
        ApplyMethod(code.move_to, [-2.5, 0, 0]),
        move_along_animation,
        run_time=2,
    )
    self.wait(0.1)
    self.play(Transform(code, data_field), move_along_animation, run_time=0.6)

    data_field2 = next.get_rows()[2][1]

    elapsed_time = 0
    delay = 0.3

    def update_text(obj, dt):
        nonlocal elapsed_time
        elapsed_time += dt
        if elapsed_time >= delay:
            obj.become(
                Text(random.choice(random_data), font_size=20).move_to(
                    data_field2.get_center()
                )
            )
            elapsed_time = 0

    data_field2.add_updater(update_text)
    self.wait(3)
    data_field2.clear_updaters()

    self.camera.frame.save_state()

    self.play(
        self.camera.frame.animate.scale(2).shift(RIGHT * 20), move_along_animation
    )

    self.remove(*[obj for obj in self.mobjects])

    eth_acc, eth_acc_t = create_table(
        [
            ["Field", "Data"],
            ["nonce", "12"],
            ["balance", "10"],
            ["storage", "userid: 1"],
            ["code", "evmcode.bin"],
        ],
        "Ethereum Account",
        [0, 0, 0],
        0.6,
    )

    self.play(Restore(self.camera.frame), Create(eth_acc))

    return eth_acc, eth_acc_t
