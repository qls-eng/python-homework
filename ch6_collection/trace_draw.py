# -*- coding: utf-8 -*-
"""
教材“自动轨迹绘制”课堂作业
题目：根据一组指令数据，用 turtle 自动绘制彩色轨迹；指令用逗号分隔，
      每行 6 个数值，依次是：行进距离、转向标志、转向角度、R、G、B。
说明：
    1. 转向标志 0 表示左转，1 表示右转；
    2. R、G、B 取 0~1 之间的浮点数，直接作为 turtle.pencolor 的颜色分量；
    3. 数据可以内置在代码中，也可以用 --file 指定外部 txt 文件（一行一条指令）；
    4. 用 --no-gui 运行只做解析与参数检查，不弹窗，便于无图形环境自测。
"""

import argparse
import sys
from pathlib import Path

# 内置指令：教材示例六条，画出五角星与彩色折线
TRACE_DATA = """\
300,0,144,1,0,0
300,0,144,0,1,0
300,0,144,0,0,1
300,0,144,1,1,0
300,0,108,0,1,1
184,0,72,1,0,1
"""

FIELDS = ("distance", "direction", "angle", "r", "g", "b")


def parse_line(line: str, line_no: int) -> dict:
    """解析一条指令，返回字段字典；格式错误抛 ValueError。

    参数:
        line: 原始文本行，形如 "300,0,144,1,0,0"。
        line_no: 行号，仅用于错误提示。
    """
    parts = [item.strip() for item in line.split(",")]
    if len(parts) != 6:
        raise ValueError(f"第 {line_no} 行字段数应为 6，实际为 {len(parts)}：{line.strip()}")

    try:
        values = [float(item) for item in parts]
    except ValueError as exc:
        raise ValueError(f"第 {line_no} 行存在非数值字段：{line.strip()}") from exc

    record = dict(zip(FIELDS, values))

    if record["direction"] not in (0.0, 1.0):
        raise ValueError(f"第 {line_no} 行转向标志只能为 0 或 1：{line.strip()}")
    for key in ("r", "g", "b"):
        if not 0.0 <= record[key] <= 1.0:
            raise ValueError(f"第 {line_no} 行颜色分量 {key} 超出 0~1：{line.strip()}")

    return record


def load_trace(path: str | None) -> list[dict]:
    """读取指令数据；path 为 None 时使用内置 TRACE_DATA。"""
    text = Path(path).read_text(encoding="utf-8") if path else TRACE_DATA

    records = []
    for line_no, raw in enumerate(text.splitlines(), 1):
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        records.append(parse_line(raw, line_no))
    return records


def describe(records: list[dict]) -> None:
    """打印解析结果表，便于核对每条指令的参数。"""
    print(f"共解析 {len(records)} 条指令：\n")
    for index, record in enumerate(records, 1):
        turn = "左转" if record["direction"] == 0 else "右转"
        color = f"({record['r']:.2f}, {record['g']:.2f}, {record['b']:.2f})"
        print(f"  {index}. 前进 {record['distance']:.0f}，{turn} {record['angle']:.0f}°，"
              f"颜色 RGB{color}")


def draw(records: list[dict]) -> None:
    """用 turtle 按指令绘制彩色轨迹。"""
    import turtle

    screen = turtle.Screen()
    screen.title("自动轨迹绘制")
    screen.setup(width=800, height=700)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(3)
    pen.hideturtle()

    for record in records:
        pen.pencolor(record["r"], record["g"], record["b"])   # 先换颜色
        if record["direction"] == 0:
            pen.left(record["angle"])
        else:
            pen.right(record["angle"])
        pen.fd(record["distance"])

    print("\n绘制完成，关闭窗口结束程序。")
    screen.mainloop()


def main() -> int:
    parser = argparse.ArgumentParser(description="自动轨迹绘制（教材示例）")
    parser.add_argument("--file", help="指令数据文件路径，默认使用内置示例数据")
    parser.add_argument("--no-gui", action="store_true", help="只解析并打印参数，不弹窗绘图")
    args = parser.parse_args()

    try:
        records = load_trace(args.file)
    except ValueError as exc:
        print(f"数据格式错误：{exc}", file=sys.stderr)
        return 1

    describe(records)

    if args.no_gui:
        print("\n已启用 --no-gui：仅完成解析与校验，未绘制图形。")
        return 0

    draw(records)
    return 0


if __name__ == "__main__":
    sys.exit(main())
