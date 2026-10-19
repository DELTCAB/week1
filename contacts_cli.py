import argparse
import json
import sys

def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("数据文件损坏，已重置为空通讯录")
        return {}

def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(description="通讯录管理工具")
    subparsers = parser.add_subparsers(dest="command")

    # add 子命令
    add_parser = subparsers.add_parser("add", help="添加联系人")
    add_parser.add_argument("name", help="姓名")
    add_parser.add_argument("phone", help="电话")

    # query 子命令
    query_parser = subparsers.add_parser("query", help="查询联系人")
    query_parser.add_argument("name", help="姓名")

    # delete 子命令
    delete_parser = subparsers.add_parser("delete", help="删除联系人")
    delete_parser.add_argument("name", help="姓名")

    # list 子命令
    subparsers.add_parser("list", help="列出所有联系人")

    # 没有参数时显示帮助
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()
    contacts = load_contacts()

    if args.command == "add":
        contacts[args.name] = args.phone
        save_contacts(contacts)
        print(f"已添加 {args.name}")
    elif args.command == "query":
        if args.name in contacts:
            print(f"{args.name} 的电话是：{contacts[args.name]}")
        else:
            print("未找到该联系人")
    elif args.command == "delete":
        if args.name in contacts:
            del contacts[args.name]
            save_contacts(contacts)
            print(f"已删除 {args.name}")
        else:
            print("未找到该联系人")
    elif args.command == "list":
        if contacts:
            print("所有联系人：")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("通讯录为空")

if __name__ == "__main__":
    main()