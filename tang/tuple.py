'''temp = ("ss","dd","gg","ff")
temp = temp[:2] +("hh",) +temp[2:]
temp'''

temp = "{0} love {1}.{2}".format("I","t","com")
print(temp)
temp = "{a} love {b}.{c}".format(a="I",b="t",c="com")
print(temp)
temp = '%c %c %c' % (97,98,99)
print(temp)

'''def disfun(price,rate):
    final_price = price + rate
    return final_price
print(disfun(4,5))
old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = disfun(old_price,rate)
print('打折后的价格是：',new_price)'''

print('------------------------lambda-----------------------')
s = lambda x, y: x + y
print(s(5,4))

print('-----------------------------filter---------------------')
print(list(filter(lambda x:x % 2,range(20))))

print('-----------------------------map-----------------------')

print(list(map(lambda x: x * 2,range(10))))

print('---------------------recursion(递归)--------------------------')
import sys
sys.setrecursionlimit(10000)

'''def chengji(x):
    result = x
    for i in range(1,x):
        result *=i
    return result

temp = int(input("输入一个正整数："))
result=chengji(temp)
print("%d 的阶乘是：%d" % (temp,result))'''

def recfun(x):
    if x == 1:
        return 1;
    else:
        return x*recfun(x-1)

num1 = int(input('输入一个正整数：'))
result = recfun(num1)
print('%d 的阶乘是：%d' % (num1,result))









