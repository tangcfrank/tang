print('-------------------------我爱鱼C工作室--------------------')
import random
secret=random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
inum = 3  # 想让你输入几次就几次
while guess != secret:
    if guess > secret:
        inum-=1
        print('数字大了，剩余%s次机会!'%inum)
        temp=input('请重新输入：')
        guess=int(temp)
        if inum == 1 and guess !=secret:
            print('你是猴子请来的逗B,3次机会已经用完了！')
            break
    elif guess < secret:
        inum -= 1
        print('数字小了，剩余%s次机会,重新输入：'%inum)
        temp=input('请重新输入：')
        guess = int(temp)
        if inum == 1 and guess != secret:
            print('你是猴子请来的逗B,3次机会已经用完了！')
            break
if guess == secret:
    print('我草，你是小甲鱼心里的蛔虫吗？！')
    print('哼！猜中了也没有奖励！')
print('游戏结束，不玩啦！')