# -*- coding: utf-8 -*-
"""
习题 5.1 字符田字格绘制
题目：编写程序，用字符方式打印田字格；采用函数方式，以格子数 n 为参数，
      能够根据参数绘制任意大小的 n×n 田字格。
"""


def draw_grid(n: int) -> None:
    """用字符打印 n×n 的田字格。

    参数:
        n: 横向 / 纵向小格子的数量，必须为正整数。
    说明:
        每个小格子宽 4 个字符、高 4 行；横线由 '+' 与 '----' 组成，
        竖线由 '|' 与四个空格组成。
    """
    if not isinstance(n, int) or n <= 0:
        print("宽度必须为大于 0 的正整数")
        return

    horizontal = "+----" * n + "+"   # 一条横向边框线
    vertical = "|    " * n + "|"    # 一条纵向边框 + 内部空白

    for _ in range(n):
        print(horizontal)           # 每个格子先画一条上边
        for _ in range(4):          # 每个格子内部画 4 行竖线
            print(vertical)
    print(horizontal)               # 最后补一条底边


if __name__ == "__main__":
    n = int(input("请输入田字格格子数 n: "))
    draw_grid(n)
