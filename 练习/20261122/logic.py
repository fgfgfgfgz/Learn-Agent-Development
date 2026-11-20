FILE = "tasks.txt"
import tasks

def add_task(todo, new):
    """添加任务"""
    todo.append(new)
    tasks.save_tasks(todo)              # 改动①：添加后立即写回文件
    return f"已添加「{new}」"


def check_task(todo, target):
    """检查某项是否在清单里"""
    if target in todo:
        return f"「{todo}」在清单里"
    else:
        return f"「{todo}」不在清单里"
