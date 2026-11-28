import sys
import stats_core
import file_io

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python stats.py 文件1.txt 文件2.txt ...")
        sys.exit()
    for path in sys.argv[1:]:
        text = file_io.read_file(path)
        lines, words, chars = stats_core.count_text(text)
        file_io.write_result(path, lines, words, chars)
        print(f"{path}: {lines} 行 / {words} 词 / {chars} 字符")
