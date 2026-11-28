def read_file(path):
    # 【填空4】用 with open(path, "r", encoding="utf-8") 打开文件并 read()，返回文本
    with open(path,"r", encoding="utf-8") as f:
        content = f.read()
        return content

def write_result(path, lines, words, chars):
    # 【填空5】用 with open(path, "a", encoding="utf-8") 打开，f.write 一行 f-string 结果
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{path}: {lines}, {words}, {chars}")
