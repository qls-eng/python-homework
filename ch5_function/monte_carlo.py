# -*- coding: utf-8 -*-
"""
课堂作业：蒙特卡罗方法手搓图形
原理：在边长为 2 的正方形（坐标范围 [-1, 1]）内随机大量投点，
      正方形面积为 4，内切单位圆面积为 π。
      落入圆内的点 / 总点数 ≈ 圆面积 / 正方形面积 = π / 4，
      因此 π ≈ 4 × 圆内点数 / 总点数。
图形：圆内点画红色，圆外点画蓝色，直观"手搓"出一个圆。
"""

import random
import turtle


def draw_frame(t, scale: int) -> None:
    """绘制正方形边框和内切单位圆。"""
    # 正方形边框
    t.penup()
    t.goto(-scale, -scale)
    t.pendown()
    for _ in range(4):
        t.forward(2 * scale)
        t.left(90)

    # 内切单位圆（半径 scale，圆心在原点）
    t.penup()
    t.goto(0, -scale)
    t.pendown()
    t.circle(scale)


def monte_carlo_pi(t, n_points: int, scale: int = 200) -> float:
    """随机投点，绘制散点并返回估算的 π 值。"""
    inside = 0

    for _ in range(n_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x * x + y * y <= 1:
            inside += 1
            t.color("red")             # 圆内：红色
        else:
            t.color("blue")            # 圆外：蓝色

        t.penup()
        t.goto(x * scale, y * scale)
        t.pendown()
        t.dot(3)

    return 4 * inside / n_points


def main() -> None:
    n_points = int(input("请输入投点数量（建议 500~2000）: "))
    scale = 200

    screen = turtle.Screen()
    screen.title("蒙特卡罗方法估算 π")
    screen.setup(width=600, height=600)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    draw_frame(t, scale)
    pi_estimate = monte_carlo_pi(t, n_points, scale)

    print(f"投点总数：{n_points}")
    print(f"估算得到的 π ≈ {pi_estimate:.4f}")

    turtle.done()


if __name__ == "__main__":
    main()
