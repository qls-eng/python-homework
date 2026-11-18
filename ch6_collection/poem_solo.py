# -*- coding: utf-8 -*-
"""
教材 P205 代码 6A：孤独的古诗词
题目：一首古诗词去掉标点后，若每个汉字都只出现一次，称它为“孤独的古诗”。
      教材原代码用集合去重后比较长度：len(s) == len(set(s))。
本程序在原代码基础上扩展为：
    1. 把判定封装成函数，可批量处理多首诗词；
    2. 对“不孤独”的诗词，列出重复字及其出现次数，说明判定依据；
    3. 完成思考练习 6.3：换几首不同的诗，观察输出差异。
"""

import re

# 判断时只保留汉字，去掉标点、空格、换行
_HANZI_PATTERN = re.compile(r"[^\u4e00-\u9fa5]")


def strip_punct(text: str) -> str:
    """去掉标点、数字、空格等非汉字字符，只留汉字。"""
    return _HANZI_PATTERN.sub("", text)


def is_lonely_poem(text: str) -> bool:
    """判断一首诗是否为“孤独的古诗”。

    参数:
        text: 诗词原文，可以带标点。
    返回:
        True 表示去掉标点后每个汉字只出现一次。
    说明:
        这里沿用了教材的做法：先去标点，再比较“字符个数”与“集合元素个数”。
        集合会自动去重，两者相等即说明没有重复字。
    """
    poem = strip_punct(text)
    return len(poem) == len(set(poem))


def duplicate_chars(text: str) -> dict[str, int]:
    """返回重复出现的汉字及其次数，按次数从多到少排序。"""
    poem = strip_punct(text)
    counts: dict[str, int] = {}
    for ch in poem:
        counts[ch] = counts.get(ch, 0) + 1
    return {ch: n for ch, n in sorted(counts.items(), key=lambda kv: -kv[1]) if n > 1}


def check_poem(title: str, author: str, text: str) -> bool:
    """判定一首诗并打印结果，返回判定值。"""
    poem = strip_punct(text)
    lonely = is_lonely_poem(text)

    print(f"《{title}》 {author}")
    print(f"  原文：{text}")
    print(f"  去标点后共 {len(poem)} 字，不同汉字 {len(set(poem))} 个")

    if lonely:
        print("  判定：True —— 孤独的古诗（每个汉字只出现一次）")
    else:
        dups = duplicate_chars(text)
        detail = "、".join(f"{ch}({n}次)" for ch, n in dups.items())
        print(f"  重复字：{detail}")
        print("  判定：False —— 存在重复汉字，不是孤独的古诗")
    print()
    return lonely


# 示例诗词：一首“孤独”，两首“不孤独”，用于对照验证判定逻辑
POEMS = [
    ("独坐敬亭山", "李白", "众鸟高飞尽，孤云独去闲。相看两不厌，只有敬亭山。"),
    ("春晓", "孟浩然", "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。"),
    ("鹿柴", "王维", "空山不见人，但闻人语响。返景入深林，复照青苔上。"),
]


if __name__ == "__main__":
    print("===== 孤独的古诗词判定 =====\n")
    lonely_count = 0
    for title, author, text in POEMS:
        if check_poem(title, author, text):
            lonely_count += 1

    print(f"共检查 {len(POEMS)} 首，其中孤独的古诗 {lonely_count} 首。")
    print("\n说明（思考练习 6.3）：换一首诗后，输出的字数和不同汉字个数会随之变化；")
    print("只要出现任意一个重复汉字，两个数字就不相等，判定结果即为 False。")
