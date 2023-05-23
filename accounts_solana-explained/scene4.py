from manim import *
from create_table import create_table, create_table_progress
import random


random_data = ["userid: 1", "count: 2", "tweet: 69",
               "content", "12/7/2006", "active: false"]


def TwoAccountDesc(self: Scene, account):
    [ex_account, ex_account_table] = create_table(
        [["Field", "Data"],
            ["lamports", "69420"],
            ["owner", "BPFL...1111"],
            ["executable", "true"],
            ["data", "bytedata.bin"],
            ["rent_epoch", "1234"]
         ],
        "Executable Account",
        [0, 0, 0],
        0.5
    )
    ex_account.next_to(account, RIGHT, buff=-0.7)

    [non_ex_account, non_ex_account_table] = create_table(
        [["Field", "Data"],
            ["lamports", "69420"],
            ["owner", "1111..1111"],
            ["executable", "false"],
            ["data", "solami"],
            ["rent_epoch", "1234"]
         ],
        "Non-Executable Account",
        [0, 0, 0],
        0.5
    )
    non_ex_account.next_to(account, LEFT, buff=-0.7)

    self.play(Transform(account, VGroup(
        non_ex_account, ex_account)))
    self.wait()

    rect_nex = SurroundingRectangle(
        non_ex_account_table.get_rows()[1], color=BLUE_C, buff=0.1)
    rect_ex = SurroundingRectangle(
        ex_account_table.get_rows()[1], color=BLUE_C, buff=0.1)

    self.play(Write(non_ex_account_table.add(rect_nex)),
              Write(ex_account_table.add(rect_ex)))
    self.wait(5)

    for i in range(1, 5):
        new_rect_nex = SurroundingRectangle(
            non_ex_account_table.get_rows()[i+1], color=BLUE_C, buff=0.1)

        new_rect_ex = SurroundingRectangle(
            ex_account_table.get_rows()[i+1], color=BLUE_C, buff=0.1)
        self.play(ApplyMethod(rect_nex.move_to, new_rect_nex),
                  ApplyMethod(rect_ex.move_to, new_rect_ex),
                  run_time=1)
        self.wait(5)

    self.play(Uncreate(rect_nex), Uncreate(rect_ex))

    self.play(FadeOut(account[0]), FadeOut(
        non_ex_account), FocusOn(ex_account), run_time=1)
    self.wait(2)

    ethDev = ImageMobject("assets/eth.png").scale(0.15)
    ethDev.move_to(ex_account_table.get_center() + 5 * UP)

    self.play(ApplyMethod(ethDev.shift, 5 * LEFT + 5 * DOWN))
    self.wait(2)

    program_image = ImageMobject("assets/explorer_program.png").scale(1)
    self.play(FadeIn(program_image))
    self.wait()

    rectangle = Rectangle(
        height=0.5,
        width=3,
        stroke_color=WHITE,
        stroke_width=6,
    )
    rectangle.shift([5.3, -0.1, 0])
    self.remove(ethDev)
    self.play(Write(rectangle))

    self.wait()

    self.remove(
        *[mob for mob in self.mobjects],
    )
    self.wait()

    self.play(Create(non_ex_account), run_time=0.8)

    data_field = non_ex_account_table.get_rows()[4][1]

    elapsed_time = 0
    delay = 0.3

    def update_text(obj, dt):
        nonlocal elapsed_time
        elapsed_time += dt
        if elapsed_time >= delay:
            obj.become(Text(random.choice(random_data),
                            font_size=23).move_to(data_field.get_center()))
            elapsed_time = 0

    data_field.add_updater(update_text)

    self.wait(4)
    data_field.clear_updaters()

    self.wait()

    img = ImageMobject("assets/system_account_output.png")
    img.next_to(non_ex_account_table, RIGHT, buff=1)
    self.play(FadeIn(img))

    rectangle = Rectangle(
        height=0.8,
        width=1.5,
        stroke_color=WHITE,
        stroke_width=5,
    )
    rectangle.shift([1, -0.2, 0])
    self.play(Write(rectangle))

    point = Dot(color=WHITE)
    point.move_to(rectangle.get_bottom() + DOWN * 0.1)

    line = Line(point.get_center(), point.get_center() + DOWN * 1.8)
    line.set_color(WHITE)

    self.play(
        FadeIn(point),
        Write(line),
        run_time=1
    )
    what = Text("No data", font_size=30)
    what.next_to(line.get_end(), DOWN, buff=0.2)
    self.play(Write(what), run_time=0.5)

    self.wait()

    progress_table, progress_table_t = create_table_progress(

        [["Field", "Data"],
         ["lamports", "69420"],
         ["owner", "1111..1111"],
         ["executable", "false"],
         ["data", "6.19mb.bin"],
         ["rent_epoch", "1234"]
         ],
        "Non-Executable Account",
        [0, 0, 0],
        0.5,
        BLUE_C,
        "Storage"
    )
    data = progress_table_t.get_rows()[4][1]

    progress_bar = progress_table[0]

    initial_start = progress_bar.get_left()

    # self.play(Transform(rent, rent2))
    self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.8)

    self.play(FadeIn(progress_table))

    x = ValueTracker(progress_bar.get_left()[0])

    dot = Dot(color=BLUE_B)
    dot.move_to(progress_bar.get_left())

    self.play(GrowFromCenter(dot))

    dot.add_updater(lambda z: z.set_x(x.get_value()))

    data.add_updater(lambda z: z.become(Text(str(round(
        x.get_value() + 7.68, 2))+"mb.bin", font_size=22).move_to(data.get_center())))

    progress_bar.add_updater(lambda z: z.become(
        Line(color=BLUE_C, start=initial_start, end=dot.get_center())))

    self.play(x.animate.set_value(progress_table[1].get_right()[
              0]), run_time=3, rate_func=linear)

    self.play(Write(Text("Storage capacity reached", font_size=25,
              color=ORANGE).next_to(progress_bar, DOWN)), run_time=0.6)

    self.play(*[FadeOut(i) for i in self.mobjects])
