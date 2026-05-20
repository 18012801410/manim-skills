"""
相遇问题 (Meeting Problem) - Elementary Math Educational Video
================================================================

A Manim Community Edition animation explaining the classic
"two people walking toward each other" problem.

Target: grades 4-5, basic arithmetic.
Length: ~4 minutes.
Style: 3b1b classic dark.

Render: manim -pqh meeting_problem.py MeetingProblem
"""

from manim import *

# ── Color Palette (3b1b Classic Dark) ──────────────────────────────
MING_BLUE = "#58C4DD"
HONG_GREEN = "#83C167"
YELLOW_KEY = "#FFE66D"
GREY_SUB = "#B0B0B0"
BG_DARK = "#1C1C1C"

config.background_color = BG_DARK

# ── Reusable sizing constants ──────────────────────────────────────
ROAD_Y = 1.5
ROAD_LEFT = LEFT * 5
ROAD_RIGHT = RIGHT * 5
MEET_X = 0.5  # meeting point closer to right since Ming is faster


class MeetingProblem(Scene):
    """Complete explainer video for the elementary math meeting problem."""

    # ── Scene 1: Problem Introduction (~40s) ───────────────────────
    def s1_intro(self) -> None:
        # Road
        road = Line(ROAD_LEFT, ROAD_RIGHT, color=WHITE, stroke_width=3)
        road.shift(UP * ROAD_Y)

        # Houses
        house_l = Text("小明家", font_size=28, color=WHITE)
        house_l.next_to(road.get_start(), DOWN, buff=0.3)
        house_r = Text("小红家", font_size=28, color=WHITE)
        house_r.next_to(road.get_end(), DOWN, buff=0.3)

        # Distance brace + label
        brace = Brace(road, UP)
        dist_label = Text("840米", font_size=36, color=GREY_SUB)
        dist_label.next_to(brace, UP, buff=0.15)

        # Character dots on the road
        ming_dot = Dot(road.get_start(), color=MING_BLUE, radius=0.18)
        hong_dot = Dot(road.get_end(), color=HONG_GREEN, radius=0.18)

        # Character names
        ming_name = Text("小明", font_size=24, color=MING_BLUE)
        ming_name.next_to(ming_dot, DOWN, buff=0.2)
        hong_name = Text("小红", font_size=24, color=HONG_GREEN)
        hong_name.next_to(hong_dot, DOWN, buff=0.2)

        # Speed labels
        ming_speed = Text("70米/分", font_size=30, color=MING_BLUE)
        ming_speed.next_to(ming_dot, UP, buff=0.15)
        hong_speed = Text("50米/分", font_size=30, color=HONG_GREEN)
        hong_speed.next_to(hong_dot, UP, buff=0.15)

        # Direction arrows
        ming_arrow = Arrow(
            ming_dot.get_center() + RIGHT * 0.5,
            ming_dot.get_center() + RIGHT * 1.8,
            color=MING_BLUE, stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )
        hong_arrow = Arrow(
            hong_dot.get_center() + LEFT * 0.5,
            hong_dot.get_center() + LEFT * 1.8,
            color=HONG_GREEN, stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
        )

        # Direction text
        direction = Text("同时出发，相向而行", font_size=30, color=WHITE)
        direction.to_edge(DOWN, buff=2.0)

        # Question
        question = Text("几分钟后相遇？", font_size=44, color=YELLOW_KEY, weight=BOLD)
        question.next_to(direction, DOWN, buff=0.5)

        # ── Animation ──
        self.play(Create(road))
        self.wait(0.2)
        self.play(FadeIn(house_l), FadeIn(house_r))
        self.play(GrowFromCenter(brace), FadeIn(dist_label))
        self.wait(0.3)
        self.play(FadeIn(ming_dot, scale=0.5), FadeIn(hong_dot, scale=0.5))
        self.play(Write(ming_name), Write(hong_name))
        self.wait(0.2)
        self.play(Write(ming_speed), Write(hong_speed))
        self.play(GrowArrow(ming_arrow), GrowArrow(hong_arrow))
        self.wait(0.3)
        self.play(Write(direction))
        self.wait(0.3)
        self.play(Write(question))
        self.wait(1.5)

        # Store for later transitions
        self.road = road
        self.ming_dot = ming_dot
        self.hong_dot = hong_dot
        self.ming_speed = ming_speed
        self.hong_speed = hong_speed

        # Clear decorations but keep road and dots
        self.play(
            FadeOut(house_l), FadeOut(house_r),
            FadeOut(brace), FadeOut(dist_label),
            FadeOut(ming_name), FadeOut(hong_name),
            FadeOut(ming_arrow), FadeOut(hong_arrow),
            FadeOut(direction), FadeOut(question),
        )

    # ── Scene 2: Line Segment Diagram (~70s) ───────────────────────
    def s2_diagram(self) -> None:
        # Transform road into abstract segment
        segment = Line(ROAD_LEFT, ROAD_RIGHT, color=WHITE, stroke_width=4)
        segment.shift(UP * ROAD_Y)

        self.play(ReplacementTransform(self.road, segment))
        self.wait(0.2)

        # Endpoint labels A, B
        label_a = Text("A", font_size=30, color=GREY_SUB)
        label_a.next_to(segment.get_start(), DOWN, buff=0.25)
        label_b = Text("B", font_size=30, color=GREY_SUB)
        label_b.next_to(segment.get_end(), DOWN, buff=0.25)
        label_a_sub = Text("(小明家)", font_size=20, color=GREY_SUB)
        label_a_sub.next_to(label_a, DOWN, buff=0.05)
        label_b_sub = Text("(小红家)", font_size=20, color=GREY_SUB)
        label_b_sub.next_to(label_b, DOWN, buff=0.05)

        self.play(FadeIn(label_a), FadeIn(label_b))
        self.play(FadeIn(label_a_sub), FadeIn(label_b_sub))

        # Distance label
        dist = Text("840米", font_size=34, color=WHITE)
        dist.next_to(segment, UP, buff=0.4)
        self.play(Write(dist))
        self.wait(0.5)

        # Meeting point — slides from left toward meeting position
        t_meet = (MEET_X - ROAD_LEFT[0]) / (ROAD_RIGHT[0] - ROAD_LEFT[0])
        meet_start = segment.get_start() + RIGHT * 0.1
        meet_target = segment.point_from_proportion(t_meet)

        meet_point = Dot(meet_start, color=YELLOW_KEY, radius=0.12)
        self.play(FadeIn(meet_point, scale=0.5))
        self.play(meet_point.animate.move_to(meet_target), run_time=1.5)
        self.wait(0.3)

        # Split into colored segments
        ming_seg = Line(
            segment.get_start(), meet_point.get_center(),
            color=MING_BLUE, stroke_width=6,
        )
        hong_seg = Line(
            meet_point.get_center(), segment.get_end(),
            color=HONG_GREEN, stroke_width=6,
        )
        self.play(Create(ming_seg), Create(hong_seg))
        self.wait(0.3)

        # Braces under each segment
        brace_ming = Brace(ming_seg, DOWN, color=MING_BLUE)
        label_ming = MathTex(r"70\times ?", font_size=32, color=MING_BLUE)
        label_ming.next_to(brace_ming, DOWN, buff=0.1)

        brace_hong = Brace(hong_seg, DOWN, color=HONG_GREEN)
        label_hong = MathTex(r"50\times ?", font_size=32, color=HONG_GREEN)
        label_hong.next_to(brace_hong, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(brace_ming), FadeIn(label_ming),
            GrowFromCenter(brace_hong), FadeIn(label_hong),
        )
        self.wait(0.8)

        # Equation below diagram
        eq_text = Text("小明的路程 + 小红的路程 = 总路程", font_size=28, color=WHITE)
        eq_text.to_edge(DOWN, buff=1.2)

        eq_math = MathTex(
            r"70\times ?", r"+", r"50\times ?", r"=", r"840",
            font_size=36,
        )
        eq_math[0].set_color(MING_BLUE)
        eq_math[2].set_color(HONG_GREEN)
        eq_math.next_to(eq_text, DOWN, buff=0.4)

        self.play(Write(eq_text))
        self.wait(0.5)
        self.play(Write(eq_math))
        self.wait(2.0)

        # Store for transition
        self.segment = segment
        self.meet_point = meet_point
        self.ming_seg = ming_seg
        self.hong_seg = hong_seg
        self.s2_deco = VGroup(
            label_a, label_b, label_a_sub, label_b_sub,
            dist, brace_ming, brace_hong, label_ming, label_hong,
            eq_text, eq_math,
        )

    # ── Scene 3: Method 1 — Separate Calculation (~50s) ────────────
    def s3_method1(self) -> None:
        # Shrink diagram to left half
        diagram = VGroup(self.segment, self.meet_point, self.ming_seg, self.hong_seg)
        self.play(diagram.animate.scale(0.75).to_edge(LEFT, buff=1.0))
        self.wait(0.2)

        # Clear S2 labels
        self.play(FadeOut(self.s2_deco))

        # Replace ? with x in labels below diagram
        label_ming2 = MathTex(r"70x", font_size=30, color=MING_BLUE)
        label_ming2.next_to(self.ming_seg, DOWN, buff=0.5)
        label_hong2 = MathTex(r"50x", font_size=30, color=HONG_GREEN)
        label_hong2.next_to(self.hong_seg, DOWN, buff=0.5)

        self.play(Write(label_ming2), Write(label_hong2))
        self.wait(0.5)

        # ── Right side: equation derivation ──
        eq_title = Text("解法一：分别算，再加起来", font_size=28, color=WHITE)
        eq_title.to_edge(RIGHT, buff=0.8).shift(UP * 2.8)

        step1 = Text("设 x 分钟后相遇", font_size=30, color=GREY_SUB)
        step1.next_to(eq_title, DOWN, buff=0.6).align_to(eq_title, LEFT)

        step2a = Text("小明路程：70x", font_size=28, color=MING_BLUE)
        step2b = Text("小红路程：50x", font_size=28, color=HONG_GREEN)
        step2 = VGroup(step2a, step2b).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        step2.next_to(step1, DOWN, buff=0.35).align_to(step1, LEFT)

        step3 = MathTex(r"70x + 50x = 840", font_size=34)
        step3[0][0:3].set_color(MING_BLUE)
        step3[0][4:7].set_color(HONG_GREEN)
        step3.next_to(step2, DOWN, buff=0.35).align_to(step2, LEFT)

        step4 = MathTex(r"120x = 840", font_size=34)
        step4.next_to(step3, DOWN, buff=0.3).align_to(step3, LEFT)

        step5 = MathTex(r"x = 7", font_size=42, color=YELLOW_KEY)
        step5.next_to(step4, DOWN, buff=0.3).align_to(step4, LEFT)

        # Animate
        self.play(Write(eq_title))
        self.wait(0.3)
        self.play(Write(step1))
        self.wait(0.5)
        self.play(Write(step2a), Write(step2b))
        self.wait(0.5)
        self.play(Write(step3))
        self.wait(0.8)
        self.play(TransformMatchingTex(step3.copy(), step4))
        self.wait(0.6)
        self.play(TransformMatchingTex(step4.copy(), step5))
        self.wait(0.3)

        box = SurroundingRectangle(step5, color=YELLOW_KEY, buff=0.15)
        self.play(Create(box))
        self.wait(0.3)

        # Animate dots converging to meeting point
        meet_y = self.ming_dot.get_center()[1]
        meet_pos = self.meet_point.get_center()
        meet_pos[1] = meet_y

        self.play(
            self.ming_dot.animate.move_to(meet_pos),
            self.hong_dot.animate.move_to(meet_pos),
            run_time=1.2,
        )
        self.wait(0.2)

        answer_text = Text("7分钟后相遇！", font_size=36, color=YELLOW_KEY, weight=BOLD)
        answer_text.next_to(box, DOWN, buff=0.5)
        self.play(Write(answer_text))
        self.wait(1.0)

        self.right_panel = VGroup(eq_title, step1, step2, step3, step4, step5, box, answer_text)
        self.label_ming2 = label_ming2
        self.label_hong2 = label_hong2

    # ── Scene 4: Method 2 — Combined Speed (~50s) ──────────────────
    def s4_method2(self) -> None:
        self.play(FadeOut(self.right_panel))
        self.play(FadeOut(self.label_ming2), FadeOut(self.label_hong2))

        # Reset dots to start positions
        start_left = self.segment.get_start()
        start_left[1] = self.ming_dot.get_center()[1]
        start_right = self.segment.get_end()
        start_right[1] = self.hong_dot.get_center()[1]

        self.play(
            self.ming_dot.animate.move_to(start_left),
            self.hong_dot.animate.move_to(start_right),
            run_time=0.6,
        )

        # Title for method 2
        eq_title2 = Text("解法二：速度和 × 时间", font_size=28, color=WHITE)
        eq_title2.to_edge(RIGHT, buff=0.8).shift(UP * 2.8)

        insight = Text(
            "两人每分钟一共走：70 + 50 = 120 米",
            font_size=30, color=WHITE,
        )
        insight.next_to(eq_title2, DOWN, buff=0.6).align_to(eq_title2, LEFT)

        self.play(Write(eq_title2))
        self.wait(0.3)
        self.play(Write(insight))
        self.wait(1.0)

        # Step-wise animation: 7 hops
        meet_y = self.ming_dot.get_center()[1]
        meet_pos = self.meet_point.get_center()
        meet_pos[1] = meet_y
        delta_ming = (meet_pos - start_left) / 7
        delta_hong = (meet_pos - start_right) / 7

        for _ in range(7):
            self.play(
                self.ming_dot.animate.shift(delta_ming),
                self.hong_dot.animate.shift(delta_hong),
                run_time=0.3,
            )
        self.wait(0.3)

        # Equations for method 2
        s1 = MathTex(r"(70 + 50) \times x = 840", font_size=34)
        s1.next_to(insight, DOWN, buff=0.6).align_to(insight, LEFT)

        s2 = MathTex(r"120 \times x = 840", font_size=34)
        s2.next_to(s1, DOWN, buff=0.3).align_to(s1, LEFT)

        s3 = MathTex(r"x = 7", font_size=42, color=YELLOW_KEY)
        s3.next_to(s2, DOWN, buff=0.3).align_to(s2, LEFT)

        self.play(Write(s1))
        self.wait(0.5)
        self.play(TransformMatchingTex(s1.copy(), s2))
        self.wait(0.5)
        self.play(TransformMatchingTex(s2.copy(), s3))
        self.wait(0.3)

        box2 = SurroundingRectangle(s3, color=YELLOW_KEY, buff=0.15)
        self.play(Create(box2))
        self.wait(0.5)

        same = Text("两种方法，答案一样！", font_size=30, color=YELLOW_KEY)
        same.next_to(box2, DOWN, buff=0.5)
        self.play(Write(same))
        self.wait(1.0)

        self.method2_panel = VGroup(eq_title2, insight, s1, s2, s3, box2, same)

    # ── Scene 5: The Connection (~35s) ─────────────────────────────
    def s5_connection(self) -> None:
        # Clear all
        all_items = VGroup(
            self.segment, self.meet_point,
            self.ming_seg, self.hong_seg,
            self.ming_dot, self.hong_dot,
            self.method2_panel,
        )
        self.play(FadeOut(all_items))
        self.wait(0.2)

        title = Text("殊途同归：两种解法其实是一回事", font_size=32, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Method 1 equation
        m1 = MathTex(r"70x", r"+", r"50x", r"=", r"840", font_size=44)
        m1[0].set_color(MING_BLUE)
        m1[2].set_color(HONG_GREEN)
        m1_label = Text("解法一", font_size=24, color=GREY_SUB)

        # Method 2 equation — split into explicit parts for reliable coloring
        m2 = MathTex(r"(70", r"+", r"50)", r"x", r"=", r"840", font_size=44)
        m2[0][1:3].set_color(MING_BLUE)   # "70"
        m2[2][0:2].set_color(HONG_GREEN)  # "50"
        m2_label = Text("解法二", font_size=24, color=GREY_SUB)

        # Arrange as two rows
        row1 = VGroup(m1_label, m1).arrange(RIGHT, buff=0.5)
        row2 = VGroup(m2_label, m2).arrange(RIGHT, buff=0.5)
        rows = VGroup(row1, row2).arrange(DOWN, buff=1.2)
        rows.shift(UP * 0.3)

        self.play(Write(row1), Write(row2))
        self.wait(1.0)

        # Highlight m1 terms, then m2 grouping
        rect_a = SurroundingRectangle(m1[0], color=MING_BLUE, buff=0.1)
        rect_b = SurroundingRectangle(m1[2], color=HONG_GREEN, buff=0.1)
        m2_grouped = VGroup(m2[0], m2[1], m2[2], m2[3])  # "(70 + 50)x"
        rect_c = SurroundingRectangle(m2_grouped, color=YELLOW_KEY, buff=0.1)

        self.play(Create(rect_a), Create(rect_b))
        self.wait(0.3)
        self.play(FadeOut(rect_a), FadeOut(rect_b), FadeIn(rect_c))
        self.wait(0.8)

        # Distributive property
        dist_label = Text("乘法分配律", font_size=26, color=YELLOW_KEY)
        dist_label.next_to(rows, DOWN, buff=0.8)

        dist_eq = MathTex(
            r"a \cdot c", r"+", r"b \cdot c", r"=", r"(a + b) \cdot c",
            font_size=36,
        )
        dist_eq[0].set_color(MING_BLUE)
        dist_eq[2].set_color(HONG_GREEN)
        dist_eq[4].set_color(YELLOW_KEY)
        dist_eq.next_to(dist_label, DOWN, buff=0.3)

        self.play(Write(dist_label))
        self.play(Write(dist_eq))
        self.wait(1.0)

        # Substitution
        sub = MathTex(
            r"70 \cdot x", r"+", r"50 \cdot x", r"=", r"(70 + 50) \cdot x",
            font_size=32,
        )
        sub[0].set_color(MING_BLUE)
        sub[2].set_color(HONG_GREEN)
        sub[4].set_color(YELLOW_KEY)
        sub.next_to(dist_eq, DOWN, buff=0.5)

        self.play(Write(sub))
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            row1, row2, rect_a, rect_b, rect_c,
            dist_label, dist_eq, sub, title,
        )))
        self.wait(0.2)

    # ── Scene 6: Summary (~25s) ────────────────────────────────────
    def s6_summary(self) -> None:
        core = Text("速度和 × 相遇时间 = 总路程", font_size=48, color=YELLOW_KEY)
        core.move_to(ORIGIN)
        self.play(Write(core))
        self.wait(1.0)

        v1 = Text("相遇时间 = 总路程 ÷ 速度和", font_size=32, color=WHITE)
        v2 = Text("速度和 = 总路程 ÷ 相遇时间", font_size=32, color=WHITE)
        v3 = Text("甲路程 + 乙路程 = 总路程", font_size=32, color=WHITE)
        variants = VGroup(v1, v2, v3).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        variants.next_to(core, DOWN, buff=0.8)

        for v in variants:
            self.play(FadeIn(v, shift=UP * 0.2))
            self.wait(0.4)

        self.wait(0.6)

        final = Text(
            "记住这个模型，走路、开车、挖隧道……道理都一样！",
            font_size=28, color=GREY_SUB,
        )
        final.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(final, shift=UP * 0.3))
        self.wait(2.0)

        self.play(FadeOut(VGroup(core, variants, final)))
        self.wait(0.5)

    # ── Main construct ─────────────────────────────────────────────
    def construct(self) -> None:
        self.s1_intro()
        self.s2_diagram()
        self.s3_method1()
        self.s4_method2()
        self.s5_connection()
        self.s6_summary()
