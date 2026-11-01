# Python 课堂日常作业合集

本仓库集中存放 Python 课程的课堂日常作业（区别于独立的实验项目仓库）。代码以函数、递归、标准库绘图为主，按章节/主题分目录管理。

## 目录结构

```
python-homework/
├── ch5_function/                 # 第 5 章 函数与代码复用
│   ├── 5.1_tianzige.py           # 习题 5.1 字符田字格绘制（函数 + 参数控制大小）
│   ├── koch_snowflake.py         # 科赫雪花（递归，0~4 阶，turtle）
│   └── monte_carlo.py            # 蒙特卡罗方法手搓图形（随机投点估算 π，turtle）
├── notes/
│   └── if_name_main.md           # 笔记：if __name__ == '__main__' 的含义与作用
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

## 运行环境

- Python 3.10+
- 绘图题目仅使用标准库 `turtle`、`random`，无需安装第三方依赖。

## 运行方式

```bash
# 5.1 字符田字格（命令行字符输出）
python ch5_function/5.1_tianzige.py

# 科赫雪花（弹出 turtle 窗口，输入阶数 0~4）
python ch5_function/koch_snowflake.py

# 蒙特卡罗估算 π（弹出 turtle 窗口，输入投点数量）
python ch5_function/monte_carlo.py
```

## 说明

- 图形类题目依赖 turtle 窗口，请在本地带图形界面的环境运行；在线无图形环境无法弹窗显示。
- 每道题文件末尾都使用 `if __name__ == '__main__':` 作为程序入口，便于被其他模块导入时不自动执行。
