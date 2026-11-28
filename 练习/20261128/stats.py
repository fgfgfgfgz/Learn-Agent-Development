import sys
import stats_core
import file_io

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python stats.py 文件1.txt 文件2.txt ...")
        sys.exit()
    for path in sys.argv[1:]:              # 【填空6】参数从 sys.argv 的哪个下标开始？
        text = file_io.read_file(path)
        # 【填空7】调用 stats_core.count_text(text)，用三个变量接收返回的元组
        lines, words, chars = stats_core.count_text(text)
        file_io.write_result(path, lines, words, chars)
        print(f"{path}: {lines} 行 / {words} 词 / {chars} 字符")

