from manim import *
from create_table import create_table


def AccountStructureCode(self: Scene):
    [account, _] = create_table(
        [["Field", "Data"],
         ["lamports", "69420"],
         ["data", "solami"],
         ["owner", "1111..1111"],
         ["executable", "false"],
         ["rent_epoch", "1234"]
         ],
        "Account",
        [0,0,0],
        0.6
    )

    self.play(DrawBorderThenFill(account), run_time=2)
    self.wait(1)

    target_position = account.get_center() + 3 * LEFT
    self.play(account.animate.move_to(target_position))
    codeLinkAccount = Text(
        "https://github.com/solana-labs/solana/blob/master/sdk/src/account.rs#L29", color=BLUE_C, font_size=25)

    accountCode = Code(
        file_name="codeblocks/account.rs",
        background="rectangle",
        tab_width=4,
        line_spacing=0.8,
        font_size=20,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(1)

    accountCode.next_to(account, RIGHT, buff=0.5)
    accountCode.move_to(DOWN)
    codeLinkAccount.move_to([0, -3, 0])

    self.play(Write(accountCode))
    self.add(codeLinkAccount)
    self.wait(2)

    self.play(FadeOut(codeLinkAccount),
              FadeOut(accountCode), run_time=1)

    self.play(account.animate.move_to(
        account.get_center() + 3 * RIGHT))
    self.wait()
    self.wait(1)
    return account