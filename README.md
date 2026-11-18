# Python 课堂日常作业合集

本仓库集中存放 Python 课程的课堂日常作业（区别于独立的实验项目仓库）。代码以函数、递归、标准库绘图与组合数据类型应用为主，按章节/主题分目录管理。

## 目录结构

```
python-homework/
├── ch5_function/                 # 第 5 章 函数与代码复用
│   ├── 5.1_tianzige.py           # 习题 5.1 字符田字格绘制（函数 + 参数控制大小）
│   ├── koch_snowflake.py         # 科赫雪花（递归，0~4 阶，turtle）
│   └── monte_carlo.py            # 蒙特卡罗方法手搓图形（随机投点估算 π，turtle）
├── ch6_collection/               # 第 6 章 组合数据类型
│   ├── poem_solo.py              # 教材 P205 代码6A 孤独的古诗词（集合去重判定）
│   ├── report_wordcloud.py       # 统计"十五五"规划报告热词频率并生成词云
│   └── trace_draw.py             # 自动轨迹绘制（解析指令数据，彩色内部交叉 + 黑色外轮廓）
├── notes/
│   └── if_name_main.md           # 笔记：if __name__ == '__main__' 的含义与作用
├── docs/
│   ├── 实验报告.md               # 本仓库作业汇总报告（含运行结果与截图）
│   └── images/                   # 运行输出截图、词云图与词频表
├── README.md
└── requirements.txt
```

## 作业清单

| 序号 | 题目 | 文件 | 知识点 |
|------|------|------|--------|
| 1 | `if __name__ == '__main__':` 的含义，why? | `notes/if_name_main.md` | 模块入口、直接运行与导入的区别 |
| 2 | 习题 5.1 字符田字格绘制 | `ch5_function/5.1_tianzige.py` | 自定义函数、参数控制、循环嵌套 |
| 3 | 绘制科赫雪花（0~4 阶） | `ch5_function/koch_snowflake.py` | 递归函数、turtle 绘图 |
| 4 | 蒙特卡罗方法手搓图形 | `ch5_function/monte_carlo.py` | 随机数、概率估算 π、turtle 散点 |
| 5 | 孤独的古诗词（P205 代码6A） | `ch6_collection/poem_solo.py` | 字符串处理、集合去重、`len(s) == len(set(s))` 判定 |
| 6 | 统计"十五五"规划报告热词 + 词云 | `ch6_collection/report_wordcloud.py` | jieba 分词、词频统计、wordcloud 词云、中文字体处理 |
| 7 | 自动轨迹绘制 | `ch6_collection/trace_draw.py` | 指令数据解析、参数校验、turtle 颜色与转向控制（15 条指令：彩色交叉 + 黑色外轮廓） |

## 运行环境

- Python 3.10+
- 第 2~5、7 题仅使用标准库（`turtle`、`random`、`math`、`re`、`argparse`）。
- 第 6 题需要第三方库：`jieba`、`wordcloud`、`matplotlib`（`wordcloud` 依赖 `matplotlib`）。

```bash
pip install -r requirements.txt
```

## 运行方式

```bash
# 5.1 字符田字格（命令行字符输出）
python ch5_function/5.1_tianzige.py

# 科赫雪花（弹出 turtle 窗口，输入阶数 0~4）
python ch5_function/koch_snowflake.py

# 蒙特卡罗估算 π（弹出 turtle 窗口，输入投点数量）
python ch5_function/monte_carlo.py

# 孤独的古诗词（终端输出三首诗的判定结果与重复字）
python ch6_collection/poem_solo.py

# 十五五报告热词 + 词云（生成 report_hotwords.csv 与 report_wordcloud.png）
python ch6_collection/report_wordcloud.py

# 自动轨迹绘制（弹出 turtle 窗口，绘制彩色内部轨迹与黑色外轮廓）
python ch6_collection/trace_draw.py

# 只解析指令、不弹窗（无图形环境自测用）
python ch6_collection/trace_draw.py --no-gui

# 使用外部指令文件
python ch6_collection/trace_draw.py --file my_trace.txt
```

## 第 6 题说明

- **语料来源**：公开新闻稿节选，直接内置在 `report_wordcloud.py` 的 `TEXT` 常量中，运行时不依赖外部 txt 文件；如需统计其他文本，替换 `TEXT` 即可。
- **中文字体**：词云必须指定中文字体，否则汉字会显示为方框。程序按 `FONT_CANDIDATES` 依次查找 `msyh.ttc`、`simhei.ttf`、`simsun.ttc` 及 Linux 下的 Noto CJK 字体，找不到时只输出词频表并提示。
- **输出文件**：`report_hotwords.csv`（`utf-8-sig` 编码，Excel 直接打开不乱码）、`report_wordcloud.png`（词云图）。

## 说明

- 图形类题目依赖 turtle 窗口，请在本地带图形界面的环境运行；在线无图形环境可用 `--no-gui` 验证解析逻辑。
- 每道题文件末尾都使用 `if __name__ == '__main__':` 作为程序入口，便于被其他模块导入时不自动执行。
