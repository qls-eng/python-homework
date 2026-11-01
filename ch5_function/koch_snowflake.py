# -*- coding: utf-8 -*-
"""
课堂作业：绘制科赫雪花（Koch Snowflake），根据阶数生成 0~4 阶。
思路：科赫曲线是递归图形。
  - 0 阶：一条直线段；
  - 高阶：把一条线段三等分，中间一段替换成等边三角形的两条边（凸起），
          再对每一小段递归处理。
  - 雪花由三条科赫曲线首尾相接构成。
"""

import turtle


def koch_curve(t, length: float, depth: int) -> None:
    """绘制一条 depth 阶科赫曲线。

    参数:
        t: turtle 画笔对象
        length: 当前线段长度
        depth: 递归阶数，0 表示直接画直线
    """
    if depth == 0:
        t.forward(length)
        return

    length /= 3
    koch_curve(t, length, depth - 1)   # 第 1 段
    t.left(60)
    koch_curve(t, length, depth - 1)   # 凸起左斜边
    t.right(120)
    koch_curve(t, length, depth - 1)   # 凸起右斜边
    t.left(60)
    koch_curve(t, length, depth - 1)   # 第 3 段


def koch_snowflake(t, depth: int, length: float = 320) -> None:
    """绘制 depth 阶科赫雪花（三条科赫曲线围成等边三角形）。"""
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)


def main() -> None:
    depth = int(input("请输入科赫雪花阶数（0~4）: "))
    depth = max(0, min(4, depth))      # 限制在 0~4 阶范围内

    screen = turtle.Screen()
    screen.title(f"科赫雪花 {depth} 阶")
    screen.setup(width=700, height=700)

    t = turtle.Turtle()
    t.speed(0)                         # 最快绘制
    t.hideturtle()

    # 移动到起点，让雪花在窗口中居中
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    koch_snowflake(t, depth)

    turtle.done()


if __name__ == "__main__":
    main()
