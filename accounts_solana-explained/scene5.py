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

    title = Text("Comparison With Ethereum", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("3. Comparison With Ethereum", color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,  # Total duration of the animation
    )

    eth_acc, eth_acc_t = create_table(
        [
            ["Field", "Data"],
            ["nonce", "12"],
            ["balance", "10"],
            ["storage", "{user_id: xyz}"],
            ["code", "evmcode.bin"],
        ],
        "Ethereum Account",
        [0, 0, 0],
        0.6,
    )

    storage = eth_acc_t.get_rows()[3]
    code = eth_acc_t.get_rows()[4]


    eth_acc.move_to(LEFT * 6)
    self.play(Create(eth_acc), eth_acc.animate.move_to(LEFT * 0))
    self.wait(1)
    self.camera.frame.save_state()
    self.play(
        self.camera.frame.animate.set_width(eth_acc.get_width() * 1.2),
        self.camera.frame.animate.move_to(eth_acc).scale(0.7),
        storage.animate.set_color(BLUE_C),
    )
    self.wait(2)
    self.play(Restore(self.camera.frame), storage.animate.set_color(WHITE))

    self.wait(2)
    self.camera.frame.save_state()
    self.play(
        self.camera.frame.animate.set_width(eth_acc.get_width() * 1.2),
        self.camera.frame.animate.move_to(eth_acc).scale(0.7).shift(DOWN * 2),
        code.animate.set_color(GREEN_C),
    )
    self.wait(2)
    self.play(Restore(self.camera.frame), storage.animate.set_color(WHITE))
    self.wait(2)
    return eth_acc, eth_acc_t
