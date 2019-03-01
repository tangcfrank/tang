listabc = ['123','dd','66']

"""123 in listabc
listabc*=5
for each in listabc:
    print(each,len(each))
print(listabc.count('123'))
listabc.index('123',4,9)
listabc.reverse()
print(listabc)"""

print("----------------------斐波那契数列------------------")
def ff(n):
    if n == 1 or n == 2:
        return  1
    elif n > 2:
        return ff(n-1) + ff(n-2)
    else:
        print('输入有误!')
        return -1

month1 = int(input('请输入经历月份：'))
if month1 != -1:
    result = ff(month1)
    print('一对兔子经过 %d 月后产生了 %d 只兔子' % (month1,result))

print('-------------------------iteretion(迭代)-------------------')
def fd(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 0:
        return -1
    while (n-2) > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
    return n3
result = fd(12)
print("12月后产生了%d只兔子" % result)
