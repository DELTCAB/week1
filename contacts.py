#"Day3: contacts manager with dictionary"

contacts = {}

while True:
    print("\n1. 添加  2. 查询  3. 删除  4. 列出  5. 退出")
    choice = input("请选择: ")

    if choice == "1":
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        contacts[name] = phone
        print(f"已添加 {name}")
    elif choice == "2":
        name = input("请输入要查询的姓名：")
        if name in contacts:
            print(f"{name} 的电话是：{contacts[name]}")
        else:
            print("查无此人")
    elif choice == "3":
        name = input("请输入要删除的姓名：")
        if name in contacts:
            del contacts[name]
            print(f"已删除 {name}")
        else:
            print("查无此人")
    elif choice == "4":
        if contacts:
            print("所有联系人：")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("当前通讯录为空")
    elif choice == "5":
        break
    else:
        print("无效选项")