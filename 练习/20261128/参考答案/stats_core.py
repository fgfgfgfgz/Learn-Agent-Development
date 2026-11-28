def count_text(text):
    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    return lines, words, chars
