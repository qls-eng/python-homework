# -*- coding: utf-8 -*-
"""
课堂作业：统计“十五五”发展规划报告热词频率，并生成词云
题目：统计报告中出现频率较高的词，按词频排序输出，并用 wordcloud 画出词云。
说明：
    1. 语料为公开新闻稿的节选，直接内置在代码中，运行本文件不需要额外准备 txt；
    2. 分词使用 jieba，停用词表内置在模块顶部，可按需要增减；
    3. 词云需要中文字体文件，程序会按候选列表自动查找，找不到时给出提示；
    4. 输出两个文件：report_hotwords.csv（词频表）、report_wordcloud.png（词云图）。
"""

import csv
import os
from collections import Counter
from pathlib import Path

import jieba
from wordcloud import WordCloud

# ============ 可配置参数 ============
BASE_DIR = Path(__file__).resolve().parent          # 输出文件放在脚本所在目录
OUTPUT_CSV = BASE_DIR / "report_hotwords.csv"
OUTPUT_PNG = BASE_DIR / "report_wordcloud.png"
TOP_N = 20          # 终端打印前 N 个高频词
MAX_WORDS = 80      # 词云中最多显示的词数

# 中文字体候选路径：Windows 与 Linux 都可能用到
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]

# 停用词：虚词、泛化动词、无区分度的通用名词
STOPWORDS = {
    "的", "和", "与", "及", "为", "在", "等", "是", "以", "对", "从", "把", "这", "那",
    "了", "着", "并", "要", "中", "上", "也", "都", "就", "而", "其", "之", "于", "由",
    "发展", "推动", "促进", "提升", "加强", "完善", "坚持", "深化", "着力", "积极",
    "全面", "重要", "水平", "能力", "体系", "建设", "加快", "推进", "实现", "进一步",
    "工作", "方面", "问题", "情况", "有关", "各项", "我国", "国家", "时期",
}

# 内置语料：公开新闻稿节选（规划主要领域的中性表述，仅用于词频统计练习）
TEXT = """
十五五时期，经济社会发展坚持高质量发展主题，加快建设现代化产业体系，巩固壮大实体经济根基，
推动科技创新和产业创新深度融合，加快高水平科技自立自强，发展新质生产力。
深入推进数字中国建设，推动人工智能、集成电路、工业母机、高端装备、新能源、新材料、
生物制造、低空经济等产业发展，提升产业链供应链韧性和安全水平。
建设强大国内市场，坚持扩大内需战略基点，纵深推进全国统一大市场建设，促进消费和投资良性互动。
深化重点领域改革，扩大高水平对外开放，稳步扩大制度型开放。
加快农业农村现代化，扎实推进乡村全面振兴，保障粮食和重要农产品稳定安全供给。
优化区域经济布局，促进区域协调发展，推进新型城镇化建设。
完善人口发展战略，着力保障和改善民生，促进高质量充分就业，健全社会保障体系，
推进健康中国建设，积极应对人口老龄化。
加快经济社会发展全面绿色转型，深入推进污染防治攻坚，建设美丽中国，
积极稳妥推进碳达峰碳中和。
坚持教育优先发展，加快建设教育强国、科技强国、人才强国。
推进国家安全体系和能力现代化，建设更高水平平安中国。
加强规划实施保障，确保各项目标任务落地见效。
十五五规划的实施，需要各地区各部门结合实际抓好落实。
"""


# 领域词补充：默认词典会把"十五五"切成"十五"+"五"，这里加入专有说法
CUSTOM_WORDS = [
    "十五五", "新质生产力", "现代化产业体系", "科技自立自强", "数字中国",
    "全国统一大市场", "乡村振兴", "新型城镇化", "碳达峰", "碳中和",
    "低空经济", "工业母机", "人口老龄化", "美丽中国", "平安中国",
]


def find_font() -> str | None:
    """按候选列表查找第一个存在的中文字体，找不到返回 None。"""
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def segment(text: str) -> list[str]:
    """用 jieba 精确模式分词，先补充领域专有词。"""
    for word in CUSTOM_WORDS:
        jieba.add_word(word)
    return jieba.lcut(text)


def count_words(words: list[str]) -> Counter:
    """过滤停用词、单字与纯符号，统计词频。"""
    counter: Counter = Counter()
    for word in words:
        word = word.strip()
        if len(word) < 2:                 # 丢掉单字与标点符号
            continue
        if word in STOPWORDS:
            continue
        counter[word] += 1
    return counter


def save_csv(counter: Counter) -> None:
    """把全部词频写入 CSV（utf-8-sig，Excel 直接打开不乱码）。"""
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["词语", "词频"])
        for word, count in counter.most_common():
            writer.writerow([word, count])


def draw_wordcloud(counter: Counter, font_path: str) -> None:
    """根据词频生成词云并保存为 PNG。"""
    wc = WordCloud(
        font_path=font_path,
        width=1200,
        height=800,
        background_color="white",
        max_words=MAX_WORDS,
        colormap="viridis",
    )
    wc.generate_from_frequencies(dict(counter))
    wc.to_file(OUTPUT_PNG)


def main() -> None:
    print("===== 十五五报告热词统计 =====\n")
    print(f"语料长度：{len(TEXT)} 字（内置节选，无需外部 txt）\n")

    words = segment(TEXT)
    print(f"jieba 分词得到 {len(words)} 个词单元")

    counter = count_words(words)
    print(f"过滤停用词、单字后保留 {len(counter)} 个不同词\n")

    print(f"----- 词频 Top {TOP_N} -----")
    for rank, (word, count) in enumerate(counter.most_common(TOP_N), 1):
        print(f"  {rank:>2}. {word:<10} {count} 次")

    save_csv(counter)
    print(f"\n已写入词频表：{OUTPUT_CSV.name}（共 {len(counter)} 行，utf-8-sig）")

    font = find_font()
    if font is None:
        print("未找到中文字体，跳过词云生成；请在 FONT_CANDIDATES 中补充本机字体路径。")
        return

    print(f"使用字体：{font}")
    draw_wordcloud(counter, font)
    print(f"已生成词云：{OUTPUT_PNG.name}")


if __name__ == "__main__":
    main()
