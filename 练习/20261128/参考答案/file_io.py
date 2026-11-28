def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_result(path, lines, words, chars):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{path}: {lines} 行 / {words} 词 / {chars} 字符\n")
