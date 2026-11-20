FILE = "tasks.txt"


def show_tasks(tasks):
    """显示所有任务，带编号"""
    if not tasks:
        print("清单是空的，先添加一项吧")
        return
    i = 1
    for t in tasks:
        print(f"{i}. {t}")
        i = i + 1


def add_task(tasks, new):
    """添加任务"""
    tasks.append(new)
    save_tasks(tasks)              # 改动①：添加后立即写回文件
    return f"已添加「{new}」"


def check_task(tasks, target):
    """检查某项是否在清单里"""
    if target in tasks:
        return f"「{target}」在清单里"
    else:
        return f"「{target}」不在清单里"


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


def save_tasks(tasks):             # 改动③：新增，把清单写回文件
    """把清单写回文件，每行一项"""
    with open(FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")


todo = load_tasks()                # 原来这里是写死的 todo = [...] ，改成从文件读

while True:
    print("\n===== 待办清单 =====")
    print("1. 查看清单")
    print("2. 添加任务")
    print("3. 检查某项")
    print("4. 退出")

    choice = input("请选择 1-4：")

    if choice == "1":
        show_tasks(todo)
    elif choice == "2":
        new = input("输入新任务：")
        print(add_task(todo, new))
    elif choice == "3":
        target = input("要检查哪项：")
        print(check_task(todo, target))
    elif choice == "4":
        print("再见！")
        break
    else:
        print("输入有误，请输入 1-4")