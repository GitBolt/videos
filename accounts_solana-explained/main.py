import manim as mn


class Accounts(mn.Scene):
    def construct(self):
        mn.Text.set_default(font="Cantarell", font_size=50)
        tx1 = mn.Text("Everything in Solana")
        tx2 = mn.Text("Everything", font_size=60)
        tx3 = mn.Text("is an Account")

        self.play(mn.Write(tx1), run_time=1.2)
        self.play(mn.FadeOut(tx1), run_time=0.5)
        self.wait(0.8)

        self.play(mn.ScaleInPlace(tx2, 2), run_time=0.1)
        self.wait()
        self.play(mn.FadeOut(tx2), run_time=0.1)

        self.play(mn.FadeIn(tx3))
        self.wait()
        self.play(mn.FadeOut(tx3), run_time=0.1)

        account_image = mn.ImageMobject("explorer_account.png").scale(1)
        self.add(account_image)
        self.wait()

        rectangle = mn.Rectangle(
            height=0.8,
            width=3,
            stroke_color=mn.WHITE,
            stroke_width=5,
        )
        rectangle.shift([-5.3, 2.4, 0])
        self.play(mn.Write(rectangle))

        point = mn.Dot(color=mn.WHITE)
        point.move_to(rectangle.get_right() + mn.RIGHT * 0.1)

        line = mn.Line(point.get_center(), point.get_center() + mn.RIGHT * 4)
        line.set_color(mn.WHITE)

        self.play(
            mn.FadeIn(point),
            mn.Write(line),
            run_time=1
        )

        what = mn.Text("What?")
        what.next_to(line.get_end(), mn.RIGHT, buff=0.5)
        self.play(mn.Write(what), run_time=0.9)
        self.wait()

        self.remove(account_image, line, point, what, rectangle)
        self.wait()

        table_data = [["Field", "Data"],
                      ["lamports", "100020"],
                      ["owner", "1111..1111"],
                      ["executable", "true"],
                      ["data", "..."],
                      ["rent_epoch", "1234"]
                      ]

        table = mn.Table(table_data, line_config={
            "stroke_width": 1, "color": mn.GRAY_C}, include_outer_lines=True
        )
        table.scale(0.3)
        table.add_highlighted_cell((1, 1), color="#163A70")
        table.add_highlighted_cell((1, 2), color="#163A70")
        table.move_to([-4.5, 0, 0])

        box = mn.SurroundingRectangle(
            table, buff=0.2, color=mn.WHITE, fill_opacity=0.04, corner_radius=0.2)
        box.set_stroke(width=0)

        title = mn.Text("Account 1", font_size=18, color=mn.WHITE)
        title.next_to(box.get_top(), mn.UP, buff=0.1)

        table_group = mn.VGroup(table, box, title)

        self.play(mn.Create(table_group))
        self.wait()

        code = mn.Code(
            code="SystemProgram::CreateAccount",
            language="rust",
            background="rectangle",
            tab_width=4,
            font_size=10,
            corner_radius=0.1,
            background_stroke_width=0,
            insert_line_no=False,
            style="dracula",
        ).scale(1.3)

        code.next_to(table, mn.RIGHT, buff=0.5)
        self.play(mn.Create(code), run_time=0.5)
        self.wait()

        table_data2 = [["Field", "Data"],
                       ["lamports", "69420"],
                       ["owner", "1111..1111"],
                       ["executable", "false"],
                       ["data", "solami"],
                       ["rent_epoch", "1234"]
                       ]

        table2 = mn.Table(table_data2, line_config={
            "stroke_width": 1, "color": mn.GRAY_C}, include_outer_lines=True
        )
        table2.scale(0.3)
        table2.add_highlighted_cell((1, 1), color="#163A70")
        table2.add_highlighted_cell((1, 2), color="#163A70")

        box2 = mn.SurroundingRectangle(
            table2, buff=0.2, color=mn.WHITE, fill_opacity=0.04, corner_radius=0.3)
        box2.set_stroke(width=0)

        title2 = mn.Text("Account 2", font_size=18, color=mn.WHITE)
        title2.next_to(box2.get_top(), mn.UP, buff=0.1)

        table_group2 = mn.VGroup(table2, box2, title2)

        table_group2.next_to(code, mn.RIGHT, buff=0.5)
        self.play(mn.Create(table_group2))

        start_point = table.get_corner(mn.UP + mn.LEFT)
        end_point = table2.get_corner(mn.UP + mn.RIGHT)
        curve_arrow = mn.Arrow(start_point, end_point,
                               path_arc=-90 * mn.DEGREES, color=mn.WHITE, stroke_width=2)

        self.play(mn.Create(curve_arrow), run_time=1.6)

        self.wait(2)
        self.remove(curve_arrow, table_group, table_group2, code)

        table_data3 = [["Field", "Data"],
                       ["lamports", "69420"],
                       ["owner", "1111..1111"],
                       ["executable", "false"],
                       ["data", "solami"],
                       ["rent_epoch", "1234"]
                       ]
        table3 = mn.Table(table_data3, line_config={
            "stroke_width": 1, "color": mn.GRAY_C}, include_outer_lines=True)
        table3.scale(0.5)
        table3.add_highlighted_cell((1, 1), color="#163A70")
        table3.add_highlighted_cell((1, 2), color="#163A70")
        box3 = mn.SurroundingRectangle(
            table3, buff=0.5, color=mn.WHITE, fill_opacity=0.04, corner_radius=0.3)
        box3.set_stroke(width=0)
        title3 = mn.Text("Account", font_size=25, color=mn.WHITE)
        title3.next_to(box3.get_top(), mn.UP, buff=0.1)
        table_group3 = mn.VGroup(table3, box3, title3)

        self.play(mn.Create(table_group3), run_time=3)
        self.wait(1)

        # Define the target position for the table
        target_position = table_group3.get_center() + 3 * mn.LEFT

        # Move the table to the left
        self.play(table_group3.animate.move_to(target_position))

        codeLinkAccount = mn.Text(
            "https://github.com/solana-labs/solana/blob/master/sdk/src/account.rs#L29", color=mn.BLUE_C, font_size=15)
        accountCode = mn.Code(
            file_name="codeblocks/account.rs",
            background="rectangle",
            tab_width=4,
            font_size=20,

            corner_radius=0.1,
            background_stroke_width=0,
            insert_line_no=False,
            style="dracula",
        ).scale(1)
        accountCode.next_to(table_group3, mn.RIGHT, buff=0.7)
        codeLinkAccount.next_to(accountCode, mn.DOWN, buff=1.7)
        # Move the code block to its final position while the table is moving
        self.play(mn.Create(accountCode))
        self.add(codeLinkAccount)
        self.wait()

        self.play(mn.FadeOut(codeLinkAccount),
                     mn.FadeOut(accountCode), run_time=1)
        self.play(table_group3.animate.move_to(table_group3.get_center() + 3 * mn.RIGHT))

        table_executable = table_group3.copy()
        table_executable[-1] = mn.Text("Executable Account", font_size=25,
                                       color=mn.WHITE).next_to(box3.get_top(), mn.UP, buff=0.1)
        table_data_ex = [["Field", "Data"],
                         ["lamports", "69420"],
                         ["owner", "BPFLoa...1111"],
                         ["executable", "true"],
                         ["data", "byte_data.bin"],
                         ["rent_epoch", "1234"]
                         ]

        table_ex = mn.Table(table_data_ex, line_config={
            "stroke_width": 1, "color": mn.GRAY_C}, include_outer_lines=True)
        table_ex.set
        table_ex.scale(0.5)
        table_ex.add_highlighted_cell((1, 1), color="#163A70")
        table_ex.add_highlighted_cell((1, 2), color="#163A70")

        table_executable[0] = table_ex
        table_executable.next_to(table_group3, mn.RIGHT, buff=-2)

        table_non_executable = table_group3.copy()
        table_non_executable[-1] = mn.Text("Non-executable Account", font_size=25,
                                           color=mn.WHITE).next_to(box3.get_top(), mn.UP, buff=0.1)
        table_data_nex = [["Field", "Data"],
                          ["lamports", "69420"],
                          ["owner", "1111..1111"],
                          ["executable", "false"],
                          ["data", "solami"],
                          ["rent_epoch", "1234"]
                          ]

        table_nex = mn.Table(table_data_nex, line_config={
            "stroke_width": 1, "color": mn.GRAY_C}, include_outer_lines=True)
        table_nex.set
        table_nex.scale(0.5)
        table_nex.add_highlighted_cell((1, 1), color="#163A70")
        table_nex.add_highlighted_cell((1, 2), color="#163A70")

        table_non_executable[0] = table_nex
        table_non_executable.next_to(table_group3, mn.RIGHT, buff=-2)

        self.play(mn.Transform(table_group3, table_executable))
        self.play(mn.Transform(table_group3, mn.VGroup(
            table_executable, table_non_executable)))
        self.wait(4)
