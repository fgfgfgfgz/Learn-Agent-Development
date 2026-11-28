print("=== 1. 你问的 \\x05 (ENQ) 会被 split() 切吗？===")
s = "a\x05b"
print("repr:", repr(s))
print("split()     =", s.split(), "← \\x05 没被切开" if s.split()==[s] else "")
print("'\\x05'.isspace() =", "\x05".isspace())

print()
print("=== 2. 全部 ASCII 里，isspace() 为 True 的字符 ===")
spaces = [(i, repr(chr(i))) for i in range(128) if chr(i).isspace()]
for code, ch in spaces:
    print(f"  U+{code:04X}  {ch:8} 十进制 {code}")

print()
print("=== 3. 这些字符真能被 split() 切吗？（逐个验证）===")
for code, _ in spaces:
    ch = chr(code)
    s = "a" + ch + "b"
    ok = s.split() == ["a", "b"]
    print(f"  U+{code:04X}: split() -> {s.split()}  {'✓切' if ok else '✗没切'}")

print()
print("=== 4. 连续混合空白，split() 合并成一个分隔符 ===")
s = "a \t\n\r\x0b\x0cb"
print("repr:", repr(s))
print("split() =", s.split())

print()
print("=== 5. 非 ASCII 的 Unicode 空白 ===")
for ch in ["\u00a0", "\u2003", "\u3000", "\u2028", "\u200b"]:
    print(f"  U+{ord(ch):04X} {ch!r}: isspace()={ch.isspace()}  split验证={'a'+ch+'b'.split() if False else ('a'+ch+'b').split()}")
