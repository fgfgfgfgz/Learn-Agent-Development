# 批量文本统计工具

## 这是什么

给一个或多个 txt 文件，统计每个文件的行数、词数、字符数，把结果打印出来并追加写回文件。M2 里程碑成品，纯 Python 标准库，无须安装任何依赖。

## 怎么运行

```bash
python stats.py 示例文本.txt
python stats.py 文件1.txt 文件2.txt 文件3.txt
```

运行结果会打印在屏幕上，同时追加写入被统计的文件末尾。

## 示例输出

```
示例文本.txt: 3 行 / 14 词 / 53 字符
```

（这是真实跑出来的结果，不是编的——你可以用 `练习/20261128/示例文本.txt` 复现。）

## 用到了什么

- Python 3（只用标准库：sys）
- 无第三方依赖
- 三个模块：`stats_core.py`（统计逻辑）、`file_io.py`（文件读写）、`stats.py`（主程序入口）

## 怎么改

- 想换统计规则：改 `stats_core.py` 的 `count_text()`
- 想换结果格式：改 `file_io.py` 的 `write_result()` 里那行 f-string
