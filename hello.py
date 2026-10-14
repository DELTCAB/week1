name = input("请输入你的名字：")
age = input("请输入你的年龄：")
print(f"你好，{name}！你今年{age}岁。")

"""
next_year = age + 1  # 这个会报错，因为age是字符串，不能直接相加
print(f"明年你将{next_year}岁。")
"""

next_year = int(age) + 1
print(f"明年你将{next_year}岁。")