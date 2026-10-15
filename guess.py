import random

target = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("我想了一个1到100之间的数字，你有7次机会。")

while attempts < max_attempts:
    guess = int(input("请输入你猜的数字: "))
    guess = int(guess)
    attempts += 1

    if guess == target:
        print(f"恭喜你，猜对了！你用了{attempts}次机会。")
        break
    elif guess < target:
        print("猜小了，再试一次。")
    else:
        print("猜大了，再试一次。")

if attempts >= max_attempts and guess != target:
    print(f"很遗憾，次数用完了。正确答案是{target}。")