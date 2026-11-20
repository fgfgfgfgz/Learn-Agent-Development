def show_tasks(todo):
    """显示所有任务，带编号"""
    if not todo:
        print("清单是空的，先添加一项吧")
        return
    i = 1
    for t in todo:
        print(f"{i}. {t}")
        i = i + 1