def count_text(text):
    lines = len(text.splitlines())
    # 【填空1】用 len 和 split() 数出词数，赋值给 words
    words = len(text.split())
    # 【填空2】用 len 数出字符数，赋值给 chars
    chars = len(text)
    # 【填空3】把 lines / words / chars 打包成一个元组返回
    return lines,words,chars
