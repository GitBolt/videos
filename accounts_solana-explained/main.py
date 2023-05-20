import manim as mn


class Accounts(mn.Scene):
    def construct(self):
        mn.Text.set_default(font="Hack", font_size=50)
        tx1 = mn.Text("Everything in Solana")
        tx2 = mn.Text("Everything", font_size=60)
        tx3 = mn.Text("Is an Account.")

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
            "stroke_width": 1, "color": mn.GRAY_C})
        table.scale(0.3)
        table.add_highlighted_cell((1,1), color="#163A70")
        table.add_highlighted_cell((1,2), color="#163A70")
        table.move_to([-4.5, -1, 0])

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
            "stroke_width": 1, "color": mn.GRAY_C})
        table2.scale(0.3)
        table2.add_highlighted_cell((1,1), color="#331670")
        table2.add_highlighted_cell((1,2), color="#331670")

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

        self.wait(1)
