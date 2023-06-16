from manim import *
from create_table import create_table, create_table_progress
import random


random_data = ["userid: 1", "count: 2", "tweet: 69",
               "content", "12/7/2006", "active: false"]


def TwoAccountDesc(self: Scene, account):

    title = Text("Types of Accounts", font_size=60)
    self.play(Write(title), run_time=1.5)

    self.wait(1.5)

    def apply_function(mob):
        mob.become(Text("2. Types of Accounts", color=BLUE_B, font_size=25).to_corner(UL))
        return mob

    self.play(
        ApplyFunction(apply_function, title),
        run_time=2,  # Total duration of the animation
    )

    [ex_account, ex_account_table] = create_table(
        [["Field", "Data"],
            ["lamports", "69420"],
            ["owner", "BPF...111"],
            ["executable", "true"],
            ["data", "data.bin"],
            ["rent_epoch", "1234"]
         ],
        "Executable Account",
        [0, 0, 0],
        0.5
    )
    ex_account.next_to(account, LEFT, buff=-1.5)
    data_field = ex_account_table.get_rows()[4][1]

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
    non_ex_account.next_to(account, RIGHT, buff=-1.5)

    self.play(Transform(account, VGroup(
        non_ex_account, ex_account)))

    self.wait(3)
    self.play(FadeOut(account[0]), FadeOut(
        non_ex_account), FocusOn(ex_account), run_time=1)
    self.wait(5)

    ethDev = ImageMobject("assets/eth.png").scale(0.15)
    ethDev.move_to(ex_account_table.get_center() + 5 * UP)

    self.play(ApplyMethod(ethDev.shift, 5 * RIGHT + 4.8 * DOWN))
    self.wait(2.5)

    anchor = ImageMobject("assets/anchor.png").scale(0.8)
    anchor.move_to(RIGHT)

    self.play(FadeOut(ethDev))
    self.play(FadeIn(anchor))

    self.wait(4)
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
    self.add(code)

    self.play(
        ApplyMethod(code.move_to, [-2.5, 0, 0]),
        run_time=2,
    )
    self.wait(0.1)
    self.play(Transform(code, data_field), run_time=0.9)



    self.wait(4)
    self.remove(
        *[mob for mob in self.mobjects],
    )

    self.play(FadeIn(non_ex_account), run_time=0.7)

    self.wait(1)
    data_field = non_ex_account_table.get_rows()[4][1]

    self.play(data_field.animate.set_color(BLUE),
              data_field.animate.set_weight(BOLD))

    elapsed_time = 0
    delay = 0.3

    def update_text(obj, dt):
        nonlocal elapsed_time
        elapsed_time += dt
        if elapsed_time >= delay:
            obj.become(Text(random.choice(random_data),
                            font_size=23, color=BLUE, weight=BOLD).move_to(data_field.get_center()))
            elapsed_time = 0

    data_field.add_updater(update_text)

    self.wait(3)
    data_field.clear_updaters()

    program_image = ImageMobject("assets/explorer_program.png").scale(1)
    self.add(program_image)
    self.wait(1)

    rectangle = Rectangle(
        height=0.5,
        width=3,
        stroke_color=WHITE,
        stroke_width=6,
    )
    rectangle.shift([5.3, -0.1, 0])
    self.play(Write(rectangle))

    self.wait(4)

    self.play(FadeOut(program_image), FadeOut(rectangle), run_time=0.5)
    self.wait()


    img = ImageMobject("assets/system_account_output.png")
    img.next_to(non_ex_account_table, LEFT, buff=1)
    self.play(FadeIn(img), run_time=0.8)

    self.wait(2)
    rectangle = Rectangle(
        height=0.8,
        width=1.5,
        stroke_color=WHITE,
        stroke_width=5,
    )
    rectangle.shift([-3.8, -0.2, 0])
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

    self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.8)

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
              0]), run_time=5, rate_func=linear)

    status = Text("Storage capacity reached", font_size=25,
                  color=ORANGE).next_to(progress_bar, DOWN)

    self.play(Write(status), run_time=0.6)

    self.play(*[FadeOut(i) for i in self.mobjects])
