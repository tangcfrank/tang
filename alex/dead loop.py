import random
print('--------------------预测下期双色球，百分百中一等奖！就是这么牛B就是这么任性----------------------------')
def num(num):
    count = 0
    a = []
    while count < num:
        if num == 6:
            a.append(random.randint(1,32))
        elif num == 1:
            a.append(random.randint(1,16))
        count +=1
    return sorted(a)

def printnum(num1):
    for each in num(num1):
        print(each, end = ' ')
    print('\n')

print('蓝色球是：',end = '')
printnum(6)

print('红色球是：',end = '')
printnum(1)

print('-----------没有中很正常，被骗了吧，哈哈，实际证明，买彩票是中不了奖，想富有还需努力，少年！-----------------------')


'''age = int(input('请输入你的年龄:'))
    if age == suiji:
        print('想的和说的一样！')
        break
    elif age > suiji:
        print('输入的数字大了！')
    elif age < suiji:
        print('输入的数字小了！------！！！@@@@@@@@**********')
    else:
        print('报错，程序错误！----------********************')
    count += 1'''