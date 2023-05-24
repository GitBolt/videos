from manim import *
from create_table import create_table
from make_code import make_code


def TokenAccounts(self: Scene):
    head = Text("Everything is an Account", font_size=40)
    self.play(Write(head), run_time=2)
    self.wait(1.5)
    system_account, system_account_t = create_table(
        [
            ["Field", "Data"],
            ["lamports", "35000"],
            ["data", "metadata"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "USDC Mint Account",
        [0, 0, 0],
        0.5,
    )

    owner = system_account_t.get_rows()[3][1]

    system_account.z_index = 2
    self.play(Uncreate(head))
    self.play(Create(system_account))

    usdc = SVGMobject("assets/usdc.svg").scale(0.5)
    usdc.z_index = 0
    usdc.move_to(LEFT * 6)

    usdt = SVGMobject("assets/usdt.svg").scale(0.5)
    usdt.z_index = 0
    usdt.next_to(usdc, RIGHT)

    self.play(Write(usdc), Write(usdt))

    self.play(usdc.animate.move_to(system_account.get_center()).scale(0.2))
    self.play(usdc.animate.move_to(RIGHT * 3.5).scale(5))

    self.play(usdt.animate.move_to(system_account.get_center()).scale(0.2))
    self.play(usdt.animate.move_to(RIGHT * 5).scale(5))

    self.wait(2)

    owner.become(Text("Token...Q5DA", font_size=20).move_to(owner.get_center()))

    token_account = system_account.copy()

    newusdc = SVGMobject("assets/usdc.svg").scale(0.2)
    newusdc.next_to(token_account[2], LEFT)

    self.play(FadeOut(usdt), Transform(usdc, token_account))
    self.play(Write(newusdc), run_time=0.8)
    token_account.add(newusdc)

    self.remove(system_account, usdc)
    self.play(token_account.animate.move_to(LEFT * 3.2 + UP * 1).scale(0.9))

    metadata = Code(
        code="""
        {
            "decimals":6,
            "freezeAuthority":"3sNB...ypn6",
            "isInitialized":true,
            "mintAuthority":"2wmV...dri9",
            "supply":"5034943402728500"
        }
        """,
        language="json",
        background="rectangle",
        tab_width=4,
        font_size=20,
        corner_radius=0.1,
        background_stroke_width=0,
        insert_line_no=False,
        style="dracula",
    ).scale(0.9)

    metadata.move_to(RIGHT * 3.5 + DOWN * 1.2)

    arrow = Arrow([-1.1, 1.2, 0], metadata.get_left(), path_arc=50 * DEGREES)

    self.play(Create(metadata), Create(arrow))
    self.wait(5)

    self.camera.frame.save_state()
    self.play(self.camera.frame.animate.move_to(RIGHT * 20).scale(2))

    self.remove(*[obj for obj in self.mobjects])

    account1, _ = create_table(
        [
            ["Field", "Data"],
            ["lamports", "69420"],
            ["data", "..."],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "System/User Account 1 (ASg2...12ij)",
        [0, 0, 0],
        0.5,
    )

    account2, _ = create_table(
        [
            ["Field", "Data"],
            ["lamports", "69420"],
            ["data", "..."],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "System/User Account 2 (B3Bh...44ai)",
        [0, 0, 0],
        0.5,
    )

    tokenAccount, _ = create_table(
        [
            ["Field", "Data"],
            ["lamports", "12000"],
            ["data", "Metadata.data"],
            ["owner", "Token...Q5DA"],
            ["executable", "false"],
            ["rent_epoch", "1234"],
        ],
        "Token Account (Account 2)",
        [0, 0, 0],
    )
    tokenAccount.move_to(UP).scale(0.7)

    metadata = make_code(
        """
            "isNative":false,
            "mint":"Es9v...nwNYB",
            "owner":"B3Bh...44ai",
            "state":"initialized",
            "tokenAmount":{
                "amount":"1000000",
                "decimals":6,
                "uiAmount":1,
                "uiAmountString":"1"
            }
        """,
        "json",
    )

    screen_amount = Text("1 USDC", font_size=50, color=BLUE)

    self.add(account1)
    self.add(account2)
    self.play(Restore(self.camera.frame), run_time=1.5)

    self.play(
        account1.animate.move_to(LEFT * 4.5 + DOWN * 2).scale(0.6),
        account2.animate.move_to(RIGHT * 4.5 + DOWN * 2).scale(0.6),
    )

    usdc = SVGMobject("assets/usdc.svg").scale(0.2)
    usdc_amount = Text("1", font_size=28, weight=BOLD)

    usdc_amount.next_to(usdc, RIGHT)
    usdc_value = VGroup(usdc, usdc_amount)
    usdc_value.move_to(account1.get_right())

    self.play(Write(usdc_value))

    self.wait(2)

    tokenAccount.move_to(LEFT * 2 + UP * 2)
    self.play(Create(tokenAccount))

    metadata_title = Text("Metadata", font_size=15)
    metadata_title.next_to(metadata, UP, buff=0.2)
    metadataGroup = VGroup(metadata, metadata_title)

    metadataGroup.next_to(tokenAccount, RIGHT, buff=1)

    self.play(Write(metadata), Write(metadata_title))

    self.wait()

    metadata_dot = Dot()
    metadata_arrow = Arrow(
        tokenAccount.get_right(),
        metadata,
        path_arc=20 * DEGREES,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.2,
    )
    metadata_dot.move_to(metadata_arrow.get_start())

    self.play(GrowArrow(metadata_arrow), Create(metadata_dot))

    owner_dot = Dot()
    owner_arrow = Arrow(
        [3.8, 2.6, 0],
        account2.get_top(),
        path_arc=-20 * DEGREES,
        stroke_width=3,
        max_tip_length_to_length_ratio=0.1,
    )
    owner_dot.move_to(owner_arrow.get_start())

    self.play(GrowArrow(owner_arrow), Create(owner_dot))

    screen_amount.move_to([0, -1.5, 0])

    display_arrow = Arrow(
        metadata,
        screen_amount.get_top(),
        stroke_width=3,
        max_tip_length_to_length_ratio=0.1,
    )
    self.play(GrowArrow(display_arrow))
    self.play(Write(screen_amount))

    self.wait()

    self.play(usdc_value.animate.move_to(tokenAccount.get_left()).scale(0.7))
    self.play(FadeOut(usdc_value), run_time=0.8)

    self.play(
        metadata.animate.become(
            make_code(
                """
            "isNative":false,
            "mint":"Es9v...nwNYB",
            "owner":"B3Bh...44ai",
            "state":"initialized",
            "tokenAmount":{
                "amount":"2000000",
                "decimals":6,
                "uiAmount":2,
                "uiAmountString":"2"
            }
        """,
                "json",
            ).move_to(metadata.get_center())
        ),
        screen_amount.animate.become(
            Text("2 USDC", font_size=50, color=BLUE).move_to([[0, -1.5, 0]])
        ),
    )
    self.wait()

    usdc_value.move_to(account1.get_right())

    self.play(Write(usdc_value))

    self.play(usdc_value.animate.move_to(tokenAccount.get_left()).scale(0.7))
    self.play(FadeOut(usdc_value), run_time=0.8)

    self.play(
        metadata.animate.become(
            make_code(
                """
            "isNative":false,
            "mint":"Es9v...nwNYB",
            "owner":"B3Bh...44ai",
            "state":"initialized",
            "tokenAmount":{
                "amount":"3000000",
                "decimals":6,
                "uiAmount":3,
                "uiAmountString":"3"
            }
        """,
                "json",
            ).move_to(metadata.get_center())
        ),
        screen_amount.animate.become(
            Text("3 USDC", font_size=50, color=BLUE).move_to([[0, -1.5, 0]])
        ),
    )

    self.wait(1)
    self.play(*[FadeOut(obj) for obj in self.mobjects])
    self.wait(3)