import random
import os,sys
#随机产生7个数，并且产生的绿球不能重复
def num(num):
    count = 0
    a = []
    while count < num:
        if num == 6:
            a.append(random.randint(1, 32))
            if count > 0:
                for each in a[:-1]:
                    if a[len(a)-1] in a[:-1]:
                        a.remove(each)
                        count -= 1
                        continue
        elif num == 1:
            a.append(random.randint(1, 16))
        count += 1
    return sorted(a)

#为了输出美观，遍历一下列表，调整了一下格式
def printnumA(num1):
    for each in num(num1):
        print(each,end = ' ')
    print('\n')

#屏幕输出，后面是一些格式调整
def displayoutA():
    print('蓝色球是：',end = '')
    printnumA(6)
    print('红色球是：',end = '')
    printnumA(1)

#把前面不想要的写入文件file1.txt，实例是前7注的写入到文件里
def printfileA():
    savea = sys.stdout
    with open('file1.txt','a')  as file1:
        sys.stdout = file1
        displayoutA()
    sys.stdout = savea


#前面num-1注的不要，打印到文件file1.txt,屏幕显示2注，分别是num,num1
def dreamA(num,num1):
    i = 0
    while True:
        if i < int(num-1):
            printfileA()
        elif i == num or i == num1:
            displayoutA()
        i += 1
        if i == int(num1 + 1):
            break

#文件清空
def clearfile():
    f = open('file1.txt','w')
    f.truncate()


print('----------------------预测下期双色球，百分百中一等奖！就是这么牛B就是这么任性------------------------')
#清空文件file1.txt
clearfile()
#想要第几次的以后2注，例如：想要第8和第9注，那么前面7注放入文件file1.txt里，屏幕显示第8和第9注
dreamA(8,9)
print('----------------------哈哈，实际证明，买彩票是中不了奖，想富有还需努力，少年！-----------------------')






