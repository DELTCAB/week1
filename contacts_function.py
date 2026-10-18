def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"已添加{name}")

def query_contact(contacts, name):
        if name in contacts:
            print(f"{name}的电话是：{contacts[name]}")
        else:
            print(f"没有找到该联系人")

def delete_contact(contacts, name):
        if name in contacts:
            del contacts[name]
            print(f"已删除{name}")
        else:
            print(f"未找到该联系人")

def list_contacts(contacts):
    if contacts:
        print("所有联系人：")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("通讯录为空")

#主程序
contacts = {}

while True:
    print("\n1. 添加  2. 查询  3. 删除  4. 列出  5. 退出")
    choice = input("请选择：")

    if choice == '1':
        name = input("请输入联系人姓名：")
        phone = input("请输入联系人电话：")
        add_contact(contacts, name, phone)
    elif choice == '2':
        name = input("请输入要查询的联系人姓名：")
        query_contact(contacts, name)
    elif choice == '3':
        name = input("请输入要删除的联系人姓名：")
        delete_contact(contacts, name)
    elif choice == "4":
        list_contacts(contacts)
    elif choice == "5":
        break
    else:
        print("无效选择")