import tasks
import ui
import logic

todo = tasks.load_tasks()                # 原来这里是写死的 todo = [...] ，改成从文件读

while True:
    print("\n===== 待办清单 =====")
    print("1. 查看清单")
    print("2. 添加任务")
    print("3. 检查某项")
    print("4. 退出")

    choice = input("请选择 1-4：")

    if choice == "1":
        ui.show_tasks(todo)
    elif choice == "2":
        new = input("输入新任务：")
        print(logic.add_task(todo, new))
    elif choice == "3":
        target = input("要检查哪项：")
        print(logic.check_task(todo, target))
    elif choice == "4":
        print("再见！")
        break
    else:
        print("输入有误，请输入 1-4")

