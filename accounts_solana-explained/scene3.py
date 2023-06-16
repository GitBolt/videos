from manim import *
from create_table import create_table


def AccountStructureCode(self: Scene):

    title = Text("Account Structure", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("1. Account Structure", color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,
    )

    [account, account_table] = create_table(
        [["Field", "Data"],
         ["lamports", "69420"],
         ["data", "solami"],
         ["owner", "1111..1111"],
         ["executable", "false"],
         ["rent_epoch", "1234"]
         ],
        "Account",
        [0, 0, 0],
        0.6
    )

    self.play(DrawBorderThenFill(account), run_time=2)
    self.wait(1)

    target_position = account.get_center() + 3.3 * LEFT
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

    accountCode.next_to(account, RIGHT * 1, buff=1)
    codeLinkAccount.move_to([0, -3.5, 0])

    self.play(Write(accountCode))
    self.play(Write(codeLinkAccount))
    self.wait(2)

    self.play(FadeOut(codeLinkAccount),
              FadeOut(accountCode), run_time=1)

    self.play(account.animate.move_to(
        account.get_center() + 3 * RIGHT))

    self.wait(1)

    rect = SurroundingRectangle(
        account_table.get_rows()[1], color=BLUE_C, buff=0.1)

    self.add(account_table.add(rect))

    self.wait(10)

    for i in range(1, 5):
        new_rect_nex = SurroundingRectangle(
            account_table.get_rows()[i+1], color=BLUE_C, buff=0.1)

        self.play(ApplyMethod(rect.move_to, new_rect_nex),
                  run_time=1)

        if i == 1:
            self.wait(6)
        elif i == 3:
            self.wait(10)
        else:
            self.wait(8)

    self.play(Uncreate(rect), Uncreate(account), Uncreate(title))
    return account
