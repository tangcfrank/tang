import random
import os,sys
#随机产生7个数，并且产生的绿球不能重复

def numA(num):
    count = 0
    a = []
    while count < num:
        if num == 6:
            a.append(random.randint(1, 32))
            if count > 0:#0
                for each in a[:-1]:
                    if a[len(a)-1] in a[:-1]:
                        a.remove(each)
                        count -= 1
                        continue
                    elif (a[len(a)-1] + 1) in a[:-1] or (a[len(a)-1] - 1) in a[:-1]:
                        a.remove(each)
                        count -= 1
                        continue
        elif num == 1:
            a.append(random.randint(1, 16))
        count += 1
    return sorted(a)

# #与上期进行比较
# oldor = [3, 13, 15, 18, 21, 33]
# oldbule = [16]
# def compareold():
#     b = numA(6)
#     for i in range(5):
#         for each in b:
#             if each in oldor:
#                 b.remove(each)
#                 return sorted(b)
#     if oldbule[0] in numA(1):
#         b.remove(oldbule[0])
#         return b
# #补全列表
# def completionNew():
#     if len(compareold()) != 6:
#         compareold().append(random.randint(1,32))


#为了输出美观，遍历一下列表，调整了一下格式
def printnumA(num1):
    for each in numA(num1):
        print(each, end = ' ')
    print('\n')

#屏幕输出，后面是一些格式调整
def displayoutA(num2):
    print('%d、蓝色球是：' % num2,end = '')
    printnumA(6)
    print('%d、红色球是：'% num2,end = '')
    printnumA(1)

#把前面不想要的写入文件file1.txt，实例是前7注的写入到文件里
def printfileA(num3):
    savea = sys.stdout
    with open('file1.txt','a')  as file1:
        sys.stdout = file1
        displayoutA(num3)
    sys.stdout = savea


#前面num-1注的不要，打印到文件file1.txt,屏幕显示2注，分别是num,num1
def dreamA(num4,num5):
    i = 1
    while True:
        if i < num4 or i < num5 and i != num4:
            printfileA(i)
        elif i == num4 or i == num5:
            displayoutA(i)
        i += 1
        if i == int(num5 + 1):
            break

#文件清空
def clearfile():
    f = open('file1.txt','w')
    f.truncate()


print('----------------------预测下期双色球，百分百中一等奖！就是这么牛B就是这么任性------------------------')
#清空文件file1.txt
clearfile()
#想要第几次的以后2注，例如：想要第8和第9注，那么前面7注放入文件file1.txt里，屏幕显示第8和第9注
dreamA(19,29)
print('---------------------哈哈，实际证明，买彩票是中不了奖，想富有还需努力，少年！-----------------------')






