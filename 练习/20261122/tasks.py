FILE = "tasks.txt"

def load_tasks():                  # 改动②：新增，启动时从文件读清单
    """启动时从文件读取清单；文件不存在就返回空清单"""
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            tasks = []
            for line in f:
                line = line.strip()
                if line:                 # 跳过空行
                    tasks.append(line)
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(todo):             # 改动③：新增，把清单写回文件
    """把清单写回文件，每行一项"""
    with open(FILE, "w", encoding="utf-8") as f:
        for t in todo:
            f.write(t + "\n")