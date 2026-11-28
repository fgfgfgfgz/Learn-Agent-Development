print("=== 1. 你问的 a\\n\\rb\\n\\r ===")
s = "a\n\rb\n\r"
print("repr:", repr(s))
print("split()     =", s.split())
print("splitlines()=", s.splitlines())

print()
print("=== 2. 更常见的 Windows 换行 a\\r\\nb\\r\\n ===")
s2 = "a\r\nb\r\n"
print("repr:", repr(s2))
print("split()     =", s2.split())
print("splitlines()=", s2.splitlines())

print()
print("=== 3. 单个 \\r 单独出现 ===")
s3 = "a\rb"
print("repr:", repr(s3))
print("split()     =", s3.split())
print("splitlines()=", s3.splitlines())

print()
print("=== 4. 带参数切：split('\\n') 遇到 \\r\\n 会留尾巴 ===")
s4 = "a\r\nb\r\n"
print("split('\\n') =", s4.split("\\n"), "← 每项末尾残留 \\r")
print("split()      =", s4.split(), "← 无参数干净")
