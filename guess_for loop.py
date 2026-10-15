import random

target = random.randint(1, 100)
max_attempts = 7

print("我想了一个 1 到 100 之间的数字，你有 7 次机会。")

for attempts in range(1, max_attempts + 1):
    guess = input("请输入你猜的数字：")
    guess = int(guess)

    if guess == target:
        print(f"恭喜你，猜对了！你用了 {attempts} 次。")
        break
    elif guess > target:
        print("大了")
    else:
        print("小了")
else:
    # 只有循环正常结束（没 break）才会执行这里
    print(f"很遗憾，次数用完了。正确答案是 {target}。")